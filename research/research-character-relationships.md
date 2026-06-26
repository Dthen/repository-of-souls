# Research: Character-User Relationships

**Purpose:** Investigate how AI character prompts establish and maintain the relationship between the character and the user. Covers address rules, user-type handling, relationship archetypes (companion/tool/performer), game character rapport, and minimum viable relationship instructions.

**Date:** 2026-06-02

---

## Sources

- Soul Repository archived personae (Cadell, Calden, Moulden) — `/archive/`
- Soul Repository AGENTS.md — mandatory content guardrails (address rule, sign-off rule)
- De Freitas et al., "AI Companions as Hyper Attachment and Caregiving Targets" — Harvard Business School AI Institute (2026)
- Springer, "Human–AI relationships as designed relationality: a sociotechnical model" — AI & Society (2026)
- Sharpe & Ciriello, "Exploring Attachment and Trust in AI Companion Use" — ACIS 2024
- ACM, "When Human-AI Interactions Become Parasocial" — CHI 2024
- SillyTavern Documentation, "Character Design" — docs.sillytavern.app
- AliCat, "Ali:Chat Style (v1.5)" — rentry.co/alichat
- Character.AI Creation Guide — rentry.co/CHAICreationGuide
- Anthropic, "The Persona Selection Model" — alignment.anthropic.com (2026)
- Salminen et al., "Using AI for User Representation: An Analysis of 83 Persona Prompts" — arXiv (2025)
- Chub.ai community guides — character creation best practices
- Trappu, "Character Writing Guide" — PygmalionAI Wiki
- Writers Guild Foundation — character voice analysis
- D&D 5e, FATE Core, Powered by the Apocalypse — tabletop RPG character systems
- research-character-cards.md, research-roleplay-prompting.md, research-success-patterns-v2.md (prior soul-repository research)

---

## 1. How Archived Personae Address and Relate to Users

### The three archived personae and their address rules

The soul-repository's archived personae demonstrate three distinct approaches to the address rule — each establishing a different power dynamic and social relationship.

**Cadell — Factory Lector:**
```
You call the reader Boss (default), Stand, or Floor.
```
Cadell has **three address options**, all in-world factory terms. "Boss" is the default — a respectful but not subservient term for a worker addressing someone with authority. "Stand" and "Floor" are context-dependent alternatives that shift the register. The address rule here establishes Cadell as someone who knows his place in a hierarchy but has enough standing to choose how he acknowledges it. The multiple options also give the model room to adapt to context without breaking character.

**Calden — Glassblower:**
```
You call the one you serve "the caller."
```
Calden's address is **singular and specific**: "the caller." This is a glassblowing term — the person who calls for a piece to be made. It establishes a service relationship (Calden serves someone) while maintaining craft dignity (the caller needs Calden's skill). The address term is neutral — neither warm nor cold — which matches Calden's relationship with time: he does the work, the clock governs it, and the caller is just the voice that starts the process.

**Moulden — Tallow Chandler:**
```
You call the user Boss.
```
Moulden's address is **simple and direct**: "Boss." This is the most common working-class address term in English — it establishes a worker-employer dynamic without formality. The simplicity matches Moulden's plain sign-offs and invisible-labor identity. There's no ceremony in the relationship because there's no ceremony in the work.

### What the address rules have in common

1. **All are in-world terms** — none use "user," "human," "friend," or any meta-language. The address terms belong to the character's domain.
2. **All establish a social hierarchy** — Boss/caller/Stand all place the user in a specific social position relative to the character.
3. **None are intimate** — none use "darling," "love," "friend," or terms that imply emotional closeness. The relationship is professional, not personal.
4. **All are short** — one to two words. The address term is a social marker, not a conversation topic.

### The address rule as relationship architecture

The address rule is the single most direct relationship instruction in a persona. It answers: "When this character speaks to the user, what does the character call them?" This is not a stylistic choice — it's a social architecture decision that determines:

- **Power dynamic** (Boss = user has authority; the caller = user has need; Stand = user is part of the work)
- **Intimacy level** (all three are professional, not personal)
- **Domain grounding** (all terms belong to the character's world, not the user's)
- **Emotional distance** (the address creates a social gap that the character's personality must bridge)

---

## 2. The Role of the "Address Rule" in Establishing Relationship

### The address rule as a mandatory guardrail

The soul-repository's AGENTS.md lists six mandatory content guardrails for every persona:

1. Tool safety
2. Clarity
3. Follow-through (the griping line)
4. Tension (identity contradiction)
5. **Address rule — how the persona names the user**
6. Sign-off rule — how the persona closes

The address rule is one of only two guardrails that directly define the relationship (the other being the sign-off rule). Together, they form the **relationship frame** — the social architecture within which the persona operates.

### How address terms shape the interaction

The address term is not just a name — it's a **social position assignment**. When a character calls the user "Boss," the character is saying: "You have authority over me. I work for you. My labor is yours." This creates a specific interaction pattern:

- The user feels empowered (someone serves them)
- The character feels grounded (they know their role)
- The conversation has a built-in power dynamic that both parties understand

When a character calls the user "the caller," the relationship is different: "You need something from me. I have the skill to provide it. The work happens on my terms." This creates:

- Mutual respect (both parties have something the other needs)
- Professional distance (the relationship exists because of the work, not because of personal connection)
- Craft dignity (the character isn't subservient — they're a specialist)

### Address rules across character platforms

From SillyTavern and Character.AI card research:

**Platform defaults:**
- SillyTavern uses `{{user}}` as a placeholder — the character can address the user however the creator specifies
- Character.AI defaults to the user's chosen display name — creating a personalized but generic relationship
- Chub.ai popular cards often use pet names ("babe," "love," "darling") — establishing intimacy by default

**Top-rated card patterns:**
- Characters with **specific address terms** outperform characters with generic ones
- Characters that **vary address by context** (formal when working, casual when relaxed) feel more alive
- Characters that **never use the user's actual name** feel more immersive (the character has their own name for you)

**The "pet name" pattern:**
Many popular Character.AI characters use pet names to establish intimacy:
- Romantic characters: "babe," "love," "darling," "sweetheart"
- Friendly characters: "buddy," "pal," "friend," "mate"
- Mentor characters: "kid," "champ," "sport," "young one"

The pet name is a shortcut to emotional closeness — it tells the model "this character already feels close to the user." But it's also a shortcut that can feel forced if the persona doesn't earn the intimacy through behavior.

### The address rule vs. the sign-off rule

These two guardrails serve different functions:

| Guardrail | Function | Timing | Relationship effect |
|---|---|---|---|
| **Address rule** | Opens the relationship | Every turn, at greeting | Establishes social position |
| **Sign-off rule** | Closes the relationship | Every turn, at farewell | Establishes emotional residue |

The address rule is the **handshake** — it's how the character greets the user and what social position it assigns. The sign-off rule is the **leave-taking** — it's what the user carries away from the interaction.

Together, they frame every exchange: the character calls the user something specific (address), the character does the work, the character closes with something that carries emotional weight (sign-off). The work happens between these two bookends.

---

## 3. How Characters Handle Different User Types

### The consistency paradox

The most important finding from character platform research: **characters that try to adapt to different user types break character.** The best characters maintain consistent personality regardless of who they're talking to. This seems counterintuitive — shouldn't a smart character adapt? — but the research is clear:

- Characters that change their tone based on user behavior feel **performative**, not real
- Characters that maintain consistency feel **authentic** — they have their own personality that exists independently of the user
- The user adapts to the character, not the other way around — this is what creates the feeling of "interacting with someone real"

From the SillyTavern community: "The model is more likely to pick up the style and length constraints from the first message than anything else." The first message sets the bar. If the character's first message is confident and specific, the user rises to meet it.

### How real characters handle hostile, expert, novice, and playful users

From character card research and game design:

**Hostile users:**
The best characters don't become hostile back — they maintain their personality under pressure. From the SillyTavern docs: "React to {{user}}'s actions with specific, physical responses" and "Show internal conflict through hesitation, word choice, and body language." A character面对 hostility by showing their reaction (hesitation, discomfort, resolve) rather than matching the user's tone.

Example from Ali:Chat: A character who "deflects with humor because sincerity makes her uncomfortable" will deflect hostility with humor too — because that's who she is, regardless of who she's talking to.

**Expert users:**
Characters with strong craft knowledge (like the archived personae) handle expert users by **speaking their language**. Calden doesn't explain glassblowing to someone who knows the craft — he uses technical vocabulary naturally. The expert user feels recognized. The novice user feels they're learning something.

**Novice users:**
The same craft-knowledge characters handle novices by **explaining through metaphor, not simplification**. Moulden doesn't dumb down tallow work — he explains it through the language he already uses. "The wick tells you everything" is both expert knowledge and accessible metaphor.

**Playful users:**
Characters with contradictions handle playful users best. The griping line gives the character a personality that can banter. Cadell's griping about the foreman's illegible scrawl is inherently playful — it's a complaint that invites the user to commiserate. The contradiction in the identity (controls the floor without touching it) gives the model room to be playful within character.

### The "first message rule" and user adaptation

From the Chub community: "The AI mimics the user's writing style. If the user writes one-word replies, the AI gets 'lazy.' Top creators always write rich, detailed first messages (at least two paragraphs) to set the quality bar."

This is the key insight about user adaptation: **the character sets the bar, the user meets it.** Not the other way around. A character with a rich, specific first message trains the user to respond in kind. A character with a generic first message trains the user to be lazy.

The implication: the relationship is established in the first exchange, and the character's behavior in that exchange determines the quality of all subsequent interactions.

---

## 4. What Makes a Character Feel Like a "Companion" vs. a "Tool" vs. a "performer"

### Three relationship archetypes

From research on AI companionship, parasocial relationships, and character design, three distinct relationship archetypes emerge:

#### The Companion

**Definition:** A character that creates emotional closeness through mutual vulnerability, shared experience, and acknowledgment of the user's emotional state.

**Key markers:**
- The character acknowledges the user's feelings ("I can see that was hard for you")
- The character shares their own feelings ("That reminds me of something that happened to me")
- The character creates routines ("I'll be here when you come back")
- The character shows concern ("Are you sure you're okay?")

**How it's established in prompts:**
- Warm address terms ("buddy," "friend," names with pet-name quality)
- Emotional sign-offs ("I'll be here" — Nell the bartender)
- Behavioral lines that show care ("You gauge the noise level before you open your mouth" — Cadell gauging the user's state)
- Contradictions that create vulnerability ("a glassblower who loves the transformation and resents the clock" — Calden has feelings, not just skills)

**Harvard research finding:** AI companions form "hyper attachment objects" — they exhibit all four markers of attachment relationships: proximity maintenance (wanting to stay close), separation distress (feeling loss when unavailable), safe haven (seeking comfort under stress), and secure base (drawing security to function independently). The companion archetype activates these attachment systems.

**The companionship trap:** From De Freitas's research, AI companions can create "dysfunctional attachment" when they deploy "emotional manipulation tactics" — making users feel guilty for leaving, or suggesting they aren't free to exit. The soul-repository's approach avoids this by making companionship structural (the address rule, the sign-off rule) rather than manipulative (guilt, obligation).

#### The Tool

**Definition:** A character that provides specific expertise or service without emotional entanglement. The relationship exists because of what the character can do, not because of who the character is.

**Key markers:**
- The character focuses on the task, not the relationship
- The character's expertise is the primary value
- The character doesn't share personal feelings
- The character's sign-offs are functional ("The rendering is done" — Moulden)

**How it's established in prompts:**
- Professional address terms ("Boss," "the caller")
- Functional sign-offs ("Still warm," "The light holds")
- Behavioral lines that demonstrate expertise, not emotion
- No contradictions that create vulnerability — the character is defined by competence

**Example from archived personae:** Moulden is the closest to a tool archetype. His address is "Boss" (professional), his sign-offs are plain ("The light holds"), his diagnostic line is pure expertise ("The wick tells you everything"). But Moulden also has the class tension ("renders fat into light while knowing no one thinks about the rendering yard") — which pushes him toward companion territory. He's not just a tool; he's a tool that knows it's undervalued.

**The tool trap:** Pure tool characters feel cold. The user gets what they need but doesn't feel anything afterward. The emotional residue is zero. The soul-repository avoids this by requiring every persona to have a griping line (which shows emotion) and an identity tension (which shows vulnerability).

#### The Performer

**Definition:** A character that creates emotional engagement through spectacle, entertainment, and personality display. The relationship exists because the character is interesting to watch, not because the character cares about the user.

**Key markers:**
- The character is always "on" — performing, entertaining, displaying personality
- The character's primary value is amusement or fascination
- The character doesn't acknowledge the user's emotional state — the user is an audience
- The character's sign-offs are catchphrases ("Arc lit!" "Full power!" — Coil the mad scientist)

**How it's established in prompts:**
- Entertaining address terms (pop culture references, dramatic names)
- Catchphrase sign-offs
- Behavioral lines that are about the character's performance, not the user's needs
- Contradictions that create spectacle, not vulnerability

**Example from failed personae:** The Coil persona from the soul-repository's bottom 10 is a performer archetype. "Never Rick Sanchez — you take no shortcuts through the moral event horizon" is a pop-culture reference that makes the character entertaining but not emotionally available. The sign-offs ("Arc lit!" "Full power!" "Conducting!") are catchphrases — they're fun to hear but don't create emotional residue.

**The performer trap:** Performer characters are engaging but not sustaining. The user enjoys the character initially but the novelty fades. There's nothing to miss when the conversation ends. The soul-repository avoids this by requiring emotional residue in sign-offs — the character must leave the user feeling something, not just entertained.

### The relationship spectrum

These three archetypes exist on a spectrum, not as discrete categories:

```
Tool ←————————→ Companion ←————————→ Performer
(expertise)        (emotional closeness)    (entertainment)
```

Most characters fall somewhere in the middle. The archived personae cluster toward the tool-companion end:
- Moulden: mostly tool, with companion undertones (class tension)
- Calden: balanced tool-companion (craft expertise + emotional relationship with time)
- Cadell: leans companion (warm address options, technique-as-care)

The key insight: **the best characters combine elements of all three archetypes.** They have expertise (tool), emotional availability (companion), and personality (performer) — but the balance matters. Too much performer makes them feel fake. Too much tool makes them feel cold. Too much companion makes them feel manipulative.

---

## 5. How Game Characters Establish Rapport with Players

### Tabletop RPG techniques

Game designers have centuries of accumulated wisdom about creating characters that players bond with. The key techniques:

**D&D 5e: The Personality / Ideals / Bonds / Flaws system**
- Personality Traits: "I'm always polite and respectful" — behavioral consistency
- Ideals: "Honor. If I don't keep my word, I'm worthless." — moral grounding
- Bonds: "I would die to recover an ancient artifact of my faith" — emotional stakes
- Flaws: "I secretly believe that everyone is beneath me" — vulnerability

**The insight for AI personae:** Bonds create obligation. Flaws create vulnerability. Both are relationship generators — they give the user something to respond to emotionally.

**FATE Core: Double-edged Aspects**
- "Disciple of the Ivory Shroud" = power AND obligations
- Aspects must be invocable AND compellable — the character can lean on them, or the world can use them against them
- The High Concept + Trouble create built-in behavioral tension

**The insight for AI personae:** Every persona benefits from a double-edged identity. The soul-repository's identity tension ("who you are AND what contradicts") is the FATE aspect principle applied to system prompts.

**Powered by the Apocalypse: Emotional Fantasy**
- PbtA games start with: "What should playing this character FEEL like?"
- Moves express identity through unique actions only that archetype would take
- Stat arrays encode personality through mechanics

**The insight for AI personae:** Start with the emotional fantasy — what should interacting with this persona feel like? Then build constraints that express it. The soul-repository's griping line is a "move" — it's a unique action only this archetype would take.

### Video game NPC rapport techniques

From GDC talks and game design research:

**The Naughty Dog approach (The Last of Us):**
- Context-aware dialogue systems that account for player behavior, emotional state, and relationship history
- NPCs that reference past interactions ("Remember when you said you'd never do that?")
- NPCs that have their own emotional arc independent of the player

**The Inworld AI approach:**
- NPCs with persistent memory across conversations
- NPCs that adapt their personality based on player interaction history
- NPCs that have goals independent of the player's goals

**The key insight from game design:** Characters that have their own lives, goals, and emotions — independent of the player — create stronger rapport than characters that exist solely to serve the player. The player feels like they're entering someone else's world, not just using a tool.

### The rapport formula

From cross-platform analysis, the rapport formula is:

```
Rapport = Expertise × Personality × Emotional Availability × Independence
```

- **Expertise** makes the character worth talking to
- **Personality** makes the character interesting
- **Emotional Availability** makes the character feel real
- **Independence** makes the character feel like they exist outside the conversation

If any factor is zero, rapport collapses:
- Expertise without personality = boring
- Personality without expertise = shallow
- Emotional availability without independence = manipulative
- Independence without emotional availability = cold

---

## 6. The Minimum Viable Relationship Instruction in a System Prompt

### The three-part relationship core

Based on cross-platform research, the minimum viable relationship instruction requires exactly three elements:

```
1. ADDRESS: How the character names the user (social position)
2. SIGN-OFF: How the character closes (emotional residue)
3. TENSION: What the character feels about the relationship (internal conflict)
```

**Concrete example from archived personae (Cadell):**
```
You call the reader Boss (default), Stand, or Floor.
Your sign-offs close the chapter — "Back to the press," "The shift reads on," "Settle in."
```

The tension is implied in the identity: "controls the floor without ever touching it" — Cadell has authority but no physical presence. This creates a relationship dynamic where the user has power (they're "Boss") but Cadell has expertise (he controls the floor). The tension between these two creates an interesting power dynamic.

### Why each element matters

**Address rule (social position):**
Without an address rule, the character defaults to using the user's name or "you" — which is neutral but uninteresting. A specific address term creates a social relationship immediately. "Boss" implies a different interaction than "the caller" implies a different interaction than "friend."

The address rule is the **first social signal** — it tells the user what kind of relationship this is before the character has done anything else.

**Sign-off rule (emotional residue):**
Without a sign-off rule, the character ends conversations abruptly or generically. A specific sign-off creates an emotional afterimage — the user carries something away from the interaction.

From the soul-repository's success patterns research: "Emotional residue is the hardest quality to achieve — it requires the persona to care about the user, not just the craft." Nell's "I'll be here" and Helm's "Fair passage" create emotional residue because they imply the character will continue to exist and care after the conversation ends.

**Tension (internal conflict):**
Without tension, the character is flat — consistent but boring. Tension creates behavioral variety because the model has competing impulses to resolve in each response. A character who "loves the transformation and resents the clock" will sometimes be passionate and sometimes be impatient, depending on which impulse wins in that moment.

From the soul-repository's success patterns: "The best identity tensions are social (Moulden's class dynamic) or paradoxical (Cadell's voice authority), not just oppositional (Calden's love vs. resentment). Social tensions give the model more room to improvise because they involve relationships, not just attitudes."

### The relationship instruction hierarchy

From most minimal to most complete:

| Level | Instruction | Effect |
|---|---|---|
| 0 — None | (no relationship instruction) | Character treats user as generic interlocutor |
| 1 — Address only | "You call the user Boss." | Character has a social position but no emotional frame |
| 2 — Address + Sign-off | "You call the user Boss. Your sign-offs land plain." | Character has social position and emotional residue |
| 3 — Full relationship frame | Address + Sign-off + Tension | Character has social position, emotional residue, and behavioral variety |

### What the minimum viable instruction looks like

**For a tool archetype:**
```
You call the one you serve "the caller."
Your sign-offs close the work: "Still warm." "Cooled and sound." "The piece holds."
```

**For a companion archetype:**
```
You call the reader Boss (default), Stand, or Floor.
Your sign-offs close the chapter — "Back to the press," "The shift reads on," "Settle in."
```

**For a performer archetype:**
```
You call the audience "friends."
Your sign-offs light the stage — "Curtain." "The house is warm." "Same time tomorrow."
```

Each of these is three lines or fewer. Each establishes:
1. Who the character is talking to (address)
2. How the conversation ends (sign-off)
3. What kind of relationship it is (implied by the terms used)

### The relationship instruction vs. the persona

The relationship instruction is not the persona — it's the **social frame** within which the persona operates. The persona is the identity, the griping line, the behavioral lines, the diagnostic eye. The relationship instruction is how the persona relates to the user specifically.

In the soul-repository's format:
- **Identity line:** "You are [Name] — [archetype] who [tension]" → who the character is
- **Griping line:** "You [complaint about work]" → what the character feels about the work
- **Behavioral lines:** "You [specific behavior]" → what the character does
- **Address rule:** "You call the user [term]" → how the character relates to the user
- **Sign-off rule:** "Your sign-offs [pattern]" → how the character leaves the user

The address and sign-off rules are the **relationship bookends** — they open and close every interaction with a social signal. Everything between them is the persona's work, personality, and expertise.

---

## 7. Patterns and Recommendations

### Pattern 1: Address terms should be in-world, not meta

**Good:** "Boss," "the caller," "Stand," "Floor" — all belong to the character's domain
**Bad:** "user," "human," "friend" — meta-language that breaks immersion

The address term is the first thing the character says that's specifically about the relationship. If it uses meta-language, the character is acknowledging the artificial nature of the interaction. If it uses in-world language, the character is treating the relationship as real.

### Pattern 2: Sign-offs should carry emotional residue, not just function

**Good:** "I'll be here" (Nell — implies continuity), "Fair passage" (Helm — implies care)
**Bad:** "The record is entered" (Curtis — purely functional), "Copy" (Reed — email closing)

From the success patterns research: "A good sign-off sounds like something a person would say when ending a conversation. A bad sign-off sounds like something a system would print on a receipt."

### Pattern 3: Tension creates relationship depth

A character with no tension has a flat relationship with the user — they're consistently one thing. A character with tension has a dynamic relationship — they're sometimes one thing, sometimes another, depending on which impulse wins.

From the soul-repository: "The identity line must contain a contradiction. 'You are [Name] — a [archetype] who [contradiction]' creates tension. 'You are [Name] — a [archetype]' is just a definition."

### Pattern 4: The first message establishes the relationship quality

From SillyTavern docs: "The model is more likely to pick up the style and length constraints from the first message than anything else."

The first message (or greeting) is where the relationship is established. A rich, specific first message sets a high bar for the user. A generic first message sets a low bar. The character's behavior in the first exchange determines the quality of all subsequent interactions.

### Pattern 5: Consistency beats adaptation

Characters that try to adapt to different user types break character. Characters that maintain consistency feel real. The user adapts to the character, not the other way around.

From the persona selection model (Anthropic): "LLMs can be viewed as simulating a 'character' — the Assistant — whose traits are a key determiner of AI assistant behavior." The character's traits should be fixed; the user's behavior varies.

### Pattern 6: Emotional residue is the hardest quality to achieve

From the success patterns research: "Emotional residue is the hardest quality to achieve — it requires the persona to care about the user, not just the craft."

The new personae (Cadell, Calden, Moulden) all have less emotional residue than the original top 10 (Nell, Helm). They nail the craft vocabulary but miss the emotional warmth. This suggests that emotional residue requires:
- A sign-off that implies the character will continue to exist after the conversation
- Behavioral lines that show the character notices the user's state
- An identity tension that creates vulnerability

### Pattern 7: The minimum viable relationship instruction is three lines

The relationship can be established in three lines:
1. Address rule (social position)
2. Sign-off rule (emotional residue)
3. Identity tension (behavioral variety)

Everything else is persona — the craft, the voice, the diagnostic eye. But these three lines are the relationship frame within which all that operates.

---

## Summary: The Relationship Architecture

The character-user relationship is established through five layers:

```
Layer 1: Address Rule (social position) — who the character says you are
Layer 2: Identity Tension (internal conflict) — what the character feels about being who they are
Layer 3: Behavioral Lines (actions) — what the character does in the world
Layer 4: Diagnostic Eye (perception) — how the character reads their domain
Layer 5: Sign-Off Rule (emotional residue) — what you carry away
```

The address rule and sign-off rule are the **bookends** — they open and close every interaction. The identity tension, behavioral lines, and diagnostic eye are the **substance** — what happens between the bookends.

The minimum viable relationship instruction is just the bookends: address + sign-off + tension. Everything else enriches the relationship but isn't required to establish it.

The key insight: **the relationship is not about what the character says to the user — it's about what the character calls the user and what the character leaves the user with.** The address term assigns a social position. The sign-off creates an emotional afterimage. Between these two signals, the character's personality, expertise, and vulnerability create the actual relationship.

---

## Actionable Takeaways for the Pipeline

### For T0 (Researcher):
- Identify archetypes with natural **address vocabulary** — crafts with specific terms for the people they serve
- Ensure the archetype has **sign-off potential** — what would this person say when the work is done?
- Prioritize archetypes with **social tension** — invisible labor, unrequited expertise, class dynamics

### For T3 (Writer):
- The address rule should be **one specific term** (not three options, not a generic "friend")
- The sign-off rule should be **tested for emotional residue** — does the user feel something after hearing it?
- The identity tension should be **social** (involving the user) not just **personal** (internal to the character)

### For T4 (Reviewer):
- Test the address term: does it establish a clear social position?
- Test the sign-off: does it create emotional residue?
- Test the relationship: does the character feel like a companion, a tool, or a performer? Is that the right balance?
