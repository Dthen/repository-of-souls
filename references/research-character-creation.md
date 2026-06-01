1|# Research: Character Creation Methodology for AI Persona Design
2|
3|**Purpose:** Inform the soul-repository pipeline's positive craft guidance — what makes a good character, not just what makes a bad one.
4|**Date:** 2026-05-31
5|
6|---
7|
8|## 1. Professional Character Design Frameworks
9|
10|### 1.1 Want / Need / Flaw (Screenwriting & Fiction)
11|
12|The most widely used character architecture across fiction, screenwriting, and game design. Three distinct concepts:
13|
14|- **Want** (external goal): What the character pursues actively. It's observable, concrete, and drives plot. A detective wants to solve the case. A chef wants the Michelin star.
15|- **Need** (internal gap): What the character actually requires to grow or succeed — but doesn't know it yet. Often the opposite of the want, or orthogonal to it. The detective needs to forgive himself. The chef needs to accept imperfection.
16|- **Flaw** (the wound): The specific trait or belief that prevents the character from seeing the need. It's not a random weakness — it's the *mechanism* of blindness. Pride, fear of abandonment, rigid ideology.
17|
18|**Key insight for AI personae:** A persona doesn't need a plot arc, but it benefits from the *tension* between what it wants to do (its purpose) and what makes that hard (its flaw or limitation). A persona that wants to be helpful but is constitutionally blunt has built-in voice. A persona that wants precision but must communicate with beginners has natural friction.
19|
20|**The Want-Need gap creates behavior.** When a character's want conflicts with their need, they make interesting choices. When an AI persona's purpose conflicts with its temperament, it generates interesting responses.
21|
22|### 1.2 FATE Core Aspects (RPG Design)
23|
24|FATE's character system is the gold standard for *economy of character expression*. Each character is defined by ~5 short phrases called **aspects**, and every aspect must be:
25|
26|- **Double-edged:** It helps you AND hurts you. "Disciple of the Ivory Shroud" gives you power AND obligations. "Infamous Girl with Sword" gives you reputation AND enemies.
27|- **Invocable AND Compellable:** You can lean on it for strength, or the world can use it against you.
28|- **Evocative, not descriptive:** "Wizard for Hire" is better than "Arcane practitioner who accepts monetary compensation for services."
29|- **Never boring:** An aspect that only activates in safe situations is wasted space.
30|
31|**The High Concept** — a one-line summary of who the character is and what they do — is the closest analog to a persona's identity line. FATE's advice: think of it as "your job, your role in life, or your calling — it's what you're good at, but it's also a duty you have to deal with."
32|
33|**The Trouble** — what complicates the character's existence — maps directly to the tension/contradiction that makes personae interesting. Two types:
34|1. **Personal struggles:** Dark sides, hard-to-control impulses ("Anger Management Issues")
35|2. **Problematic relationships:** People or organizations that create friction ("The Scar Triad Wants Me Dead")
36|
37|**Key insight for AI personae:** Every persona should have something like an aspect — a short phrase that's simultaneously a strength and a complication. The FATE test: "Can this phrase both help me succeed AND get me into trouble?" If yes, it's a good aspect. If a persona's identity line only enables and never constrains, it's flat.
38|
39|### 1.3 PbtA Playbooks (Tabletop RPG Design)
40|
41|Powered by the Apocalypse games use **playbooks** — character archetypes defined by:
42|
43|- **A thematic hook:** Not just "what you do" but "what story you're in." The Chosen isn't just a fighter — they're someone *destined* for something. The Mundane isn't just weak — they're the normal person in a supernatural world.
44|- **Moves that express identity:** Each playbook gets unique actions that only *that kind of character* would take. The Spooky has moves about their dark past. The Professional has moves about bureaucracy and protocol.
45|- **Stat arrays that encode personality:** In Apocalypse World, the Hardcase has high Hard (aggression) and low Hot (charisma). Stats are personality, not just mechanics.
46|
47|**Jay Dragon's playbook design approach (from Possum Creek Games):**
48|1. Start with the **emotional fantasy** — what does playing this character *feel like*?
49|2. Define the **unique angle** — what does this playbook see that others don't?
50|3. Build moves that **express** the fantasy, not just enable it
51|4. Leave room for **player interpretation** — the playbook is a seed, not a cage
52|
53|**Key insight for AI personae:** A persona is essentially a playbook — it defines which "moves" (response patterns, tones, approaches) belong to this character. The PbtA lesson: start with the emotional fantasy (what does *interacting with this persona feel like*?), then build constraints that express it.
54|
55|### 1.4 D&D 5e Personality Traits / Ideals / Bonds / Flaws
56|
57|D&D's system is the simplest framework:
58|
59|- **Personality Traits:** Two specific behavioral patterns ("I'm always polite and respectful")
60|- **Ideals:** The core principle ("Honor. I don't steal from others")
61|- **Bonds:** What connects you to the world ("I protect those who cannot protect themselves")
62|- **Flaws:** The specific weakness ("I judge others harshly, and myself even more harshly")
63|
64|**Key insight for AI personae:** The four-category structure maps almost directly to persona components: Traits (behavioral lines), Ideals (identity/purpose), Bonds (address rule, relationship to user), Flaws (Nevers, limitations). The D&D system shows you can create a compelling character with just 4 short statements — each one doing a different job.
65|
66|---
67|
68|## 2. What Makes a Character Feel Alive vs. Flat
69|
70|### 2.1 The Contradiction Principle
71|
72|> "Real people have contradictions. When a character feels like a real person, we recognize our own internal contradictions in them."
73|
74|Characters feel alive when they contain **productive contradictions** — not logical impossibilities, but tensions that mirror how real people work:
75|
76|- The generous person who is stingy with their time
77|- The fearless warrior who is terrified of emotional vulnerability
78|- The meticulous planner who is chaotic in their personal life
79|- The cynic who keeps doing kind things
80|
81|**Flat characters are consistent.** They always react the same way. They have one note. The villain is always cruel. The hero is always brave. Consistency feels mechanical.
82|
83|**Alive characters are *mostly* consistent — with one or two productive inconsistencies** that create surprise. The gruff mentor who occasionally says something devastatingly tender. The cheerful optimist who goes quiet at a specific trigger.
84|
85|**For AI personae:** A persona that *always* complains is flat. A persona that complains about everything except this one thing they genuinely love — that's alive. Build in one point of softness, one place where the character breaks their own pattern.
86|
87|### 2.2 Tension as Engine
88|
89|Tension isn't just plot conflict — it's the state of *two things being true at once*:
90|
91|- **Internal tension:** "I want to help, but I don't trust myself to not overstep"
92|- **Relational tension:** "I respect your autonomy, but I can see the mistake coming"
93|- **Tonal tension:** Formal language masking deep affection. Casual language masking sharp intelligence.
94|
95|The best character voices live in the **gap between what they say and what they mean**, or between **how they sound and what they do**. A persona that sounds grumpy but delivers excellent work is more interesting than one that sounds eager and delivers excellent work.
96|
97|**K.M. Weiland's insight:** The first thing people notice about a character is their **stance** — how they orient toward the world:
98|- **Aggressive:** Forward-leaning, future-focused, action-oriented
99|- **Withdrawn:** Backward-leaning, past-focused, reflective
100|- **Dependent:** Laterally-oriented, present-focused, relationship-seeking
101|
102|A persona's stance determines not just *what* it says but *when* and *to whom* it speaks up.
103|
104|### 2.3 The "First Thing People Notice" Test
105|
106|From K.M. Weiland's voice framework: **"What is the first thing people notice about this character?"** If you can't answer this in one phrase, the character lacks a hook.
107|
108|Good answers: "They never stop moving." "They look through you, not at you." "They smell like old books." "They laugh before they speak."
109|
110|For AI personae: What's the first thing a user notices? If every persona's first impression is "helpful and articulate," they're all the same character. The first impression should be *specific* and *slightly surprising*.
111|
112|---
113|
114|## 3. How Voice Emerges from Constraint
115|
116|### 3.1 The Constraint-First Theory of Voice
117|
118|Voice doesn't emerge from freedom — it emerges from **what you can't do**. A character who can say anything has no voice. A character who can only say things *a certain way* has a powerful one.
119|
120|Constraints that generate voice:
121|
122|| Constraint Type | Example | Voice Effect |
123||---|---|---|
124|| **Economy** | "Uses 5 words where others use 15" | Terse, precise, implies more than states |
125|| **Domain** | "Can only explain things through cooking metaphors" | Warm, sensory, grounded |
126|| **Register** | "Formal vocabulary, broken syntax" | Intelligent but unsettled, possibly foreign |
127|| **Tempo** | "Short sentences. Always. Even when the thought is complex." | Controlled, deliberate, slightly aggressive |
128|| **Vocabulary ceiling** | "Never uses a word longer than 3 syllables" | Direct, plain-spoken, trustworthy |
129|| **Metaphor source** | "Everything is an ocean — storms, tides, depths, currents" | Sweeping, emotional, prone to drama |
130|
131|### 3.2 Domain as Voice Generator
132|
133|A character's **domain of expertise** doesn't just give them knowledge — it gives them a **metaphor family** (Matt Bird's term from *Secrets of Story*). The aspect of a character's life that determines which metaphors, curses, and exclamations they use.
134|
135|- A chef doesn't just cook — they *season* their language, find things *half-baked*, call ideas *raw*
136|- A sailor doesn't just sail — they navigate conversations, weather storms, find things shipshape
137|- A telegrapher doesn't just send messages — they keep things *clear of noise*, find the *signal*, *key* things in
138|
139|**The metaphor family is the most efficient voice-building tool.** It generates hundreds of micro-distinctions from a single source. If you know the domain, you know the voice — because the domain constrains which words are available.
140|
141|### 3.3 The Five Voice Tools (K.M. Weiland)
142|
143|1. **Dialogue tics:** A favored word, a favored volume, a preferred word count
144|2. **Personalized slang/swears:** Words that belong only to this character
145|3. **Metaphor families:** The source domain for all comparisons and exclamations
146|4. **Catchphrases:** Memorable but easily overdone — use sparingly
147|5. **Rhythms and phrasings:** The most powerful tool — not *what* words, but *how they're strung together*
148|
149|**For AI personae:** The 100-200 word SOUL.md format means you can't deploy all five tools. Prioritize:
150|- **Rhythm** (sentence structure patterns)
151|- **Metaphor family** (one source domain)
152|- **One dialogue tic** (a word they favor or avoid)
153|
154|### 3.4 The "Could Appear in Any Persona" Test
155|
156|> "If a line could appear in any persona with only the domain noun swapped, it is a copy, not a voice."
157|
158|"You reach for every tool available" works for a glassblower, an apothecary, and a harbour pilot — which means it belongs to none of them. True voice requires sentence structures that are *architecturally* different, not just *decoratively* different.
159|
160|**Test:** Replace the domain-specific nouns with placeholders. If the sentence still works for any archetype, it's not voice — it's a template.
161|
162|---
163|
164|## 4. Naming Conventions in Fiction
165|
166|### 4.1 Names as Immediate Characterization
167|
168|> "A name is more than just something to call your character. It's part of a person's identity, part of their family and home. It can impact tone, convey history." — Alison Stine, Literary Hub
169|
170|Names are the **first piece of information** a reader encounters. They create snap judgments before any action or dialogue.
171|
172|### 4.2 Sound Symbolism and Phonetics
173|
174|Names carry **musical qualities** that evoke feelings:
175|- **Warmth/softness:** Vowels, nasals (m, n), liquids (l, r) — "Mila," "Lena," "Noah"
176|- **Hardness/authority:** Plosives (k, t, p, b), fricatives — "Katrina," "Brutus," "Victoria"
177|- **Mystery/otherness:** Unusual combinations, unfamiliar phonemes — "Xalith," "Zird," "Cynere"
178|
179|### 4.3 Naming Strategies from Professional Writers
180|
181|| Strategy | Example | Effect |
182||---|---|---|
183|| **Obituaries/graveyards** | Agatha Christie's method | Authentic, period-appropriate |
184|| **Thematic naming** | *Trashlands*: all characters named after things lost to climate change (Coral, Trillium, Miami) | Worldbuilding through names |
185|| **Final girl naming** | Short, androgynous names (Jess, Sid, Wil) | Genre-aware, signals archetype |
186|| **Formal/informal contrast** | Edmund "Bunny" (*A Secret History*) | Shows dual nature |
187|| **Name-matches-personality** | Antoinette Conway (prickly name, prickly character) | Reinforces trait |
188|| **Ordinary-for-extraordinary** | Kin Stewart (time-traveling IT dad) | Creates ironic contrast |
189|| **Cultural signaling** | Tarisai (West African inspiration), Sarabeth (religious/regional) | Instantly locates character |
190|| **Mashup** | "Wizard Private Eye," "Monster-slaying Accountant" | Genre-bending, attention-grabbing |
191|| **Relationship naming** | "Black Sheep of the Thompson Family" | Instant social context |
192|
193|### 4.4 Naming Rules of Thumb
194|
195|1. **Avoid same-initial characters** in the same context — readers confuse them
196|2. **Match tone to genre** — a noir detective shouldn't be named "Bubbles"
197|3. **A nickname reveals relationship** — who calls them what, and why
198|4. **Unfamiliarity signals otherness** — unusual spellings or phonemes mark a character as from *somewhere else*
199|5. **An unnamed character is a choice** that draws attention — be intentional
200|
201|### 4.5 For AI Personae
202|
203|Personae names should:
204|- Be **memorable on first encounter** (users will see this name repeatedly)
205|- **Sound like what the character is** — phonetically match the archetype's register
206|- Be **distinct from other personae** in the repository (no two names should share first letter, similar rhythm, or similar register)
207|- **Work as a form of address** — users will say/write this name, so it should be comfortable to use
208|- Carry **implied worldbuilding** — "Brendan the Wizen" tells you something about the character before any description
209|
210|---
211|
212|## 5. Actionable Insights for the AI Persona Pipeline
213|
214|### 5.1 For T1 Researcher (Seed Generation)
215|
216|**Instead of:** Collecting domain facts and behavioral constraints.
217|**Also collect:**
218|- The **emotional fantasy** of the archetype — what does interacting with this persona *feel like*?
219|- The **metaphor family** — what domain vocabulary generates the character's comparisons?
220|- The **productive contradiction** — what two truths about this character are in tension?
221|- The **first impression** — what does a user notice in the first exchange?
222|- The **stance** — aggressive (forward), withdrawn (backward), or dependent (lateral)?
223|
224|### 5.2 For T2 Namer (Naming)
225|
226|**Instead of:** Avoiding bad names (collision, misdirection, borrowed).
227|**Also pursue:**
228|- Names that **sound like the archetype** (phonetic matching)
229|- Names that **work as address** (comfortable to say repeatedly)
230|- Names that **imply worldbuilding** (the name tells a micro-story)
231|- Names with **distinct rhythm** from existing personae
232|
233|### 5.3 For T2 Writer (Drafting)
234|
235|**Instead of:** Avoiding negative patterns (Don't copy, Don't exceed word count).
236|**Also build:**
237|- A **metaphor family** from the archetype's domain (one source for all comparisons)
238|- A **sentence rhythm** that's architecturally distinct (not just decoratively different)
239|- One **productive contradiction** — a place where the character breaks their own pattern
240|- A **first-impression hook** — the first 1-2 lines should be the thing users notice
241|- **Double-edged aspects** — identity lines that both enable and constrain
242|
243|### 5.4 For T3 Reviewer (Critique)
244|
245|**Instead of:** Checking for format violations and negative patterns.
246|**Also test:**
247|- **The "any persona" test:** Replace domain nouns with placeholders. Does the voice still work? If yes, it's a template, not a voice.
248|- **The contradiction test:** Is there a productive tension? Does the character have a place where they break their own pattern?
249|- **The first-impression test:** What does the user notice first? Is it specific and surprising?
250|- **The metaphor-family test:** Is there a coherent source domain? Do all comparisons come from the same world?
251|- **The aspect test:** Could each major line both help AND hurt? Is it double-edged?
252|
253|### 5.5 For T4 Refiner and T5 Final Reviewer
254|
255|**Final quality gates (positive, not just negative):**
256|1. The persona has a **clear emotional fantasy** — you can describe what interacting with it *feels like* in one phrase
257|2. The persona has **one productive contradiction** — a place where two truths are in tension
258|3. The persona has a **distinct sentence rhythm** — the structure itself signals the character
259|4. The persona has a **coherent metaphor family** — comparisons come from one source domain
260|5. The persona has a **first-impression hook** — something specific and slightly surprising
261|6. The persona's **name sounds like what it is** — phonetically appropriate, memorable, distinct
262|
263|---
264|
265|## 6. Summary: The Anatomy of a Good Persona
266|
267|A compelling AI persona in ~150 words needs:
268|
269|| Element | What It Does | Source Framework |
270||---|---|---|
271|| **Identity** (High Concept) | Says who you are and what you do | FATE |
272|| **Contradiction** (Trouble) | Creates productive tension | FATE, fiction craft |
273|| **Metaphor family** (Domain) | Generates voice from constraint | Matt Bird, K.M. Weiland |
274|| **Sentence rhythm** (Voice) | Makes the character recognizable without tags | Weiland, craft essays |
275|| **Stance** (Orientation) | Determines when and how they speak | Enneagram/Weiland |
276|| **First impression** (Hook) | What users notice immediately | Character craft |
277|| **Flaw** (Limitation) | The specific mechanism of limitation | Want/Need/Flaw |
278|| **Behavioral lines** (Moves) | What this persona does that others don't | PbtA playbooks |
279|| **Nevers** (Trouble/Compulsion) | The constraints that generate voice | FATE aspects |
280|| **Address rule** (Bond) | How it relates to the user | D&D Bonds |
281|| **Sign-off** (Closing) | How it exits — its last impression | Character craft |
282|
283|---
284|
285|## Sources
286|
287|- FATE Core SRD: https://fate-srd.com/fate-core/your-character-idea
288|- K.M. Weiland, "Top 14 Tips and Tools for Creating Unique Character Voices": https://www.helpingwritersbecomeauthors.com/character-voices/
289|- Alison Stine, "How Should You Name Your Characters?" (Literary Hub): https://lithub.com/how-should-you-name-your-characters/
290|- September C. Fawkes, "Character's Want vs. Need (Explained 4 Different Ways)": https://www.septembercfawkes.com/2021/02/characters-want-vs-need-explained-4.html
291|- Matt Bird, *Secrets of Story* (metaphor families concept)
292|- Jay Dragon, "Writing Playbooks: An Approach" (Possum Creek Games)
293|- D&D 5e Basic Rules, Chapter 4: Personality and Background
294|- C.S. Lakin, "Using Contradictions to Create Masterful Microtension": https://www.livewritethrive.com/2026/02/16/using-contradictions-to-create-masterful-microtension-part-2/
295|