<a id="headlights"></a>
## Topic 27. Don't Outrun Your Headlights

> It's tough to make predictions, especially about the future.
>
> Lawrence "Yogi" Berra, after a Danish Proverb

<a id="d24e11526"></a>
It's late at night, dark, pouring rain. The two-seater whips around the tight curves of the twisty little mountain roads, barely holding the corners. A hairpin comes up and the car misses it, crashing though the skimpy guardrail and soaring to a fiery crash in the valley below. State troopers arrive on the scene, and the senior officer sadly shakes their head. “Must have outrun their headlights.”

<a id="d24e11545"></a>
Had the speeding two-seater been going faster than the speed of light? No, that speed limit is firmly fixed. What the officer referred to was the driver's ability to stop or steer in time in response to the headlight's illumination.

<a id="d24e11547"></a>
<a id="FNPTR-35"></a>
Headlights have a certain limited range, known as the throw distance.
Past that point, the light spread is too diffuse to be effective. In
addition, headlights only project in a straight line, and won't
illuminate anything off-axis, such as curves, hills, or dips in the
road. According to the National Highway Traffic Safety Administration,
the average distance illuminated by low-beam headlights is about
160 feet. Unfortunately, stopping distance at 40mph
is 189 feet, and at 70mph a whopping 464 feet.[[35]](#FOOTNOTE-35)
So indeed, it's
actually pretty easy to outrun your headlights.

<a id="d24e11557"></a>
In software development, our “headlights” are similarly limited. We can't see too far ahead into the future, and the further off-axis you look, the darker it gets. So Pragmatic Programmers have a firm rule:

**Tip 42: Take Small Steps—Always**

<a id="d24e11569"></a>
Always take small, deliberate steps, checking for feedback and adjusting before proceeding. Consider that the rate of feedback is your speed limit. You never take on a step or a task that's “too big.”

<a id="d24e11575"></a>
What do we mean exactly by feedback? Anything that independently confirms or disproves your action. For example:

- Results in a REPL provide feedback on your understanding of APIs and algorithms
- Unit tests provide feedback on your last code change
- User demo and conversation provide feedback on features and usability

<a id="d24e11622"></a>
What's a task that's too big? Any task that requires “fortune telling.” Just as the car headlights have limited throw, we can only see into the future perhaps one or two steps, maybe a few hours or days at most. Beyond that, you can quickly get past educated guess and into wild speculation. You might find yourself slipping into fortune telling when you have to:

- Estimate completion dates months in the future
- Plan a design for future maintenance or extendability
- Guess user's future needs
- Guess future tech availability

<a id="d24e11661"></a>
But, we hear you cry, aren't we supposed to design for future maintenance? Yes, but only to a point: only as far ahead as you can see. The more you have to predict what the future will look like, the more risk you incur that you'll be wrong. Instead of wasting effort designing for an uncertain future, you can always fall back on designing your code to be replaceable. Make it easy to throw out your code and replace it with something better suited. Making code replaceable will also help with cohesion, coupling, decoupling, and DRY, leading to a better design overall.

<a id="d24e11685"></a>
Even though you may feel confident of the future, there's always the chance of a black swan around the corner.

### Black Swans

<a id="d24e11690"></a>
In his book, [*The Black Swan: The Impact of the Highly Improbable* [Tal10]](<../A2 Exercise Answers/README.md#d6040e970>), Nassim Nicholas Taleb posits that all significant events in history have come from high-profile, hard-to-predict, and rare events that are beyond the realm of normal expectations. These outliers, while statistically rare, have disproportionate effects. In addition, our own cognitive biases tend to blind us to changes creeping up on the edges of our work (see Topic 4, [*Stone Soup and Boiled Frogs*](<../01 Pragmatic Philosophy/04 Stone Soup and Boiled Frogs - stone_soup.md#stone_soup>)).

<a id="d24e11709"></a>
<a id="FNPTR-36"></a>
Around the time of the first edition of The Pragmatic Programmer,
debate raged in computer magazines and online forums over the burning
question: “Who would win the desktop GUI wars, Motif or
OpenLook?”[[36]](#FOOTNOTE-36) It was the wrong question. Odds are you've probably never
heard of these technologies as neither “won” and the browser-centric
web quickly dominated the landscape.

**Tip 43: Avoid Fortune-Telling**

<a id="d24e11734"></a>
Much of the time, tomorrow looks a lot like today. But don't count on it.

### Related Sections Include

- Topic 12, [*Tracer Bullets*](<../02 Pragmatic Approach/12 Tracer Bullets - tracer_bullets.md#tracer_bullets>)
- Topic 13, [*Prototypes and Post-it Notes*](<../02 Pragmatic Approach/13 Prototypes and Post-it Notes - prototyping.md#prototyping>)
- Topic 40, [*Refactoring*](<../07 While Coding/40 Refactoring - refactor.md#refactor>)
- Topic 41, [*Test to Code*](<../07 While Coding/41 Test to Code - test_to_build.md#test_to_build>)
- Topic 48, [*The Essence of Agility*](<../08 Before the Project/48 The Essence of Agility - essence_of_agility.md#essence_of_agility>)
- Topic 50, [*Coconuts Don't Cut It*](<../09 Pragmatic Projects/50 Coconuts Don't Cut It - do_what_works.md#do_what_works>)

<a id="d24e9114"></a>
<a id="FOOTNOTE-30"></a>
<a id="d24e10251"></a>
<a id="FOOTNOTE-31"></a>
<a id="d24e10431"></a>
<a id="FOOTNOTE-32"></a>
<a id="d24e10742"></a>
<a id="FOOTNOTE-33"></a>
<a id="d24e10955"></a>
<a id="FOOTNOTE-34"></a>
<a id="d24e11553"></a>
<a id="FOOTNOTE-35"></a>
<a id="d24e11715"></a>
<a id="FOOTNOTE-36"></a>
[[30]](<23 Design by Contract - dbc.md#FNPTR-30>)Based in part on earlier work by Dijkstra, Floyd, Hoare, Wirth, and others.

[[31]](<25 Assertive Programming - assertions.md#FNPTR-31>)In C and C++ these are usually implemented as macros. In Java,
assertions are disabled by default. Invoke the Java VM with the
–enableassertions flag to enable them, and leave them enabled.

[[32]](<25 Assertive Programming - assertions.md#FNPTR-32>)<http://www.eps.mcgill.ca/jargon/jargon.html#heisenbug>

[[33]](<26 How to Balance Resources - balance_resources.md#FNPTR-33>)For a discussion of the dangers of coupled code, see Topic 28, [*Decoupling*](<../05 Bend or Break/28 Decoupling - coupling.md#coupling>).

[[34]](<26 How to Balance Resources - balance_resources.md#FNPTR-34>)See the tip [here](<../05 Bend or Break/30 Transforming Programming - function_pipelines.md#pg-donthoard>).

[[35]](#FNPTR-35)Per the NHTSA, Stopping Distance = Reaction Distance +
Braking Distance, assuming an average reaction time of
1.5s
and deceleration of 17.02ft/s².

[[36]](#FNPTR-36)Motif and OpenLook were GUI
standards for X-Window based Unix workstations.
