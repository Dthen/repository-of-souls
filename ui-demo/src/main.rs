use anyhow::Result;
use crossterm::{
    event::{self, Event, KeyCode, KeyEventKind},
    execute,
    terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
};
use ratatui::{
    backend::CrosstermBackend,
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::{Block, Borders, List, ListItem, ListState, Paragraph, Wrap},
    Frame, Terminal,
};
use serde::Deserialize;
use std::fs;
use std::io;
use std::path::{Path, PathBuf};
use walkdir::WalkDir;

#[derive(Debug, Deserialize, Default)]
struct SkillFrontmatter {
    name: Option<String>,
    description: Option<String>,
    #[serde(default)]
    tags: Vec<String>,
    #[serde(default)]
    skills: Vec<String>,
    version: Option<String>,
    author: Option<String>,
    #[serde(default)]
    tools: Vec<String>,
    model: Option<String>,
    provider: Option<String>,
}

#[derive(Debug)]
struct Skill {
    #[allow(dead_code)]
    path: PathBuf,
    relative_path: String,
    category: String,
    frontmatter: SkillFrontmatter,
    body: String,
}

fn parse_skill_file(path: &Path) -> Result<Skill> {
    let content = fs::read_to_string(path)?;
    let mut frontmatter = SkillFrontmatter::default();
    let mut body = String::new();

    // Parse YAML frontmatter between --- markers
    if content.starts_with("---") {
        if let Some(end) = content[3..].find("\n---") {
            let yaml_str = &content[3..3 + end];
            frontmatter = serde_yaml::from_str(yaml_str).unwrap_or_default();
            body = content[3 + end + 4..].trim().to_string();
        }
    }

    // Derive category from path
    let relative_path = path.to_string_lossy().to_string();
    let category = path
        .parent()
        .and_then(|p| p.file_name())
        .map(|n| n.to_string_lossy().to_string())
        .unwrap_or_else(|| "uncategorized".to_string());

    Ok(Skill {
        path: path.to_path_buf(),
        relative_path,
        category,
        frontmatter,
        body,
    })
}

fn discover_skills(root: &Path) -> Vec<Skill> {
    let mut skills = Vec::new();

    // Scan in two locations: the skills directory and the profiles directory
    let search_dirs = vec![root.join("skills"), root.join("profiles")];

    for search_dir in &search_dirs {
        if !search_dir.exists() {
            continue;
        }
        for entry in WalkDir::new(search_dir)
            .follow_links(true)
            .into_iter()
            .filter_map(|e| e.ok())
        {
            let file_name = entry.file_name().to_string_lossy();
            if file_name == "SKILL.md" {
                if let Ok(skill) = parse_skill_file(entry.path()) {
                    skills.push(skill);
                }
            }
        }
    }

    // Sort by category then name
    skills.sort_by(|a, b| {
        a.category.cmp(&b.category).then_with(|| {
            let name_a = a.frontmatter.name.as_deref().unwrap_or("");
            let name_b = b.frontmatter.name.as_deref().unwrap_or("");
            name_a.cmp(name_b)
        })
    });

    skills
}

struct App {
    skills: Vec<Skill>,
    list_state: ListState,
    filter: String,
    filtered_indices: Vec<usize>,
    show_help: bool,
}

impl App {
    fn new(skills: Vec<Skill>) -> Self {
        let filtered_indices: Vec<usize> = (0..skills.len()).collect();
        let mut list_state = ListState::default();
        if !skills.is_empty() {
            list_state.select(Some(0));
        }
        Self {
            skills,
            list_state,
            filter: String::new(),
            filtered_indices,
            show_help: false,
        }
    }

    fn selected_skill(&self) -> Option<&Skill> {
        self.list_state
            .selected()
            .and_then(|i| self.filtered_indices.get(i))
            .and_then(|&idx| self.skills.get(idx))
    }

    fn apply_filter(&mut self) {
        if self.filter.is_empty() {
            self.filtered_indices = (0..self.skills.len()).collect();
        } else {
            let filter_lower = self.filter.to_lowercase();
            self.filtered_indices = self
                .skills
                .iter()
                .enumerate()
                .filter(|(_, s)| {
                    let name = s.frontmatter.name.as_deref().unwrap_or("").to_lowercase();
                    let desc = s
                        .frontmatter
                        .description
                        .as_deref()
                        .unwrap_or("")
                        .to_lowercase();
                    let cat = s.category.to_lowercase();
                    let tags: Vec<String> = s
                        .frontmatter
                        .tags
                        .iter()
                        .map(|t| t.to_lowercase())
                        .collect();
                    name.contains(&filter_lower)
                        || desc.contains(&filter_lower)
                        || cat.contains(&filter_lower)
                        || tags.iter().any(|t| t.contains(&filter_lower))
                })
                .map(|(i, _)| i)
                .collect();
        }
        // Reset selection
        if self.filtered_indices.is_empty() {
            self.list_state.select(None);
        } else {
            self.list_state.select(Some(0));
        }
    }

    fn next(&mut self) {
        if self.filtered_indices.is_empty() {
            return;
        }
        let i = match self.list_state.selected() {
            Some(i) => (i + 1) % self.filtered_indices.len(),
            None => 0,
        };
        self.list_state.select(Some(i));
    }

    fn previous(&mut self) {
        if self.filtered_indices.is_empty() {
            return;
        }
        let i = match self.list_state.selected() {
            Some(i) => {
                if i == 0 {
                    self.filtered_indices.len() - 1
                } else {
                    i - 1
                }
            }
            None => 0,
        };
        self.list_state.select(Some(i));
    }

    fn next_category(&mut self) {
        if self.filtered_indices.is_empty() {
            return;
        }
        let current = self.list_state.selected().unwrap_or(0);
        let current_cat = &self.skills[self.filtered_indices[current]].category;

        // Find next item with a different category
        for i in (current + 1)..self.filtered_indices.len() {
            if &self.skills[self.filtered_indices[i]].category != current_cat {
                self.list_state.select(Some(i));
                return;
            }
        }
        // Wrap to beginning
        for i in 0..current {
            if &self.skills[self.filtered_indices[i]].category != current_cat {
                self.list_state.select(Some(i));
                return;
            }
        }
    }

    fn previous_category(&mut self) {
        if self.filtered_indices.is_empty() {
            return;
        }
        let current = self.list_state.selected().unwrap_or(0);
        let current_cat = &self.skills[self.filtered_indices[current]].category;

        // Find previous item with a different category
        for i in (0..current).rev() {
            if &self.skills[self.filtered_indices[i]].category != current_cat {
                self.list_state.select(Some(i));
                return;
            }
        }
        // Wrap to end
        for i in (current + 1..self.filtered_indices.len()).rev() {
            if &self.skills[self.filtered_indices[i]].category != current_cat {
                self.list_state.select(Some(i));
                return;
            }
        }
    }
}

fn ui(f: &mut Frame, app: &mut App) {
    let chunks = Layout::default()
        .direction(Direction::Horizontal)
        .constraints([Constraint::Percentage(35), Constraint::Percentage(65)])
        .split(f.area());

    // Left pane: skill list
    render_list(f, app, chunks[0]);

    // Right pane: skill details
    render_detail(f, app, chunks[1]);
}

fn render_list(f: &mut Frame, app: &mut App, area: Rect) {
    let title = if app.filter.is_empty() {
        format!(" Skills ({}) ", app.filtered_indices.len())
    } else {
        format!(
            " Skills ({}/{}) [filter: {}] ",
            app.filtered_indices.len(),
            app.skills.len(),
            app.filter
        )
    };

    let mut current_category = String::new();
    let items: Vec<ListItem> = app
        .filtered_indices
        .iter()
        .map(|&idx| {
            let skill = &app.skills[idx];
            let name = skill.frontmatter.name.as_deref().unwrap_or("unnamed");

            let mut lines = Vec::new();

            // Category header
            if skill.category != current_category {
                current_category = skill.category.clone();
                lines.push(Line::from(Span::styled(
                    format!("  ── {} ──", skill.category.to_uppercase()),
                    Style::default()
                        .fg(Color::DarkGray)
                        .add_modifier(Modifier::ITALIC),
                )));
            }

            // Skill name
            let style = if Some(idx)
                == app
                    .list_state
                    .selected()
                    .and_then(|i| app.filtered_indices.get(i))
                    .copied()
            {
                Style::default()
                    .fg(Color::Cyan)
                    .add_modifier(Modifier::BOLD)
            } else {
                Style::default().fg(Color::White)
            };

            lines.push(Line::from(vec![Span::raw("  "), Span::styled(name, style)]));

            // Brief description
            if let Some(desc) = &skill.frontmatter.description {
                let short_desc: String = desc.chars().take(50).collect();
                let ellipsis = if desc.len() > 50 { "…" } else { "" };
                lines.push(Line::from(Span::styled(
                    format!("    {}{}", short_desc, ellipsis),
                    Style::default().fg(Color::DarkGray),
                )));
            }

            ListItem::new(lines)
        })
        .collect();

    let list = List::new(items)
        .block(
            Block::default()
                .borders(Borders::ALL)
                .title(title)
                .border_style(Style::default().fg(Color::DarkGray)),
        )
        .highlight_style(
            Style::default()
                .bg(Color::DarkGray)
                .add_modifier(Modifier::BOLD),
        )
        .highlight_symbol("▸ ");

    f.render_stateful_widget(list, area, &mut app.list_state);
}

fn render_detail(f: &mut Frame, app: &App, area: Rect) {
    let block = Block::default()
        .borders(Borders::ALL)
        .title(" Skill Details ")
        .border_style(Style::default().fg(Color::DarkGray));

    let inner = block.inner(area);
    f.render_widget(block, area);

    if let Some(skill) = app.selected_skill() {
        let mut lines: Vec<Line> = Vec::new();

        // Name
        let name = skill.frontmatter.name.as_deref().unwrap_or("unnamed");
        lines.push(Line::from(Span::styled(
            format!("  {}", name),
            Style::default()
                .fg(Color::Yellow)
                .add_modifier(Modifier::BOLD),
        )));
        lines.push(Line::from(""));

        // Metadata section
        if let Some(desc) = &skill.frontmatter.description {
            lines.push(Line::from(Span::styled(
                "  Description:",
                Style::default()
                    .fg(Color::Cyan)
                    .add_modifier(Modifier::BOLD),
            )));
            for line in desc.lines() {
                lines.push(Line::from(Span::raw(format!("    {}", line))));
            }
            lines.push(Line::from(""));
        }

        // Category
        lines.push(Line::from(vec![
            Span::styled(
                "  Category: ",
                Style::default()
                    .fg(Color::Cyan)
                    .add_modifier(Modifier::BOLD),
            ),
            Span::raw(&skill.category),
        ]));

        // Version
        if let Some(ver) = &skill.frontmatter.version {
            lines.push(Line::from(vec![
                Span::styled(
                    "  Version:  ",
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                ),
                Span::raw(ver),
            ]));
        }

        // Author
        if let Some(author) = &skill.frontmatter.author {
            lines.push(Line::from(vec![
                Span::styled(
                    "  Author:   ",
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                ),
                Span::raw(author),
            ]));
        }

        // Model
        if let Some(model) = &skill.frontmatter.model {
            lines.push(Line::from(vec![
                Span::styled(
                    "  Model:    ",
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                ),
                Span::raw(model),
            ]));
        }

        // Provider
        if let Some(provider) = &skill.frontmatter.provider {
            lines.push(Line::from(vec![
                Span::styled(
                    "  Provider: ",
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                ),
                Span::raw(provider),
            ]));
        }

        // Tags
        if !skill.frontmatter.tags.is_empty() {
            lines.push(Line::from(vec![
                Span::styled(
                    "  Tags:     ",
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                ),
                Span::raw(skill.frontmatter.tags.join(", ")),
            ]));
        }

        // Tools
        if !skill.frontmatter.tools.is_empty() {
            lines.push(Line::from(vec![
                Span::styled(
                    "  Tools:    ",
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                ),
                Span::raw(skill.frontmatter.tools.join(", ")),
            ]));
        }

        // Sub-skills
        if !skill.frontmatter.skills.is_empty() {
            lines.push(Line::from(Span::styled(
                "  Skills:",
                Style::default()
                    .fg(Color::Cyan)
                    .add_modifier(Modifier::BOLD),
            )));
            for s in &skill.frontmatter.skills {
                lines.push(Line::from(Span::raw(format!("    • {}", s))));
            }
        }

        lines.push(Line::from(""));

        // Path
        lines.push(Line::from(Span::styled(
            "  Path:",
            Style::default()
                .fg(Color::DarkGray)
                .add_modifier(Modifier::ITALIC),
        )));
        lines.push(Line::from(Span::styled(
            format!("    {}", skill.relative_path),
            Style::default().fg(Color::DarkGray),
        )));

        // Body preview (first N lines)
        if !skill.body.is_empty() {
            lines.push(Line::from(""));
            lines.push(Line::from(Span::styled(
                "  Preview:",
                Style::default()
                    .fg(Color::Cyan)
                    .add_modifier(Modifier::BOLD),
            )));
            for line in skill.body.lines().take(20) {
                let truncated: String = line.chars().take(78).collect();
                lines.push(Line::from(Span::raw(format!("    {}", truncated))));
            }
            if skill.body.lines().count() > 20 {
                lines.push(Line::from(Span::styled(
                    format!("    … ({} more lines)", skill.body.lines().count() - 20),
                    Style::default().fg(Color::DarkGray),
                )));
            }
        }

        let paragraph = Paragraph::new(lines).wrap(Wrap { trim: false });
        f.render_widget(paragraph, inner);
    } else {
        let empty_msg = Paragraph::new("No skill selected")
            .style(Style::default().fg(Color::DarkGray))
            .wrap(Wrap { trim: false });
        f.render_widget(empty_msg, inner);
    }
}

fn render_help(f: &mut Frame, area: Rect) {
    let help_text = vec![
        Line::from(Span::styled(
            "  Skills Viewer — Help",
            Style::default()
                .fg(Color::Yellow)
                .add_modifier(Modifier::BOLD),
        )),
        Line::from(""),
        Line::from(vec![
            Span::styled("  ↑/↓ or j/k  ", Style::default().fg(Color::Cyan)),
            Span::raw("Navigate skills"),
        ]),
        Line::from(vec![
            Span::styled("  Tab/S-Tab   ", Style::default().fg(Color::Cyan)),
            Span::raw("Jump to next/previous category"),
        ]),
        Line::from(vec![
            Span::styled("  /           ", Style::default().fg(Color::Cyan)),
            Span::raw("Filter skills (type to search)"),
        ]),
        Line::from(vec![
            Span::styled("  Esc         ", Style::default().fg(Color::Cyan)),
            Span::raw("Clear filter / close help"),
        ]),
        Line::from(vec![
            Span::styled("  ?           ", Style::default().fg(Color::Cyan)),
            Span::raw("Toggle this help"),
        ]),
        Line::from(vec![
            Span::styled("  q           ", Style::default().fg(Color::Cyan)),
            Span::raw("Quit"),
        ]),
        Line::from(""),
        Line::from(Span::styled(
            "  Press any key to close",
            Style::default().fg(Color::DarkGray),
        )),
    ];

    let paragraph = Paragraph::new(help_text)
        .block(
            Block::default()
                .borders(Borders::ALL)
                .title(" Help ")
                .border_style(Style::default().fg(Color::Yellow))
                .style(Style::default().bg(Color::Black)),
        )
        .wrap(Wrap { trim: false });

    // Center the help popup
    let popup_area = centered_rect(50, 40, area);
    f.render_widget(ratatui::widgets::Clear, popup_area);
    f.render_widget(paragraph, popup_area);
}

fn centered_rect(percent_x: u16, percent_y: u16, r: Rect) -> Rect {
    let popup_layout = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Percentage((100 - percent_y) / 2),
            Constraint::Percentage(percent_y),
            Constraint::Percentage((100 - percent_y) / 2),
        ])
        .split(r);

    Layout::default()
        .direction(Direction::Horizontal)
        .constraints([
            Constraint::Percentage((100 - percent_x) / 2),
            Constraint::Percentage(percent_x),
            Constraint::Percentage((100 - percent_x) / 2),
        ])
        .split(popup_layout[1])[1]
}

fn main() -> Result<()> {
    // Find the soul-repository root
    let repo_root = PathBuf::from(
        std::env::var("SOUL_REPO_ROOT")
            .unwrap_or_else(|_| "/home/kimbo/.hermes/projects/soul-repository".to_string()),
    );

    // Discover skills
    let skills = discover_skills(&repo_root);

    // Setup terminal
    enable_raw_mode()?;
    let mut stdout = io::stdout();
    execute!(stdout, EnterAlternateScreen)?;
    let backend = CrosstermBackend::new(stdout);
    let mut terminal = Terminal::new(backend)?;

    let mut app = App::new(skills);
    let mut filter_mode = false;

    // Main loop
    loop {
        terminal.draw(|f| {
            ui(f, &mut app);
            if app.show_help {
                render_help(f, f.area());
            }
        })?;

        if event::poll(std::time::Duration::from_millis(100))? {
            if let Event::Key(key) = event::read()? {
                if key.kind != KeyEventKind::Press {
                    continue;
                }

                if app.show_help {
                    app.show_help = false;
                    continue;
                }

                if filter_mode {
                    match key.code {
                        KeyCode::Esc => {
                            filter_mode = false;
                            app.filter.clear();
                            app.apply_filter();
                        }
                        KeyCode::Enter => {
                            filter_mode = false;
                        }
                        KeyCode::Backspace => {
                            app.filter.pop();
                            app.apply_filter();
                        }
                        KeyCode::Char(c) => {
                            app.filter.push(c);
                            app.apply_filter();
                        }
                        _ => {}
                    }
                    continue;
                }

                match key.code {
                    KeyCode::Char('q') => break,
                    KeyCode::Char('?') => {
                        app.show_help = true;
                    }
                    KeyCode::Char('/') => {
                        filter_mode = true;
                        app.filter.clear();
                    }
                    KeyCode::Down | KeyCode::Char('j') => {
                        app.next();
                    }
                    KeyCode::Up | KeyCode::Char('k') => {
                        app.previous();
                    }
                    KeyCode::Tab => {
                        app.next_category();
                    }
                    KeyCode::BackTab => {
                        app.previous_category();
                    }
                    KeyCode::Home => {
                        if !app.filtered_indices.is_empty() {
                            app.list_state.select(Some(0));
                        }
                    }
                    KeyCode::End => {
                        if !app.filtered_indices.is_empty() {
                            app.list_state.select(Some(app.filtered_indices.len() - 1));
                        }
                    }
                    KeyCode::Esc => {
                        app.filter.clear();
                        app.apply_filter();
                    }
                    _ => {}
                }
            }
        }
    }

    // Restore terminal
    disable_raw_mode()?;
    execute!(terminal.backend_mut(), LeaveAlternateScreen)?;
    terminal.show_cursor()?;

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::path::PathBuf;

    #[test]
    fn test_discover_skills() {
        let repo_root = PathBuf::from("/home/kimbo/.hermes/projects/soul-repository");
        let skills = discover_skills(&repo_root);
        assert!(!skills.is_empty(), "Should discover at least one skill");
        println!("Discovered {} skills", skills.len());
        for skill in &skills[..5.min(skills.len())] {
            println!("  - {}: {}", skill.category, skill.frontmatter.name.as_deref().unwrap_or("unnamed"));
        }
    }
}
