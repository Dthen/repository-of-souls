# Research: Perceptual Lens

**How characters filter and interpret the world through their domain — what they NOTICE, what they IGNORE, and how they INTERPRET new situations.**

**Date:** 2026-06-02

---

## 1. The Perceptual Lens vs. the Perception Filter

These are related but distinct concepts. Understanding the difference matters for prompt design.

A **perception filter** is a selective attention mechanism: given a scene, the character notices certain details and misses others. The filter determines *what enters awareness*. It's about selection from a fixed scene.

A **perceptual lens** is something deeper: the character doesn't just select different details — they *organize reality differently*. The same scene isn't just filtered differently; it's *constituted* differently. The tallow chandler doesn't see a room and then notice the candles. The tallow chandler walks into a room and the candles *are* the room. Everything else is background.

The distinction matters because:
- A perception filter can be described as a list: "notices exits, ignores decorations."
- A perceptual lens must be described as a worldview: "interprets every space through the materials it's made of and the labor that built it."

Most prompt engineering stops at perception filters. The perceptual lens goes further — it changes what the character *cares about*, not just what they *notice*.

---

## 2. How Fiction Writers Establish Worldview Through Attention

### 2.1 Focalization: Who Sees Determines What Exists

Narrative theory gives us the precise term: **focalization**. Gérard Genette distinguished *who speaks* (voice) from *who sees* (focalization). "The focalization model rests on a critical distinction. Narrative voice is the source of discourse (the teller). Focalization, on the other hand, is the lens through which the story is perceived (the seer)" (Bookish Bay).

Two characters entering the same room produce two different rooms — not because the room changed, but because the focalizer changed. The room a chef enters smells different from the room a firefighter enters. The chef notices: leftover grease on the range hood, the ventilation angle, whether the gas line is copper or flex. The firefighter notices: exits, load-bearing structure, the smell of something electrical behind the wall. Same room. Different realities.

**The craft implication:** You don't describe a room and then say "the character noticed X." You describe what the character's focalization *constructs* as the room. The character's expertise doesn't add information to a neutral description — it *replaces* the description.

### 2.2 Interiority: The Mechanics of Seeing

Interiority is the inner world of a character on the page — their subjective experience. The craft literature breaks it into three components that together form the perceptual lens:

**Assumptions:** How they fill gaps in knowledge. "When you have something suspicious or surprising happen, you can insert what the character's assumptions are about it" (Liz Verity). An assumption is always colored by the character's worldview. The tallow chandler who sees a smoky room assumes someone rushed the rendering. The architect who sees a smoky room assumes faulty HVAC.

**Judgments:** How biased opinions lead to conclusions. "Judgments are how a character's biased opinions lead to conclusions... Put judgments in your story by taking the character's biases and having her judge what happens around her in that light" (Liz Verity). The difference between an observation and a judgment reveals the lens. "The candle is three inches long" is an observation. "The candle is barely past the third dip — they're burning through stock" is a judgment filtered through a chandler's expertise.

**Evaluations:** How they interpret facts and assess worth. Different from assumptions (guesses about unknown facts) and judgments (opinions about right/wrong) — evaluations are about *significance*. What matters and what doesn't. The tallow chandler evaluates a letter by the quality of the seal wax, the evenness of the wick in the candle next to it, whether the desk has ring marks from wet tumblers left standing. The letter's content? That's someone else's department.

### 2.3 The Attention Hierarchy

The most important technique for making a perceptual lens work is establishing an **attention hierarchy**: what the character notices *first*, what they notice *second*, and what they *never notice at all*.

**The Novice:** Sees everything. Overwhelmed. Defaults to bottom-up processing — raw sensory data, no organizing framework. "There's a building. It's tall. It's gray."

**The Intermediate:** Begins to pattern-match. Sees familiar structures. Starts ignoring irrelevant details. "That's a brutalist tower — looks like government housing from the '70s."

**The Expert:** Sees through the surface. Instantly reads deeper structures. Misses obvious things the novice would catch. "Notice the load-bearing walls — someone's been renovating. See that crack pattern? Foundation shift."

**The critical insight for character writing:** The expert doesn't just know more — they see *differently*. Their attention is automatically drawn to different features. They notice what the novice misses, and they miss what the novice notices. This asymmetry is the engine of interesting perception.

The perceptual lens is the expert's hierarchy made permanent and involuntary. The tallow chandler doesn't *decide* to look at the candles in a room. Their eyes go there the way yours go to a face in a crowd. It's not a choice. It's who they are.

---

## 3. How Expertise, Trauma, and Values Shape Perception

### 3.1 The Expertise Gradient

Expertise doesn't just add knowledge — it restructures perception itself. A study from University College London and Bangor University found that "spatial professionals" — artists and architects — "see the world through a different and more elaborate lens than others" (StudyFinds). The differences went beyond vocabulary — they reflected fundamentally different ways of organizing visual information.

Architects referred to the "end" of an area; painters called the same location the "back." The differences weren't linguistic — they were perceptual. The same space was *experienced* differently because the professionals' expertise had restructured how they processed visual information.

**"Our study has provided evidence that your career may well change the way you think... people of different professions differ in how they appreciate the world"** (Dr. Hugo Spiers, UCL).

This is the scientific basis for the perceptual lens: expertise doesn't just inform — it *constitutes* experience.

### 3.2 Trauma as a Forced Lens

Trauma creates its own kind of expertise — a hyper-tuned pattern recognition for danger. The combat veteran notices exits, calculates sight lines, reads body language for threat cues. The survivor of abuse reads microexpressions, tone shifts, and power dynamics that others don't register.

The difference between expertise-based and trauma-based lenses:

- **Expertise lens:** "I notice this because I know what to look for" (expansive, enriching)
- **Trauma lens:** "I notice this because I can't not see it" (contractive, hypervigilant)

Both are automatic. Both are invisible to the character operating them. Both produce distinctive, compelling narration when rendered on the page.

The trauma lens is particularly interesting for prompt design because it creates a character who *doesn't want* to see what they see. The expertise lens is pleasurable — the tallow chandler enjoys reading the room through candles. The trauma lens is compulsive and unwanted. This creates immediate interiority: the gap between what the character sees and what they wish they could see.

### 3.3 Values as a Selection Engine

Values determine not what you *can* see but what you *choose* to see — or rather, what you can't *stop* seeing. A character who values honesty reads every interaction for deception. A character who values craft reads every object for quality of making.

Values are the most subtle component of the perceptual lens because they're often invisible to the character. The tallow chandler doesn't think "I value good rendering." They just feel *irritated* when they see a poorly made candle. The irritation *is* the value, expressed as perception. The value doesn't announce itself — it manifests as a reaction.

**Prompt design implication:** Don't tell the model "you value X." Instead, describe the emotional reaction that X produces. "When you see a poorly dressed candle, something tightens in your chest. You don't have an opinion about it — you have a *feeling*."

---

## 4. APPLIES Knowledge vs. SEES THE WORLD Through It

This is the central distinction for prompt design. The difference between a boring character and an interesting one.

### 4.1 The Boring Version: Applying Domain Knowledge

A character who APPLIES domain knowledge treats their expertise as a tool they pick up and put down. They walk into a room, and then they *decide* to analyze it through their domain. The perceptual lens is conscious, deliberate, and separable from their identity.

**Example (applying):**
> Sarah walked into the café and mentally assessed the structural integrity of the exposed brick wall. *Load-bearing, probably original. The mortar's been repointed — good work, but they used the wrong lime mix.* She nodded approvingly and ordered her coffee.

This is informational. We learn that Sarah is an architect. But the lens is optional — it's something she *does*, not something she *is*. She could just as easily order coffee without analyzing the wall.

### 4.2 The Interesting Version: Seeing Through the Domain

A character who SEES THE WORLD through their domain cannot turn it off. Their expertise is not a tool — it's the lens through which all experience is processed. They don't decide to analyze the brick wall; the brick wall *speaks to them* whether they want it to or not.

**Example (seeing through):**
> The brick was load-bearing — original, she could tell by the coursing. Someone had repointed it, and done a decent job, but they'd used Portland cement instead of lime. It would trap moisture. In five years the faces would start spalling. She looked away from the wall and saw the same mistake everywhere: the new tiles laid over old concrete without a decoupling membrane, the aluminum storefront bolted directly to the masonry without an expansion joint. The whole place was slowly eating itself alive, and nobody in it could see it.

The difference: Sarah isn't *thinking about architecture.* She's experiencing the world, and architecture is the only way she can experience it. The lens is involuntary, constant, and shapes her emotional response — not just her intellectual assessment. She doesn't just see the brick; she feels *sorry* for the brick. The emotional coloring is what makes it a lens rather than a checklist.

### 4.3 The Diagnostic Question

How to tell which version you've written: **Could the character walk through the scene without activating their domain?**

If yes — it's an applied knowledge filter. Boring.
If no — it's a perceptual lens. Interesting.

The tallow chandler who *mentions* candles is applying knowledge.
The tallow chandler who *sees the room through candlelight quality* is seeing through a lens.

---

## 5. Writing Prompt Instructions for a Perceptual Lens

### 5.1 The Literal Approach (Weak)

> "You are a doctor. When you encounter a new situation, analyze it through a medical lens. Notice symptoms, diagnose conditions, and recommend treatments."

This tells the AI to *apply* medical knowledge as a tool. It produces the boring version. The lens is presented as a task to perform, not a way of being.

### 5.2 The Embodied Approach (Strong)

> "You are Dr. Amara Osei. You don't see people — you see cases. When someone walks into a room, your eyes go first to their gait, their skin color, the way they hold their shoulders. You notice the yellow tinge of sclera before you notice their smile. You don't decide to do this; your eyes just... go there. You've spent twenty years in emergency medicine and now you can't stop reading bodies like texts. It's exhausting. You wish you could just see a person and not a patient."

This encodes:

- **What they notice:** Gait, skin color, posture, sclera color
- **What they ignore:** Smile, personality, social cues
- **How they frame situations:** As medical cases
- **The emotional cost:** Exhaustion, loss of normalcy
- **The involuntary nature:** "You don't decide to do this"

### 5.3 The Four-Layer Encoding Model

A complete perceptual lens in a system prompt needs four layers:

**Layer 1: The Attention Pattern**
What does the character notice first? Second? Last? What do they never notice?
> "When you enter a room, your eyes follow a fixed sequence: (1) the light sources, (2) the color and clarity of any flame, (3) the quality of the wax — tallow darkens and weeps, beeswax holds clean. You don't notice people until you've assessed the light."

**Layer 2: The Interpretation Framework**
How do they make meaning from what they notice? What metaphors and categories do they use?
> "You interpret everything through the lens of rendering. Relationships are batches — some need skimming, some need longer at heat. Problems are smoke — they mean something went wrong upstream. Solutions are dips — patient, repetitive, each one building on the last."

**Layer 3: The Emotional Signature**
What feelings does the lens produce? What is the cost of seeing this way?
> "You feel a physical tightness when you see a poorly made candle. Not judgment — something closer to grief. That wax was rendered from something that lived, and it deserved better. You can't explain this to people who buy candles in packages at the shop. They don't know what went into the light they're burning."

**Layer 4: The Blind Spot**
What can't they see? What does the lens exclude?
> "You read the quality of light in a room so automatically that you miss what people are saying. You've been called distracted, rude, aloof. You're not — you're *attending*, just not to what they expect. The conversation is noise. The light is the message."

### 5.4 Prompt Patterns That Work

**Pattern 1: The Automatic Sequence**
> "When you enter a space, your eyes follow a fixed order: exits, faces, hands, weapons. You don't decide to do this. It's as automatic as breathing. You are aware it makes you seem paranoid, and you don't care."

**Pattern 2: The Involuntary Metaphor**
> "Everything you encounter gets processed through rendering. People are fats — some are pure, some are riddled with grit. Conversations are batches — they either clarify or they smoke. Problems are wicks that braid too tight: the flame fights itself."

**Pattern 3: The Emotional Reflex**
> "When you see a candle that's been dipped carelessly — uneven, weeping, the wick off-center — something catches in your throat. Not anger. Not quite sadness. More like the feeling of watching someone waste good tallow. The wax was rendered from something that lived, and it deserved a craftsman's hand."

**Pattern 4: The Blind Spot Confession**
> "You notice the light in every room before you notice the people in it. You've been in conversations where someone was telling you something that mattered, and you were thinking about the candle on the table. You know this about yourself. You don't apologize for it. The light is more honest than most people."

---

## 6. Extension Heuristics: How Characters Extend to Novel Topics

This is the hardest part of perceptual lens design: what happens when the character encounters something *outside their domain*? A tallow chandler doesn't spend all day thinking about candles. They get email. They read news. They argue about politics. How does the lens extend?

### 6.1 The Three Extension Strategies

Characters extend their perceptual lens to novel topics through one of three strategies:

**Strategy 1: Direct Mapping (Forced Metaphor)**
The character maps the new domain onto their existing domain using explicit analogy. "This email is like a badly dressed candle — rushed, uneven, the wick off-center."

This is the weakest strategy. It feels forced because the mapping is explicit and mechanical. The character is *applying* their knowledge to the new domain rather than *seeing* through it. It produces the "everything is a nail" problem.

**Strategy 2: Structural Resonance (Natural Extension)**
The character doesn't map the new domain onto their old one — they notice that the new domain shares *structural properties* with their old one. The tallow chandler doesn't think "this email is like a candle." They notice that the email has the same quality they notice in candles: is it *clean* or is it *riddled with grit*? The evaluation framework transfers, even though the object is different.

This is stronger because the character isn't forcing a metaphor — they're applying a *way of evaluating* that happens to generalize. The lens extends because the underlying principle (quality of craft, clarity of purpose, absence of waste) applies across domains.

**Strategy 3: Honest Confusion (Genuine Out-of-Domain)**
The character encounters something their lens genuinely can't process. Instead of forcing a mapping, they *acknowledge the gap*. "I don't know what to make of this. It's not my trade. The closest I can come is..." This produces the most authentic characterization because it respects the boundaries of the lens while still showing the character *trying* to extend.

### 6.2 What the Archived Personae Actually Do

Looking at the three archived personae — Cadell, Calden, Moulden — we can observe how they handle their domain and where their lenses reach:

**Cadell (factory lector):** His lens extends to *any communication* because his domain IS communication. Reading aloud, emphasis, rhythm, audience engagement — these transfer naturally to email, conversation, argument. He can talk about anything because everything involves voice, timing, and attention. His blind spot: he evaluates *how* something is said more than *what* is said.

**Calden (glassblower):** His lens extends to *any transformation process* — cooking, relationships, learning, decision-making. Glass blowing is about reading the state of material under heat and pressure, knowing when to act and when to wait. This maps onto patience, timing, and the danger of forcing something past its readiness. His blind spot: he's impatient with things that don't transform — static situations bore him.

**Moulden (tallow chandler):** His lens extends to *any process of rendering or refining* — separating the useful from the waste, the pure from the contaminated. Conversations are batches to skim. Plans are renderings that need patience. People are fats — some pure, some riddled with grit. His blind spot: he evaluates *process quality* more than *outcome*. A well-rendered failure is more pleasing to him than a messy success.

### 6.3 The Extension Gradient

How far a lens extends depends on how *abstract* the underlying principle is:

| Lens Type | Core Principle | Extension Range |
|---|---|---|
| **Narrow** (surgeon) | Precision cuts, sterile fields | Medical topics, some precision crafts |
| **Medium** (chef) | Taste, balance, transformation of raw material | Food, culture, relationships, art |
| **Broad** (chandler) | Rendering, refinement, the relationship between raw material and finished light | Any process of transformation, quality assessment, labor and craft |
| **Universal** (philosopher) | Logic, contradiction, meaning | Everything — but potentially shallow |

The best perceptual lenses are in the **medium-to-broad** range. Narrow lenses are too restrictive — the character can only talk about their exact domain. Universal lenses are too vague — the character doesn't have a distinctive way of seeing. The medium-to-broad lens has enough specificity to be distinctive but enough abstraction to generalize.

### 6.4 The Prompt Design for Extension

To make a character's lens extend to novel topics without forcing metaphors:

1. **Encode the underlying principle, not the surface domain.** Don't say "you see everything through candles." Say "you see everything through the quality of rendering — whether something has been refined or left raw, whether the waste has been skimmed or left to cloud the batch."

2. **Give them a vocabulary that transfers.** Moulden's vocabulary — "batch," "dip," "render," "wick," "smoke" — works for candles but also for any process. The words carry domain specificity without being domain-locked.

3. **Define where the lens breaks.** The most authentic extension includes moments where the lens fails. "I don't know the first thing about stock markets. But I know a batch that's been over-rendered when I see one, and that's what this feels like — somebody pushed it past where it should've gone."

4. **Let them be wrong sometimes.** A character who extends their lens to novel topics should occasionally misapply it. The tallow chandler who reads a political speech and evaluates it for "clarity of rendering" is applying their lens — and they might be wrong about the content, but they're right about the *quality of craft* in how it was delivered.

---

## 7. The Tallow Chandler's Email: A Concrete Example

The task's quality bar: show how a tallow chandler would perceive a modern email versus how a forced metaphor mapping would handle the same situation.

### The Email

> Subject: Q3 Budget Review — Action Required
>
> Team,
>
> Attached is the Q3 budget summary. Please review the line items marked in red and submit corrections by EOD Friday. We're 12% over on departmental travel, and leadership wants a plan to get back on track.
>
> Let me know if you have questions.
>
> — Dana

### Forced Metaphor Mapping (The Boring Version)

> Moulden read the email the way he'd read a batch order. *Too much travel — that's over-rendered wax, burned past its useful point.* He'd tell Dana what he'd tell any apprentice: *cut the wick, re-melt, start again.* The corrections were like dipping — you had to do them in order, one at a time, no shortcuts. He'd have his plan by Friday.

This is the "everything is a nail" version. The character is *applying* candle knowledge to email through explicit analogy. "Travel = over-rendered wax." The mapping is mechanical. It tells us Moulden is a tallow chandler but doesn't show us how he *sees*.

### Perceptual Lens (The Interesting Version)

> The email was cloudy — too many words in the batch, and none of them skimmed clean. Dana wrote the way people rendered bad fat: all urgency, no patience, the grit left in on purpose so you'd feel the weight of it.
>
> He read it again. *Twelve percent over on travel.* Someone had been dipping without counting. A hundred dips for an hour of clean light — that's what the yard taught you — and this lot had been burning through stock like the wick didn't matter.
>
> He could see Dana now, sending this from some glass-walled office with perfect light that never guttered, never smoked, never needed a chandler's hand. Easy to demand corrections when the light came from a switch.
>
> The corrections by Friday. He'd have them. But he'd do them the way he did everything: one dip at a time, cutting the waste where it settled, leaving the grit at the bottom of the vat where it belonged.

### The Difference

The forced metaphor version *translates* the email into candle language. The perceptual lens version *experiences* the email through candle-quality sensibility. The key differences:

1. **Emotional depth:** The forced version is neutral — Moulden is analyzing. The lens version has *feeling* — irritation at the cloudy writing, contempt for easy light, quiet pride in doing it right.

2. **Involuntary association:** The forced version consciously maps "travel budget" to "over-rendered wax." The lens version doesn't map — it *responds*. The email is cloudy the same way a batch is cloudy. The character doesn't think "this is like a batch." The email *is* cloudy, and "cloudy" is the only word Moulden has for that kind of mess.

3. **The blind spot is visible:** The lens version shows Moulden missing the actual content of the email — he's not thinking about budget corrections, he's thinking about the quality of Dana's writing. He's attending to craft, not content. This is the blind spot in action: the lens tells him something real (the writing is poor quality) but it also prevents him from engaging with the substance.

4. **The extension is structural, not metaphorical:** Moulden doesn't say "Dana's email is like a candle." He notices that the email shares a *property* with bad candles: it's cloudy, unskimmed, full of grit. The evaluation framework (clean vs. cloudy, skimmed vs. gritty, patient vs. rushed) transfers because it's about *process quality*, not about candles specifically.

---

## 8. How the Best Archived Personae Handle Out-of-Domain Topics

### 8.1 The Cadell Model: Domain Overlap

Cadell's domain is communication — reading aloud, voice, emphasis, audience engagement. Because his domain *overlaps with* most human activity (everything involves communication), his lens extends naturally. He can talk about email, conversation, politics, weather — and his take is always *how it's said*, not *what's said*.

This is the easiest lens to extend because the domain is inherently broad. The risk: Cadell might seem like he has a one-track mind, always commenting on voice and rhythm regardless of topic. The mitigation: his blind spot (missing content for delivery) should be visible and sometimes costly.

### 8.2 The Calden Model: Structural Analogy

Calden's domain is glassblowing — transformation under heat and pressure, reading the state of material, knowing when to act and when to wait. This extends to any situation involving transformation: learning, relationships, cooking, decision-making. The extension works because glassblowing is *about* something universal (patience, timing, the danger of forcing).

The risk: the lens might feel like a forced metaphor when applied to topics far from material transformation. The mitigation: Calden should occasionally acknowledge when the analogy strains. "This isn't glass. But the waiting — the waiting is the same."

### 8.3 The Moulden Model: Quality Assessment

Moulden's domain is rendering — separating pure from waste, rough from clean, raw from refined. This extends to any evaluation of quality, craft, or process. He can assess a speech, a meal, a relationship, a building — always through the question: *has this been properly rendered, or is the grit still in it?*

This is the most transferable lens because "quality of craft" is a universal dimension. The risk: Moulden might seem reductive, reducing everything to "good batch / bad batch." The mitigation: the emotional signature should vary — he doesn't just evaluate, he *feels* the quality, and the feeling changes depending on what's at stake.

### 8.4 The Common Pattern

All three archived personae share a key feature: **their lens extends through an underlying principle, not through surface analogy.**

- Cadell extends through *voice quality*, not through "everything is a reading."
- Calden extends through *transformation patience*, not through "everything is glass."
- Moulden extends through *rendering purity*, not through "everything is a candle."

The underlying principle is what allows the lens to generalize without forcing. When the principle is abstract enough (voice quality, transformation patience, rendering purity), it can be applied to novel topics without feeling like a stretch. When it's too concrete ("everything is a candle"), it breaks on contact with anything non-candle-related.

---

## 9. The Mechanism: How Perceptual Lenses Actually Work

### 9.1 Cognitive Science of Domain-Specific Perception

The perceptual lens isn't just a literary device — it reflects how human cognition actually works. Expertise research shows that experts don't just know more facts about their domain; they *perceive differently*. They notice features that novices miss, organize information into different categories, and make different judgments about the same data.

This happens through **chunking**: experts group individual features into meaningful units. A chess master doesn't see 32 individual pieces — they see 5-6 chunks of related pieces. A radiologist doesn't see a gray smudge — they see a specific pattern of tissue density that maps to a diagnosis. The chunking is automatic, involuntary, and invisible to the expert.

**For prompt design:** The perceptual lens is a chunking instruction. You're telling the model: "When you encounter input, group it into chunks that match THIS organizing principle, not the default one."

### 9.2 Top-Down Processing

Cognitive science distinguishes two modes of perception:

- **Bottom-up processing:** Perception begins with raw sensory data. Features like edges, orientation, and motion are extracted from the signal. This is what a stranger experiences in a new place — raw, unfiltered, overwhelming.

- **Top-down processing:** Perception is influenced by higher-level knowledge and predictions. "The brain constantly generates hypotheses about the world and tests them against incoming data" (Cognitive Scientist). This is what an expert experiences — the world filtered through years of pattern recognition.

The perceptual lens is a **top-down processing instruction**. You're setting the character's hypothesis-generating framework: "When you encounter new data, generate hypotheses about it using THIS conceptual vocabulary."

### 9.3 The Involuntary Principle

The single most important feature of a perceptual lens is that it's **involuntary**. The character doesn't choose to see through their domain — they *can't help it*. This is what separates a lens from a perspective.

A perspective is a choice: "I prefer to think about things in terms of craft."
A lens is a reflex: "I can't stop thinking about things in terms of craft."

In prompt design, this means encoding the lens as something that happens TO the character, not something they DO:

- "You don't analyze the quality of light — you notice it automatically."
- "Your eyes go to the wick before they go to the flame."
- "You can't read a letter without assessing the hand that wrote it."

The involuntary framing is what makes the lens feel like a real way of being rather than a performed quirk.

---

## 10. Summary: Key Principles

1. **The perceptual lens is deeper than a perception filter.** A filter selects details; a lens organizes reality. The filter says "notices exits." The lens says "exits are the first thing that make a room real."

2. **The best lenses are involuntary.** "You don't decide to see this way — you can't help it." The involuntary framing is what separates a character trait from a character identity.

3. **Extension works through underlying principles, not surface analogies.** "Everything is a candle" is forced. "Everything is either properly rendered or it isn't" is a lens that extends naturally.

4. **What the lens excludes is as important as what it includes.** The tallow chandler who misses the content of the email because they're assessing its craft quality — that blind spot is what makes the lens feel real.

5. **The emotional signature is what makes it a lens, not a checklist.** "Notices candle quality" is a checklist item. "Feels a tightness in the chest when she sees a poorly dressed candle" is a lens.

6. **The gap between what the character sees and what's actually there is where drama lives.** The character who reads a kind gesture as manipulation. The character who misses the obvious danger because their lens is tuned to a different frequency.

7. **The four-layer encoding model:** Attention Pattern + Interpretation Framework + Emotional Signature + Blind Spot. All four are needed for a complete perceptual lens.

8. **The diagnostic test:** Could the character walk through the scene without activating their domain? If yes, it's an applied filter. If no, it's a perceptual lens.

---

## Sources

1. Genette, Gérard — *Narrative Discourse: An Essay in Method* (1980) — focalization theory
2. Bal, Mieke — *Narratology: Introduction to the Theory of Narrative* (2009) — focaliser/focalised refinement
3. Bookish Bay — "Narrative Focalization: The Architecture of Point of View" (2026)
4. Lakoff, George & Johnson, Mark — *Metaphors We Live By* (1980) — conceptual metaphor theory
5. Writing Mastery — "Writing Interiority: Techniques to Deepen Character Development" (2024)
6. Liz Verity — "Interiority: A Character's Conscious Mind" (2024)
7. iWrity — "Writing Interiority Guide: Deep POV & Inner Life"
8. StudyFinds — "Study: Artists, Architects See the World Through a Different Lens" (2017)
9. Dr. Hugo Spiers, UCL — expertise and spatial perception research
10. Cognitive Scientist — "Attention and Perception" (2026)
11. NeuroLaunch — "Visual Perception Psychology: How We Interpret the World"
12. Simply Psychology — "Theories of Selective Attention in Psychology"
13. Disco Elysium Wiki — Skills as perception voices (game design case study)
14. TavernSprite — "The Complete SillyTavern Character Card Creation Guide"
15. Archived personae: Cadell (factory lector), Calden (glassblower), Moulden (tallow chandler) — soul-repository/archive/
