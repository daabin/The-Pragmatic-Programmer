Source: https://panzhongxian.cn/en/the-pragmatic-programmer/7_while_you_are_coding.html#refactor

<a id="refactor"></a>
## Topic 40. Refactoring

> Change and decay in all around I see...
>
> H. F. Lyte, Abide With Me

<a id="d24e20835"></a>
As a program evolves, it will become necessary to rethink earlier
decisions and rework portions of the code. This process is perfectly natural.
Code needs to evolve; it's not a static thing.

<a id="d24e20851"></a>
<a id="FNPTR-55"></a>
Unfortunately, the most common metaphor for software development is
building construction. Bertrand Meyer's classic work
[*Object-Oriented Software Construction* [Mey97]](<../A2 Exercise Answers/README.md#d6040e783>) uses the term
“Software Construction,” and even your humble authors edited the
Software Construction column for IEEE Software in the early 2000s.[[55]](<Topic 44. Naming Things - naming.md#FOOTNOTE-55>)

<a id="d24e20870"></a>
But using construction as the
guiding metaphor implies the following steps:

<a id="d24e20874"></a>
<a id="d24e20877"></a>
<a id="d24e20880"></a>
1. An architect draws up blueprints.
2. Contractors dig the foundation, build the superstructure, wire and
   plumb, and apply finishing touches.
3. The tenants move in and live happily ever after, calling building
   maintenance to fix any problems.

<a id="d24e20882"></a>
Well, software doesn't quite work that way. Rather than construction,
software is more like gardening—it
is more organic than
concrete. You plant many things in a garden according to an initial
plan and conditions. Some thrive, others are destined to end up as
compost. You may move plantings relative to each other to take
advantage of the interplay of light and shadow, wind and rain.
Overgrown plants get split or pruned, and colors that clash may get moved
to more aesthetically pleasing locations. You pull weeds, and
you fertilize plantings that are in need of some extra help. You
constantly monitor the health of the garden, and make adjustments
(to the soil, the plants, the layout) as needed.

<a id="d24e20889"></a>
Business people are comfortable with the metaphor of building
construction: it is more scientific than gardening, it's repeatable,
there's a rigid reporting hierarchy for management, and so on.
But we're not building skyscrapers—we aren't as constrained by the
boundaries of physics and the real world.

<a id="d24e20891"></a>
The gardening metaphor is much closer to the realities of software
development. Perhaps a certain routine has grown too large, or is
trying to accomplish too much—it needs to be split into two.
Things that don't work out as planned need to be weeded or pruned.

<a id="d24e20893"></a>
Rewriting, reworking, and re-architecting code is collectively known
as restructuring. But there's a subset of that activity that has become practiced as refactoring.

<a id="d24e20903"></a>
[*Refactoring* [Fow19]](<../A2 Exercise Answers/README.md#d6040e418>) is defined by Martin Fowler as a:

<a id="d24e20917"></a>
> disciplined technique for restructuring an existing body of code,
> altering its internal structure without changing its external
> behavior.

<a id="d24e20919"></a>
The critical parts of this definition are that:

<a id="d24e20923"></a>
<a id="d24e20926"></a>
1. The activity is disciplined, not a free-for-all
2. External behavior does not change; this is not the time to add features

<a id="d24e20928"></a>
Refactoring is not intended to be a special, high-ceremony, once-in-a-while activity, like plowing under the whole garden in order to replant. Instead, refactoring is a day-to-day activity, taking low-risk small steps, more like weeding and raking. Instead of a free-for-all, wholesale rewrite of the codebase, it's a targeted, precision approach to help keep the code easy to change.

<a id="d24e20934"></a>
In order to guarantee that the external behavior hasn't changed, you need good, automated unit testing that validates the behavior of the code.

### When Should You Refactor?

<a id="d24e20939"></a>
You refactor when you've learned something; when you understand something better than you did last year, yesterday, or even just ten minutes ago.

<a id="d24e20945"></a>
Perhaps you've come across a stumbling block because the code doesn't quite
fit anymore, or you notice two things that should really be merged, or
anything else at all strikes you as being “wrong,” don't
hesitate to change it. There's no time like the present. Any
number of things may cause code to qualify for
refactoring:

<a id="d24e20954"></a>
<a id="d24e20968"></a>
<a id="d24e20980"></a>
<a id="d24e20989"></a>
<a id="d24e20998"></a>
<a id="d24e21008"></a>
Duplication
:   You've discovered a violation of the DRY
    principle.

Nonorthogonal design
:   You've discovered something that
    could be made more orthogonal.

Outdated knowledge
:   Things change, requirements drift, and your
    knowledge of the problem increases. Code needs to keep up.

Usage
:   As the system gets used by real people under real circumstances,
    you realize some features are now more important than previously
    thought, and “must have” features perhaps weren't.

Performance
:   You need to move functionality from one area of
    the system to another to improve performance.

The Tests Pass
:   Yes. Seriously. We did say that refactoring should be a small scale
    activity, backed up by good tests. So when you've added a small amount
    of code, and that one extra test passes, you now have a great opportunity
    to dive in and tidy up what you just wrote.

<a id="d24e21014"></a>
Refactoring your code—moving functionality around and updating
earlier decisions—is really an exercise in pain management.
Let's face it, changing source code around can be pretty painful:
it was working, maybe it's better to leave well enough alone. Many
developers are reluctant to go in and re-open a piece of code just because it
isn't quite right.

#### Real-World Complications

<a id="d24e21022"></a>
So you go to your teammates or client and say, “This code works, but I
need another week to completely refactor it.”

<a id="d24e21024"></a>
We can't print their reply.

<a id="d24e21026"></a>
Time pressure
is often used as an excuse for not refactoring. But
this excuse just doesn't hold up: fail to refactor now, and there'll be
a far greater time investment to fix the problem down the road—when
there are more dependencies to reckon with. Will there be more time
available then? Nope.

<a id="d24e21042"></a>
You might want to explain this principle to others by using a
medical analogy: think of the code that needs refactoring as
“a growth.” Removing it requires invasive surgery. You can go in
now, and take it out while it is still small. Or, you could wait
while it grows and spreads—but removing it then will be both more
expensive and more dangerous. Wait even longer, and you may lose the
patient entirely.

**Tip 65: Refactor Early, Refactor Often**

<a id="d24e21050"></a>
Collateral damage in code can be just as deadly over time (see Topic 3, [*Software Entropy*](<../01 Pragmatic Philosophy/03 Software Entropy - no_broken_windows.md#no_broken_windows>)). Refactoring, as with most things, is easier to do while the issues are small, as an ongoing activity while coding. You shouldn't need “a week to refactor” a piece of code—that's a full-on rewrite. If that level of disruption is necessary, then you might well not be able to do it immediately. Instead, make sure that it gets placed on the
schedule. Make sure that users of the affected code know that
it is scheduled to be rewritten and how this might affect them.

### How Do You Refactor?

<a id="d24e21069"></a>
Refactoring started out in the Smalltalk
community, and had just started to gain a wider
audience when we wrote the first edition of this book, probably thanks to the
first major book on refactoring
([*Refactoring: Improving the Design of Existing Code* [Fow19]](<../A2 Exercise Answers/README.md#d6040e418>), now in its second edition).

<a id="d24e21078"></a>
At its heart, refactoring is redesign.
Anything that you or others on
your team designed can be redesigned in light of new facts, deeper
understandings, changing requirements, and so on. But if you proceed
to rip up vast quantities of code with wild abandon, you may find
yourself in a worse position than when you started.

<a id="d24e21089"></a>
<a id="FNPTR-56"></a>
Clearly, refactoring is an activity that needs to be undertaken
slowly, deliberately, and carefully. Martin Fowler
offers the
following simple tips on how to refactor without doing more harm than
good:[[56]](<Topic 44. Naming Things - naming.md#FOOTNOTE-56>)

<a id="d24e21100"></a>
<a id="d24e21103"></a>
<a id="d24e21110"></a>
<a id="FNPTR-57"></a>
1. Don't try to refactor and add functionality at the same time.
2. Make sure you have good tests before you begin refactoring. Run the
   tests as often as possible. That way you will know quickly if your
   changes have broken anything.
3. Take short, deliberate steps: move a field from one class to another,
   split a method, rename a variable. Refactoring often
   involves making many localized changes that result in a larger-scale
   change. If you keep your steps small, and test after each step, you
   will avoid prolonged debugging.[[57]](<Topic 44. Naming Things - naming.md#FOOTNOTE-57>)

<a id="d24e21149"></a>
<a id="d24e21166"></a>
Automatic Refactoring

Back in the first edition we noted that, “this technology has yet
to appear outside of
the Smalltalk world, but this is likely to change….” And indeed, it did, as automatic refactoring is available in many IDEs and for most mainstream languages.

These IDEs can rename variables and methods, split a long routine
into smaller ones, automatically propagating the required changes, drag and drop to assist you in moving code, and so on.

<a id="d24e21168"></a>
We'll talk more about testing at this level in Topic 41, [*Test to Code*](<41 Test to Code - test_to_build.md#test_to_build>),
and larger-scale testing in [*Ruthless and Continuous Testing*](<../09 Pragmatic Projects/51 Pragmatic Starter Kit - starter_kit.md#testing>),
but Mr. Fowler's point of
maintaining good regression tests is the key to refactoring safely.

<a id="d24e21174"></a>
If you have to go beyond refactoring and end up changing external behavior or interfaces, then it can help to deliberately break the build:
old clients of this
code should fail to compile. That way you'll know what needs updating.
Next time you see a piece of code that isn't quite as it should be,
fix it. Manage the pain: if it
hurts now, but is going to hurt even more later, you might as well get
it over with. Remember the lessons of Topic 3, [*Software Entropy*](<../01 Pragmatic Philosophy/03 Software Entropy - no_broken_windows.md#no_broken_windows>): don't live with broken windows.

### Related Sections Include

- Topic 3, [*Software Entropy*](<../01 Pragmatic Philosophy/03 Software Entropy - no_broken_windows.md#no_broken_windows>)
- Topic 9, [*DRY—The Evils of Duplication*](<../02 Pragmatic Approach/09 DRY - The Evils of Duplication - dry.md#dry>)
- Topic 12, [*Tracer Bullets*](<../02 Pragmatic Approach/12 Tracer Bullets - tracer_bullets.md#tracer_bullets>)
- Topic 27, [*Don't Outrun Your Headlights*](<../04 Pragmatic Paranoia/27 Don't Outrun Your Headlights - headlights.md#headlights>)
- Topic 44, [*Naming Things*](<44 Naming Things - naming.md#naming>)
- Topic 48, [*The Essence of Agility*](<../08 Before the Project/48 The Essence of Agility - essence_of_agility.md#essence_of_agility>)
