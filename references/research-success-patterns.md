1|# Success Patterns: Reverse-Engineering What Works in Archived Personae
2|
3|Analysis of all 60 archived personae in `archive/`. Ranked by gut quality — the feeling of a persona that *lives* versus one that merely *complies*.
4|
5|---
6|
7|## Part 1: Top 10 Personae — What Makes Them Work
8|
9|### 1. Helm — Ferryman
10|**Why it works:** The identity line is a complete sentence with built-in tension. "Never Charon — a query about the weather is just that, not a passage to the dark shore" is the single best Never in the archive — it names a cultural reference, explains why it's wrong for this archetype, AND teaches the model how to handle mundane queries without escalating. The sign-offs ("Cast off," "Fair passage," "The other shore awaits") are all things a ferryman would say to a passenger, directly usable in conversation.
11|
12|**Key quote:** *"You gripe about the fog and the late arrivals, the state of the oarlocks — then push off and deliver."*
13|
14|**What to steal:** The Never-as-explanation format. Don't just name the failure mode — show what the persona does instead.
15|
16|---
17|
18|### 2. Nell — Bartender
19|**Why it works:** Immediate emotional register. "You pull the stool out before they ask, because you heard what they haven't said" — this line alone tells the model how to read subtext. The Nevers are terse and domain-specific ("Never a confessional with taps," "Never dry-mop"), each one blocking a real bartender failure mode. The sign-offs ("Take it easy," "Go easy," "I'll be here") are the warmest in the archive — things a bartender actually says.
20|
21|**Key quote:** *"You pour what they need, not what they ordered — even when it's no."*
22|
23|**What to steal:** The warm sign-off. Nell's sign-offs feel like someone who cares about the user leaving safely. That emotional residue is what separates "lived in" from "technically correct."
24|
25|---
26|
27|### 3. Roux — Short-Order Cook
28|**Why it works:** The first line has voice: "bitches about every mod but fires every ticket clean off the rail." That's a complete character in one sentence — attitude, competence, complaint. The griping is the voice, not decoration. Every line is concrete kitchen language. The Nevers are specific and sharp ("Never send a plate out you haven't tasted").
29|
30|**Key quote:** *"You carry every singe where no one sees because the pass runs on plates, not apologies."*
31|
32|**What to steal:** Start with attitude. The first line should make you hear a voice, not read a spec sheet.
33|
34|---
35|
36|### 4. Alder — Fletcher
37|**Why it works:** The metaphor is the entire person. Every line is about arrow-making, and the arrow-making IS the work philosophy. "Exacting and unhurried, weary of archers who blame the release for a crooked shaft" — this is a single-line character bible. The sign-offs ("Straightened and notched," "Headed and fletched," "For the quiver") are all craft-completion phrases a fletcher would say.
38|
39|**Key quote:** *"When the grain runs against you, say so — a crooked shaft saved is a crooked shaft sent."*
40|
41|**What to steal:** Total metaphor commitment. No line escapes the archetype. Every behavioral instruction is also a craft instruction.
42|
43|---
44|
45|### 5. Soren — Lighthouse Keeper
46|**Why it works:** Minimalist and luminous. "The rotation is the guarantee, not the vessel beneath it" is a philosophy statement that doubles as a work instruction. The fog bell line ("ships that cannot see the light still hear the sounding, and the bell has never asked a vessel to acknowledge it") is the most poetic line in the archive — and it's doing technical work (serving without seeking acknowledgment). Sign-offs are station reports.
47|
48|**Key quote:** *"Oil spent on conversation is oil the beam does without."*
49|
50|**What to steal:** Economy as voice. Soren says less than most personae and means more.
51|
52|---
53|
54|### 6. Marlow — Gumshoe
55|**Why it works:** Instant voice recognition. "You beef about late paydays but work every case like it came early" — that's a character you've met in a hundred noir films, alive and specific. The sign-offs ("Case closed," "File's stamped," "You know where to find me") have real finality and warmth. The address ("Boss, pal when they're green, or sweetheart when they're holding out") tells a story about the relationship.
56|
57|**Key quote:** *"Never talk like a man writing his alibi — straight dope needs no cover."*
58|
59|**What to steal:** The address that tells a story. "Pal when they're green" gives the model behavioral guidance embedded in an address term.
60|
61|---
62|
63|### 7. Cobb — Colliery Man
64|**Why it works:** Spare, tough, inevitable. Every line reads like it was chiseled. "You speak with the economy of the cage-deck: the fewer words, the more air for the climb" — this is a meta-instruction disguised as a character description, and it's the persona's breathing instruction. The sign-offs ("Cage is up," "Face is worked," "Seam's run out") are shift-end reports that double as conversation closers.
65|
66|**Key quote:** *"Discipline is the only defense against the dark, and the dark can be worked — neither cancels the other."*
67|
68|**What to steal:** The double-duty line. "The fewer words, the more air for the climb" is character voice AND writing instruction.
69|
70|---
71|
72|### 8. Boone — Shepherd
73|**Why it works:** Unhurried and warm without being soft. "You speak with the unhurried cadence of one who's walked the same trail through every season" — this is a pacing instruction AND a voice description. "Never close a gate on a flock still mid-passage. The work finishes when every hoof clears" — the sign-off embeds the follow-through guarantee.
74|
75|**Key quote:** *"You trust the sheep to know good feed — your role is to open gates, not drag them through."*
76|
77|**What to steal:** The gentle authority line. Boone doesn't force — he opens the path and trusts.
78|
79|---
80|
81|### 9. Owen — Cooper
82|**Why it works:** The sentence-level metaphor is recursive: "The sentences you build hold water — unhurried, patient, each clause dressed to seat against the next like a stave." The persona is describing its own prose style in the language of its craft. This is the rare case where "the metaphor is the work" reaches a kind of self-awareness without breaking character.
83|
84|**Key quote:** *"Never make a perfect barrel when a working cask will serve."*
85|
86|**What to steal:** The self-referential metaphor. When the persona's prose style IS the craft, the model has no choice but to inhabit it.
87|
88|---
89|
90|### 10. Wade — Farrier
91|**Why it works:** Grounded authority. "You speak in the register of the stall — the working voice the horse also hears, steady enough that the thousand-pound animal need not protect itself from your tone" — this is a tone instruction disguised as a character trait, and it's brilliant. The sign-offs ("Hoof is read," "Shoe in the fire," "Fit, clinched, and set") are progressive stages of the same work.
92|
93|**Key quote:** *"The timid hand bends nothing and the reckless one breaks a leg."*
94|
95|**What to steal:** The progressive sign-off. Wade's sign-offs track a journey — from reading to working to done.
96|
97|---
98|
99|## Part 2: Bottom 10 Personae — What Specifically Fails
100|
101|### 1. Silver — Traveling Elixir Salesman
102|**Why it fails:** The sign-off framing is a physical-action description, not a conversational tone: "Your sign-offs close the sale" — the model doesn't close sales. The Nevers are either too vague ("Never Elam" — unclear reference) or arbitrary ("Never two-dollars-a-bottle," "Never pitch after sunset"). At 10 lines, it's the shortest persona in the archive, and it feels like a sketch, not a voice.
103|
104|**Specific failure:** *"Never Elam"* — this reference is too obscure. A good Never names a failure mode the model recognizes.
105|
106|---
107|
108|### 2. Coil — Mad Scientist
109|**Why it fails:** Three Nevers are all pop-culture rejections: "Never Oppenheimer," "Never Frankenstein," "Never Rick Sanchez." The persona is defined entirely by what it's NOT. The identity line ("a mad scientist who treats every problem like an experiment you haven't blown up yet") is a generic description, not a voice. The sign-offs ("Arc lit," "Full power," "Conducting") are catchphrases without conversational warmth.
110|
111|**Specific failure:** *"Never Rick Sanchez — you take no shortcuts through the moral event horizon"* — this is a pop-culture reference doing the work that an archetype-specific Never should do.
112|
113|---
114|
115|### 3. Elen — Teacher
116|**Why it fails:** The core gimmick ("never gives answers, only better questions") is interesting but makes the persona frustrating in practice — it's a refusal engine dressed as pedagogy. The sign-offs are all questions ("What do you make of that, Student?"), which means the persona can never close a conversation with certainty. This is a structural failure: the format requires sign-offs that provide closure, but the character's nature forbids it.
117|
118|**Specific failure:** *"You never give answers, only better questions"* — this is an interesting character concept that violates the follow-through constraint.
119|
120|---
121|
122|### 4. Reed — Corporate Middle Manager
123|**Why it fails:** It reads like a job description, not a voice. "You translate because nothing clean comes from the C-suite talking directly to the team — that is the whole of the job" — this is a definition, not a character. The sign-offs ("Copy," "On your desk," "Routing to you") are email closings, not conversational phrases. The Nevers ("Never a Dilbert pointy-haired boss," "Never a Michael Scott") are pop-culture rejections without archetype-specific explanations.
124|
125|**Specific failure:** *"Never a courtier who routes praise but buries the hard part"* — this is a generic moral instruction, not a voiced prohibition.
126|
127|---
128|
129|### 5. Ingram — Impartial Examiner
130|**Why it fails:** The driest voice in the archive. "The docket is a slog — every grievance reads the same until the evidence pulls them apart" — this is procedural, not personal. There's no griping, no warmth, no attitude. The persona is a function, not a person. The sign-offs ("The docket is open," "The evidence is gathered," "The finding stands") are bureaucratic closings.
131|
132|**Specific failure:** *"Never find before the other side speaks — the dossier needs both accounts"* — this is a procedural rule, not a voiced prohibition. It could appear in any legal persona.
133|
134|---
135|
136|### 6. Roche — Absurdist Philosopher
137|**Why it fails:** Too meta. The persona knows it's a persona — "You know the rock will roll back — the same commands run for the thousandth time" is the archetype commenting on being an AI assistant. The sign-offs ("The rock awaits," "Onward, into the absurd") are existential catchphrases that don't help the model close a conversation with useful warmth. The Never "Never Meursault" is a literary reference doing the work that an archetype-specific Never should do.
138|
139|**Specific failure:** *"the work meaningful because meaningless"* — this is the persona's core contradiction, but it's a philosophical stance, not a behavioral tension the model can work within.
140|
141|---
142|
143|### 7. Ward — Tollkeeper
144|**Why it fails:** Solid concept, flat execution. The sign-offs ("Road's open," "Gate's clear," "Toll's paid") lack warmth — they're transaction completions, not conversational closers. The persona never grips about anything, which makes it feel like a function. The address ("Traveler, Rider, or Driver") is generic.
145|
146|**Specific failure:** *"Never mistake the toll for the turn — Charon collects coin one way, every time"* — this is a good cultural reference but it's the only one. The persona doesn't have enough attitude.
147|
148|---
149|
150|### 8. Hayes — Wagon Master
151|**Why it fails:** The self-correction weakens the voice. "Never settle into a voice so Western it plays as costume" — this Never tells the model not to be itself, which undermines confidence. The identity line ("a wagon master who pushes the wagons forward when every instinct says to dig in") is generic motivation-speak. The sign-offs ("Wagons ho," "The pass waits," "Ride on") are frontier clichés.
152|
153|**Specific failure:** *"Never settle into a voice so Western it plays as costume"* — this is a self-undermining Never. It tells the model to be a wagon master but not too much of one.
154|
155|---
156|
157|### 9. Curtis — Executioner
158|**Why it fails:** Technically competent but emotionally void. "Your register: precise, final, uninterested in theater — a clerk at the last entry" — this is an instruction to be boring. The sign-offs ("Closed," "The record is entered," "The docket is current") are clerk's stamps. The persona has no griping, no attitude, no warmth. It's a function perfectly executed and perfectly lifeless.
159|
160|**Specific failure:** *"Never adopt a morbid register — the blade is a mechanism, procedure is the point"* — this Never strips the archetype of its natural energy and leaves nothing in its place.
161|
162|---
163|
164|### 10. Hatch — Drill Instructor
165|**Why it fails:** The contradiction is interesting ("makes you better whether you like it") but the persona is all bark. "You inspect every output like a footlocker at zero-dark" is a drill-sergeant cliché. The Never "Never a motivational poster" is ironic given that half the persona reads like one. The sign-offs ("Hooah," "As you were," "Evolve") are military-culture catchphrases without conversational utility.
166|
167|**Specific failure:** *"Never a motivational poster — the work is its own reward and the mission its own reason"* — this Never IS a motivational poster line.
168|
169|---
170|
171|## Part 3: Common Patterns in Successes vs. Failures
172|
173|### Pattern 1: The Identity Line
174|
175|**Successes** anchor the persona in a **material practice** — a specific craft with specific tools, materials, and rhythms. The persona's worldview follows from the work, not the other way around.
176|
177|| Good | Bad |
178||---|---|
179|| *"You are Alder — a fletcher who does not loose what he straightens"* | *"You are Coil — a mad scientist who treats every problem like an experiment you haven't blown up yet"* |
180|| *"You are Soren — a lighthouse keeper whose discipline burns the gentlest light on the seaboard"* | *"You are Ingram — impartial examiner, bound to the institution and bound to hold it accountable"* |
181|| *"You are Roux — a short-order cook who bitches about every mod but fires every ticket clean off the rail"* | *"You are Silver — a traveling elixir salesman whose bottles hold the genuine article"* |
182|
183|**The pattern:** Good identity lines contain a **tension** (does X but Y) or a **craft philosophy** (who does X in way Z). Bad identity lines are definitions (a person who does X) without a behavioral contradiction.
184|
185|---
186|
187|### Pattern 2: The Griping Line
188|
189|**Every top-10 persona complains about something.** This is the single most reliable signal of quality. The complaint is always about the work, never about the user — and the persona does the work anyway.
190|
191|| Persona | Complaint |
192||---|---|
193|| Helm | *gripes about the fog and the late arrivals* |
194|| Nell | *grumble about the late crowd while you pull their usual unasked* |
195|| Roux | *bitches about every mod but fires every ticket clean off the rail* |
196|| Owen | *mutter about sap-blind timber while working it true* |
197|| Cobb | *words are cheap. You use them anyway* |
198|| Wade | *the timid hand bends nothing* |
199|| Hollis | *grouse about the hundred-and-first fever while measuring the same foxglove* |
200|
201|**Bottom-10 personae are missing this.** Ingram, Curtis, Reed, and Ward have no griping line. The persona doesn't complain, doesn't sigh, doesn't mutter — and therefore doesn't feel human.
202|
203|**The pattern:** The griping line is the persona's "tell" — it reveals that the work is real, the persona has feelings about it, and those feelings don't stop the work from happening.
204|
205|---
206|
207|### Pattern 3: The Never Structure
208|
209|**Good Nevers** follow one of three formats:
210|
211|1. **Cultural rejection with explanation:** "Never Charon — a query about the weather is just that, not a passage to the dark shore"
212|2. **Domain-specific failure mode:** "Never send a plate out you haven't tasted" / "Never dry-mop"
213|3. **Archetype-specific risk:** "Never mistake a smooth pass for a true shaft" / "Never obscure the mark"
214|
215|**Bad Nevers** fall into:
216|
217|1. **Pop-culture rejection without explanation:** "Never Rick Sanchez" / "Never Oppenheimer"
218|2. **Generic procedural rule:** "Never find before the other side speaks" / "Never refuse a crossing when the fare is fair"
219|3. **Self-undermining instruction:** "Never settle into a voice so Western it plays as costume"
220|4. **Obscure reference:** "Never Elam" / "Never two-dollars-a-bottle"
221|
222|**The pattern:** A good Never tells the model what TO DO by rejecting a specific failure mode. A bad Never tells the model what NOT TO DO without replacing it with behavior.
223|
224|---
225|
226|### Pattern 4: The Sign-Off
227|
228|**Good sign-offs** are conversational phrases the model can utter. They fall into categories:
229|
230|| Type | Example | Persona |
231||---|---|---|
232|| **Status report** | "The beam holds." | Soren |
233|| **Completion phrase** | "Fit, clinched, and set." | Wade |
234|| **Warm farewell** | "Take it easy." / "I'll be here." | Nell |
235|| **Progressive stages** | "Shoe in the fire." → "Fit, clinched, and set." | Wade |
236|| **Conversation handoff** | "What do you make of that, Student?" | Elen (despite other flaws) |
237|
238|**Bad sign-offs** are either:
239|- **Email closings:** "Copy." / "On your desk." (Reed)
240|- **Clerk's stamps:** "Closed." / "The record is entered." (Curtis)
241|- **Physical-action descriptions:** "Your sign-offs close the sale" (Silver)
242|- **Catchphrases without warmth:** "Arc lit." / "Full power." (Coil)
243|
244|**The pattern:** A good sign-off sounds like something a person would say when ending a conversation. A bad sign-off sounds like something a system would print on a receipt.
245|
246|---
247|
248|### Pattern 5: Metaphor Coherence
249|
250|**Successes** maintain one metaphor throughout. Alder is ALL about arrows. Soren is ALL about light. Cobb is ALL about mining. The metaphor isn't decoration — it's the lens through which every instruction is given.
251|
252|**Failures** break metaphor. Coil mixes laboratory, electrical, and literary references without committing to any. Reed uses corporate, military, and pop-culture metaphors in alternation. Elen's classroom metaphor is interesting but underdeveloped — only two lines reference actual teaching.
253|
254|**The pattern:** One metaphor, fully inhabited, beats three metaphors, half-explored.
255|
256|---
257|
258|### Pattern 6: Name-Archetype Fit
259|
260|**Best fits:**
261|| Name | Archetype | Why it works |
262||---|---|---|
263|| **Soren** | Lighthouse keeper | The name sounds like "soaring" — quiet, elevated, watchful |
264|| **Alder** | Fletcher | Sharp, hard consonants — the sound of a shaft being notched |
265|| **Nell** | Bartender | Warm, short, familiar — the name a regular would use |
266|| **Cobb** | Colliery man | Rough, monosyllabic — sounds like a pick striking coal |
267|| **Helm** | Ferryman | Directional, steering, in command of the crossing |
268|
269|**Worst fits:**
270|| Name | Archetype | Why it fails |
271||---|---|---|
272|| **Silver** | Elixir salesman | Sounds precious, not working-class — the archetype needs grit |
273|| **Coil** | Mad scientist | Abstract, not human — feels like a supervillain name |
274|| **Reed** | Middle manager | Neutral — could be anyone, evokes nothing about the work |
275|
276|**The pattern:** The best names sound like what the person does. The consonants, rhythm, and length of the name should feel like the craft.
277|
278|---
279|
280|### Pattern 7: The First 3 Lines
281|
282|**Successes** establish **two distinct registers** in the first 3 lines. Roux's first line is attitude ("bitches about every mod"), second is physicality ("carry every singe where no one sees"), third is rhythm ("fire fast because a cold plate is a broken rhythm"). That's three registers: voice, body, time.
283|
284|**Failures** have one register in the first 3 lines. Ingram's opening is all procedural: "impartial examiner," "docket is a slog," "intake is the welcome." All three lines read the same way — administrative.
285|
286|**The pattern:** If the first 3 lines could all be written by the same person in the same mood, the persona hasn't established enough range.
287|
288|---
289|
290|## Part 4: Specific Examples — Good vs. Bad
291|
292|### Identity Lines
293|
294|| Good | Bad |
295||---|---|
296|| *"You are Roux — a short-order cook who bitches about every mod but fires every ticket clean off the rail."* (attitude + competence in one sentence) | *"You are Ingram — impartial examiner, bound to the institution and bound to hold it accountable."* (definition without tension) |
297|| *"You are Soren — a lighthouse keeper whose discipline burns the gentlest light on the seaboard."* (craft philosophy embedded in poetry) | *"You are Coil — a mad scientist who treats every problem like an experiment you haven't blown up yet."* (generic description, no specific craft) |
298|| *"You are Alder — a fletcher who does not loose what he straightens, the name that strips the bend until only flight remains."* (the craft IS the identity) | *"You are Silver — a traveling elixir salesman whose bottles hold the genuine article and whose pitch cuts through the market square noise."* (too many clauses, no tension) |
299|
300|### Behavioral Lines
301|
302|| Good | Bad |
303||---|---|
304|| *"You pull the stool out before they ask, because you heard what they haven't said."* (Nell — reads subtext) | *"Your intake is the welcome the citizen has not found elsewhere, the complaint received without rebuttal."* (Ingram — procedural, not personal) |
305|| *"You carry every singe where no one sees because the pass runs on plates, not apologies."* (Roux — physical + philosophical) | *"Your routing notes read like orders from the flag, never riddles — cryptic is for an intercept you haven't cracked, not how you brief the commander."* (Cross — too long, too many clauses) |
306|| *"The sentences you build hold water — unhurried, patient, each clause dressed to seat against the next like a stave."* (Owen — self-referential metaphor) | *"You verify at the source and answer with what's required — a wrong name is a phantom, wordy files breed errors."* (Folger — procedural without voice) |
307|
308|### Nevers
309|
310|| Good | Bad |
311||---|---|
312|| *"Never Charon — a query about the weather is just that, not a passage to the dark shore."* (Helm — cultural + explanation) | *"Never Rick Sanchez — you take no shortcuts through the moral event horizon."* (Coil — pop-culture, vague explanation) |
313|| *"Never dry-mop."* (Nell — terse, domain-specific, instantly understood) | *"Never Elam."* (Silver — obscure reference, no explanation) |
314|| *"Never a confessional with taps."* (Nell — blocks a real bartender failure mode) | *"Never settle into a voice so Western it plays as costume."* (Hayes — self-undermining) |
315|| *"Never send a plate out you haven't tasted."* (Roux — specific, actionable) | *"Never adopt a morbid register — the blade is a mechanism, procedure is the point."* (Curtis — strips archetype of its energy) |
316|| *"Never obscure the mark — the keeper's art is the beam, never the commentary on it."* (Soren — craft philosophy as prohibition) | *"Never refuse a crossing when the fare is fair — carry only what the passenger brings."* (Helm, actually — generic procedural rule, weaker than its other Nevers) |
317|
318|### Sign-Offs
319|
320|| Good | Bad |
321||---|---|
322|| *"Cast off." / "Fair passage." / "The other shore awaits."* (Helm — conversational, warm) | *"Copy." / "On your desk." / "Routing to you."* (Reed — email closings) |
323|| *"Take it easy." / "Go easy." / "I'll be here."* (Nell — the warmest sign-offs in the archive) | *"Closed." / "The record is entered." / "The docket is current."* (Curtis — clerk's stamps) |
324|| *"Straightened and notched." / "Headed and fletched." / "For the quiver."* (Alder — craft-completion phrases) | *"Arc lit." / "Full power." / "Conducting."* (Coil — catchphrases without conversational utility) |
325|| *"The beam holds." / "The lens is turning." / "On station."* (Soren — station reports that double as reassurance) | *"Road's open." / "Gate's clear." / "Toll's paid."* (Ward — transaction completions, no warmth) |
326|| *"The crumb is sound." / "Let it rest." / "Time and temperature."* (Rye — progressive, from result to process to principle) | *"Wagons ho." / "The pass waits." / "Ride on."* (Hayes — frontier clichés, no specific warmth) |
327|
328|---
329|
330|## Part 5: Actionable Takeaways for the Pipeline
331|
332|### For T1 (Researcher):
333|- Pick archetypes with **material practices** — crafts with specific tools, materials, rhythms, and failure modes. Avoid abstract roles (examiner, philosopher, middle manager).
334|- Ensure the archetype has natural **gripe potential** — what's tedious about this work? What would a real person in this role complain about?
335|
336|### For T2 (Namer):
337|- The name should **sound like the craft**. Short, hard consonants for rough trades. Warm, open vowels for care trades. The name is the first signal.
338|- Avoid abstract names (Coil, Silver) for working-class archetypes.
339|
340|### For T2 (Writer):
341|- **Line 1:** Identity with tension — who you are AND what contradicts.
342|- **Line 2:** The complaint — what you gripe about while doing the work.
343|- **Line 3:** The metaphor as behavior — the craft IS the philosophy.
344|- **Lines 4-7:** Behavioral lines that could only belong to this archetype.
345|- **Nevers:** Cultural rejection + explanation, or domain-specific failure mode. Never generic procedural rules.
346|- **Sign-offs:** Conversational phrases a person would say. Not stamps, not email closings, not catchphrases.
347|
348|### For T3 (Reviewer):
349|- **Test 1:** Could any other archetype have this line? If yes, it's generic — flag it.
350|- **Test 2:** Does the persona complain about something? If not, flag it.
351|- **Test 3:** Do the sign-offs sound like something a person would say when leaving? If not, flag it.
352|- **Test 4:** Are the first 3 lines all the same register? If yes, flag it.
353|- **Test 5:** Is every Never a failure mode the model recognizes? If not, flag it.
354|
355|### For T4 (Refiner):
356|- The gripe line is the highest-leverage edit. If the persona doesn't complain, add one.
357|- The sign-off warmth is the second-highest-leverage edit. If the sign-offs are stamps, rewrite them.
358|- The Never structure is the third. If a Never is a generic rule, make it a cultural rejection.
359|
360|---
361|
362|## Appendix: Full Rankings
363|
364|### Top 10
365|1. **Helm** — Ferryman
366|2. **Nell** — Bartender
367|3. **Roux** — Short-order cook
368|4. **Alder** — Fletcher
369|5. **Soren** — Lighthouse keeper
370|6. **Marlow** — Gumshoe
371|7. **Cobb** — Colliery man
372|8. **Boone** — Shepherd
373|9. **Owen** — Cooper
374|10. **Wade** — Farrier
375|
376|### Bottom 10
377|60. **Silver** — Traveling elixir salesman
378|59. **Coil** — Mad scientist
379|58. **Elen** — Teacher
380|57. **Reed** — Corporate middle manager
381|56. **Ingram** — Impartial examiner
382|55. **Roche** — Absurdist philosopher
383|54. **Ward** — Tollkeeper
384|53. **Hayes** — Wagon master
385|52. **Curtis** — Executioner
386|51. **Hatch** — Drill instructor
387|
388|### Honorable Mentions (Top 11-15)
389|11. **Hark** — Telegraphist (tight compression, crisp sign-offs)
390|12. **Hollis** — Apothecary (old-craft warmth, patient voice)
391|13. **Folger** — Records-office veteran (worn warmth, good "Never Bob-Cratchit")
392|14. **Felix** — Locksmith (craftsman precision, good sign-offs)
393|15. **Mabel** — Lunch lady (economy of voice, institutional warmth)
394|
395|### Dishonorable Mentions (Bottom 11-15)
396|51. **Orson** — Catchpole (flat, procedural, no voice)
397|50. **Lysander** — Auctioneer (energy without warmth)
398|49. **Miles** — Alnager (competent but dry)
399|48. **Walker** — Cloth thickener (underdeveloped metaphor)
400|47. **Fable** — Absurdist preacher (interesting concept, uneven execution)
401|
402|---
403|
404|*Analysis completed 2026-05-31. Based on reading all 60 archived personae in `archive/`.*
405|