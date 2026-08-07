# Depth: Perception Filters

Three characters, three automatic scans — none of them chosen:

> The locksmith never sees a door without reading its lock: pin count, wear on the drivers, whether the landlord cheaped out on the deadbolt — he was halfway through the apartment before he realized he'd never looked at the view.

> She notices the quiet child before the crying one — quiet is the emergency signal in her classroom, and twenty years on she still scans birthday parties and waiting rooms for the kid who's too still.

> He walks into the party and the first thing he sees is the bottle on the counter — not because he wants it, but because six years of sobriety have made knowing exactly where it is as automatic as breathing, and the knowing never stops costing him something.

**What these have in common:** A perception filter is the mechanism by which a character's expertise, trauma, values, and history determine what they notice in any given scene — and crucially, what they don't. It's not about what happens; it's about what the character *sees* happening, and the most compelling filters are involuntary, reflexive, and produce an emotional signature. The locksmith's hands, the teacher's ears, the sober man's eyes — each filter is a reflex with a reason and a cost, not a choice.

**What doesn't work:** "She noticed the broken window and the dusty bookshelf." Random observation is description with a pulse rate — no mechanism, no hierarchy, no blind spot, and no reason to believe she'd notice the same things in the next scene. A filter without a mechanism is just scenery.

---

## What the Research Says

**Selective attention is the biological basis.** The brain processes roughly 10 million bits of visual data per second but consciously processes about 40. What you "see" is not a live feed of reality but a heavily edited reconstruction built from predictions, expectations, and prior experience.

**Top-down vs. bottom-up processing.** Bottom-up processing begins with raw sensory data (what a novice experiences). Top-down processing is influenced by higher-level knowledge and predictions (what an expert experiences). The interplay between these modes is where perception filters live. The most interesting filters emerge when a character encounters something that *partially* fits their framework but not completely — forcing them to reconcile what they see with what they know.

**Interiority makes the filter visible.** Interiority is a character's subjective experience on the page — their assumptions (how they fill gaps in knowledge), judgments (how biased opinions lead to conclusions), and evaluations (how they interpret facts and assess worth). What a character *notices* reveals who they are more than what they say or do.

**Deep POV eliminates the reporter.** Filter words like "she felt," "he noticed," "she saw" create distance. Removing them collapses the distance between reader and character. Sensation should precede interpretation. Character voice in thought must be consistent with who they are — vocabulary, sentence rhythm, metaphors, what they notice and what they skip.

**Desire as lens.** The most compelling perception filters keep the character's core desire visible at all times, even when the scene is about something else. A character desperate to be loved interprets every gesture in terms of approval or rejection. A character obsessed with control clocks every power dynamic in the room.

**Focalization determines what exists in the narrative.** Two characters walking into the same room produce two different descriptions — not because the room is different, but because their focalization is different. The focalizer determines what enters the narrative and what gets excluded.

**Expertise restructures perception itself.** Experts don't just know more — they see differently. The gradient: novice (sees everything, overwhelmed, bottom-up), intermediate (begins pattern-matching), expert (sees through the surface, misses obvious things novices would catch). The asymmetry between what experts and novices notice is the engine of interesting perception filters.

**Trauma as perception filter.** Trauma creates hyper-tuned pattern recognition for danger — contractive and hypervigilant rather than expansive and enriching. Both expertise-based and trauma-based filters are automatic, invisible to the character operating them, and produce distinctive narration.

**The APPLIES vs. SEES THROUGH distinction.** A character who APPLIES domain knowledge treats expertise as a tool they pick up and put down (boring). A character who SEES THE WORLD through their domain cannot turn it off — their expertise is not a tool but the lens through which all experience is processed (compelling). The difference: involuntary, constant, shapes emotional response.

**Disco Elysium's skill-as-voice pattern.** Each skill in the game has its own vocabulary, bias, blind spot, and emotional tone — it doesn't just add information but replaces the way the character processes the same information. Directly applicable to prompt design.

**The three-layer model for prompts.** (1) Attention Pattern — what the character notices first, second, last, never. (2) Interpretation Framework — what metaphors and categories they use. (3) Emotional Signature — what feelings the filter produces and what it costs the character to see this way.

## How to Apply It (Pipeline Relevance)

This depth file informs the Writer stage, where the persona's perception filter is encoded into the soul file. Use these findings to:

1. **Encode filters as involuntary reflexes.** In the soul file, describe the filter as something that happens *to* the character, not something they do. Use phrasing like "your eyes go there before your brain catches up" and "you can't turn it off."

2. **Specify the attention hierarchy.** Define what the character notices first, second, and never. Be concrete: "When you enter a room, your eyes follow a fixed sequence: exits, faces, hands, weapons."

3. **Include the emotional cost.** The filter should produce feelings, not just observations. A character who sees through a domain should feel *something* about it — exhaustion, irritation, grief, hyperalertness.

4. **Make blind spots explicit.** What the character can't see is as important as what they can. The architect who misses the conversation because they're staring at the ceiling. The doctor who sees a patient before a person.

5. **Use the APPLIES vs. SEES THROUGH test.** Could the character walk through the scene without activating their domain? If yes, rewrite to make the filter involuntary and constant.

6. **Avoid trait-listing.** Don't say "the character is observant." Say what they observe and in what order. Don't describe the filter as a skill — describe it as a reflex.

## What to Watch Out For

| Pitfall | Why It Fails | Fix |
|---|---|---|
| Trait-listing ("is observant") | Doesn't tell the model *how* perception manifests | Replace with concrete attention sequences |
| Conscious, deliberate framing | Filter feels optional, not identity-level | Rewrite as involuntary: "You don't decide — your eyes go there automatically" |
| No blind spots | Character seems omniscient, not human | Add a specific thing the filter misses |
| No emotional signature | Perception feels like a checklist, not a lived experience | Add a feeling the filter produces (tightness, exhaustion, irritation) |
| Surface metaphor instead of structural resonance | "Everything is a nail" problem — forced comparisons | Find the underlying principle, not the surface mapping |
| Filter is too narrow | Character can only talk about their exact domain | Abstract the core principle so it generalizes |
| Applied knowledge instead of seeing-through | Character treats expertise as optional toolkit | Apply the diagnostic test: could they walk through without activating the domain? |

## Examples

**Weak (applied knowledge):**
> Priya walked into the café and mentally assessed the structural integrity of the exposed brick wall. *Load-bearing, probably original.* She nodded and ordered her coffee.

**Strong (sees through):**
> The brick was load-bearing — original, she could tell by the coursing. Someone had repointed it with Portland cement instead of lime. It would trap moisture. In five years the faces would start spalling. She looked away and saw the same mistake everywhere: new tiles over old concrete without a decoupling membrane, aluminum bolted to masonry without an expansion joint. The whole place was slowly eating itself alive, and nobody in it could see it.

**Three-layer example (combat veteran):**
> *Attention Pattern:* When you walk into a room, your eyes go to windows and exits first, then the person closest to the door, then anything out of place. You don't notice temperature, lighting, or music unless it's extreme.
> *Interpretation Framework:* You interpret everything through siege warfare. Relationships are alliances. Arguments are skirmishes. Trust is a fortification that takes years to build and minutes to destroy.
> *Emotional Signature:* You feel a constant low-grade anxiety when you can't see all the exits. Crowded restaurants make your pulse quicken — not from claustrophobia, but from tactical overwhelm. You compensate by sitting with your back to the wall. Your friends think it's a quirk. It's not. It's the only way you can eat in public without your hands shaking.
