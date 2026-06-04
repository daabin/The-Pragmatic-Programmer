<a id="prototyping"></a>
## Topic 13. Prototypes and Post-it Notes

<a id="d24e5260"></a>
Many industries use prototypes to try out specific ideas;
prototyping is much cheaper than full-scale production. Car makers, for
example, may build many different prototypes of a new car design. Each
one is designed to test a specific aspect of the car—the aerodynamics,
styling, structural characteristics, and so on. Old school folks might
use a clay model for wind tunnel testing, maybe a balsa wood and duct
tape model will do for the art department, and so on. The less romantic
will do their modeling on a computer screen or in virtual reality,
reducing costs even further. In
this way, risky or uncertain elements can be tried out without
committing to building the real item.

<a id="d24e5271"></a>
We build software prototypes in the same fashion, and for the same
reasons—to analyze and expose risk, and to offer chances for
correction at a greatly reduced cost. Like the car makers, we can target
a prototype to test one or more specific aspects of a project.

<a id="d24e5277"></a>
We tend to think of prototypes as code-based, but they don't always have
to be. Like the car makers, we can build prototypes out of different
materials. Post-it notes are great for prototyping dynamic things such
as workflow and application logic. A user interface can be prototyped as
a drawing on a whiteboard, as a nonfunctional mock-up drawn with a paint
program, or with an interface builder.

<a id="d24e5279"></a>
Prototypes are designed to answer just a few questions, so they are much
cheaper and faster to develop than applications that go into production.
The code can ignore unimportant details—unimportant to you at the
moment, but probably very important to the user later on. If you are
prototyping a UI, for instance, you can get away with incorrect results
or data. On the other hand, if you're just investigating computational
or performance aspects, you can get away with a pretty poor UI, or
perhaps even no UI at all.

<a id="d24e5285"></a>
But if you find yourself in an environment where you
cannot give up the details, then you need to ask yourself
if you are really building a prototype at all. Perhaps a tracer bullet
style of development would be more appropriate in this case (see
Topic 12, [*Tracer Bullets*](<12 Tracer Bullets - tracer_bullets.md#tracer_bullets>)).

### Things to Prototype

<a id="d24e5304"></a>
What sorts of things might you choose to investigate with a prototype?
Anything that carries risk. Anything that hasn't been tried before, or
that is absolutely critical to the final system. Anything unproven,
experimental, or doubtful. Anything you aren't comfortable with. You can prototype:

- Architecture
- New functionality in an existing system
- Structure or contents of external data
- Third-party tools or components
- Performance issues
- User interface design

<a id="d24e5349"></a>
Prototyping is a learning experience. Its value lies not in the
code produced, but in the lessons learned. That's really the
point of prototyping.

**Tip 21: Prototype to Learn**

### How to Use Prototypes

<a id="d24e5364"></a>
When building a prototype, what details can you ignore?

<a id="d24e5371"></a>
<a id="d24e5379"></a>
<a id="d24e5387"></a>
<a id="d24e5395"></a>
Correctness
:   You may be able to use dummy data where
    appropriate.

Completeness
:   The prototype may function only in a very
    limited sense, perhaps with only one preselected piece of input
    data and one menu item.

Robustness
:   Error checking is likely to be incomplete or
    missing entirely. If you stray from the predefined path, the
    prototype may crash and burn in a glorious display of pyrotechnics.
    That's okay.

Style
:   Prototype
    code shouldn't have much in the way of comments or
    documentation (although you may produce reams of documentation as a result of
    your experience with the prototype).

<a id="d24e5411"></a>
Prototypes gloss over details, and focus in on specific
aspects of the system being considered, so you may want to implement
them using a high-level scripting language—higher than the rest
of the project (maybe a language such as Python or Ruby), as these
languages can get out of your way. You may choose to continue to develop
in the language used for the prototype, or you can switch; after all,
you're going to throw the prototype away anyway.

<a id="d24e5422"></a>
To prototype user interfaces, use
a tool that lets you focus on the appearance and/or
interactions without worrying about code or markup.

<a id="d24e5433"></a>
Scripting languages also work well as the “glue'' to combine low-level
pieces into new combinations. Using this approach, you can rapidly
assemble existing components into new configurations to see how things
work.

### Prototyping Architecture

<a id="d24e5438"></a>
Many prototypes are constructed to model the entire system under
consideration. As opposed to tracer bullets, none of the individual
modules in the prototype system need to be particularly functional. In
fact, you may not even need to code in order to prototype
architecture—you can prototype on a whiteboard, with Post-it notes or
index cards. What you are looking for is how the system hangs together
as a whole, again deferring details. Here are some specific areas you
may want to look for in the architectural prototype:

- Are the responsibilities of the major areas well defined
  and appropriate?
- Are the collaborations between major components well defined?
- Is coupling minimized?
- Can you identify potential sources of duplication?
- Are interface definitions and constraints acceptable?
- Does every module have an access path to the data it needs
  during execution? Does it have that access when it needs it?

<a id="d24e5508"></a>
This last item tends to generate the most surprises and the most
valuable results from the prototyping experience.

### How Not to Use Prototypes

<a id="d24e5516"></a>
Before you embark on any code-based prototyping, make sure that everyone
understands that you are writing disposable code. Prototypes can be
deceptively attractive to people who don't know that they are just
prototypes. You must make it very clear that this code is disposable,
incomplete, and unable to be completed.

<a id="d24e5525"></a>
It's easy to become misled by the apparent completeness of a
demonstrated prototype, and project sponsors or management may insist on
deploying the prototype (or its progeny) if you don't set the right
expectations. Remind them that you can build a great prototype of a new
car out of balsa wood and duct tape, but you wouldn't try to drive it in
rush-hour traffic!

<a id="d24e5527"></a>
If you feel there is a strong possibility in your environment or culture
that the purpose of prototype code may be misinterpreted, you may be
better off with the tracer bullet approach. You'll end up with a solid
framework on which to base future development.

<a id="d24e5538"></a>
Properly used prototypes can save you huge amounts of time,
money, and pain by identifying and correcting potential
problem spots early in the development cycle—the time when fixing
mistakes is both cheap and easy.

### Related Sections Include

- Topic 12, [*Tracer Bullets*](<12 Tracer Bullets - tracer_bullets.md#tracer_bullets>)
- Topic 14, [*Domain Languages*](<14 Domain Languages - domain_languages.md#domain_languages>)
- Topic 17, [*Shell Games*](<../03 Basic Tools/17 Shell Games - know_your_shell.md#know_your_shell>)
- Topic 27, [*Don't Outrun Your Headlights*](<../04 Pragmatic Paranoia/27 Don't Outrun Your Headlights - headlights.md#headlights>)
- Topic 37, [*Listen to Your Lizard Brain*](<../07 While Coding/37 Listen to Your Lizard Brain - listen_to_your_lizard_brain.md#listen_to_your_lizard_brain>)
- Topic 45, [*The Requirements Pit*](<../08 Before the Project/45 The Requirements Pit - requirements.md#requirements>)
- Topic 52, [*Delight Your Users*](<../09 Pragmatic Projects/52 Delight Your Users - delight.md#delight>)

### Exercises

<a id="exercise-3"></a>
**Exercise 3** ([possible answer](<../A2 Exercise Answers/README.md#answer-3>))

<a id="d24e5586"></a>
Marketing would like to sit down and brainstorm a few web page designs
with you. They are thinking of clickable image maps to take you to
other pages, and so on. But they can't decide on a model for the
image—maybe it's a car, or a phone, or a house. You have a list of
target pages and content; they'd like to see a few prototypes. Oh, by
the way, you have 15 minutes. What tools might you use?
