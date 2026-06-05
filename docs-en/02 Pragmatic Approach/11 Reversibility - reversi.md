<a id="reversi"></a>
## Topic 11. Reversibility

> Nothing is more dangerous than an idea if it's the only one you have.
>
> Emil-Auguste Chartier (Alain), Propos sur la religion, 1938

<a id="d24e4780"></a>
Engineers prefer simple, singular solutions to problems. Math tests that
allow you to proclaim with great confidence that $ x = 2 $ are
much more comfortable than fuzzy, warm essays about the myriad causes of
the French Revolution. Management tends to agree with the engineers:
singular, easy answers fit nicely on spreadsheets and project plans.

<a id="d24e4796"></a>
If only the real world would cooperate! Unfortunately, while
$ x $
is $ 2 $ today, it may need to
be $ 5 $
tomorrow,
and $ 3 $ next week. Nothing is forever—and if you
rely heavily on some fact, you can almost guarantee that it will
change.

<a id="d24e4813"></a>
There is always more than one way to implement something, and there is
usually more than one vendor available to provide a third-party product.
If you go into a project hampered by the myopic notion that there is
only one way to do it, you may be in for an unpleasant surprise. Many
project teams have their eyes forcibly opened as the future unfolds:

<a id="d24e4823"></a>
> “But you said we'd use database XYZ! We are 85% done coding the
> project, we can't change now!” the programmer
> protested. “Sorry, but our company decided to standardize on
> database PDQ instead—for all projects. It's out of my hands.
> We'll just have to recode. All of you will be working weekends
> until further notice.”

<a id="d24e4825"></a>
Changes don't have to be that Draconian, or even that immediate. But
as time goes by, and your project progresses, you may find yourself
stuck in an untenable position. With every critical decision, the
project team commits to a smaller target—a narrower version of
reality that has fewer options.

<a id="d24e4827"></a>
<a id="FNPTR-18"></a>
By the time many critical decisions have been made, the target becomes
so small that if it moves, or the wind changes direction, or a
butterfly in Tokyo flaps its wings, you miss.[[18]](<15 Estimating - learn_to_estimate.md#FOOTNOTE-18>) And you may miss by a huge
amount.

<a id="d24e4835"></a>
The problem is that critical decisions aren't easily reversible.

<a id="d24e4837"></a>
Once you decide to use this vendor's database, or that architectural
pattern, or a certain deployment model, you are committed to a course of
action that cannot be undone, except at great expense.

### Reversibility

<a id="d24e4846"></a>
Many of the topics in this book are geared to producing flexible,
adaptable software. By sticking to their recommendations—especially
the [DRY principle](<09 DRY - The Evils of Duplication - dry.md#dry>), [decoupling](<../05 Bend or Break/28 Decoupling - coupling.md#coupling>), and use of [external configuration](<../05 Bend or Break/32 Configuration - configuration.md#configuration>)—we don't have to make as many
critical, irreversible decisions. This is a good thing, because we don't
always make the best decisions the first time around. We commit to a
certain technology only to discover we can't hire enough people with the
necessary skills. We lock in a certain third-party vendor just before
they get bought out by their competitor. Requirements, users, and
hardware change faster than we can get the software developed.

<a id="d24e4857"></a>
Suppose you decide, early in the project, to use a relational database
from vendor A. Much later, during performance testing, you discover that
the database is simply too slow, but that the document database from
vendor B is faster. With most conventional projects, you'd be out of
luck. Most of the time, calls to third-party products are entangled
throughout the code. But if you really abstracted the idea of a
database out—to the point where it simply provides persistence as a
service—then you have the flexibility to change horses in midstream.

<a id="d24e4862"></a>
Similarly, suppose the project begins as a browser-based application,
but then, late in the game, marketing decides that what they really want
is a mobile app. How hard would that be for you? In an ideal world, it shouldn't impact you too much, at least on the server side. You'd be stripping out some HTML rendering
and replacing it with an API.

<a id="d24e4864"></a>
The mistake lies in assuming that any decision is cast in stone—and
in not preparing for the contingencies that might arise. Instead of
carving decisions in stone, think of them more as being written in the
sand at the beach. A big wave can come along and wipe them out at any
time.

**Tip 18: There Are No Final Decisions**

### Flexible Architecture

<a id="d24e4880"></a>
While many people try to keep their code flexible, you also need to
think about maintaining flexibility in the areas of architecture,
deployment, and vendor integration.

<a id="d24e4899"></a>
We're writing this in 2019. Since the turn of the century we've seen the following “best practice” server-side architectures:

- Big hunk of iron
- Federations of big iron
- Load-balanced clusters of commodity hardware
- Cloud-based virtual machines running applications
- Cloud-based virtual machines running services
- Containerized versions of the above
- Cloud-supported serverless applications
- And, inevitably, an apparent move back to big hunks of iron for some
  tasks

<a id="d24e4926"></a>
Go ahead and add the very latest and greatest fads to this list, and
then regard it with awe: it's a miracle that anything ever worked.

<a id="d24e4928"></a>
How can you plan for this kind of architectural volatility? You can't.

<a id="d24e4930"></a>
What you can do is make it easy to change. Hide third-party APIs behind
your own abstraction layers. Break your code into components: even if
you end up deploying them on a single massive server, this approach is a
lot easier than taking a monolithic application and splitting it. (We
have the scars to prove it.)

<a id="d24e4941"></a>
And, although this isn't particularly a reversibility issue, one final piece of advice.

**Tip 19: Forgo Following Fads**

<a id="d24e4953"></a>
No one knows what the future may hold, especially not us! So enable
your code to rock-n-roll: to “rock on'' when it can, to roll with the
punches when it must.

### Related Sections Include

- Topic 8, [*The Essence of Good Design*](<08 The Essence of Good Design - essence_of_design.md#essence_of_design>)
- Topic 10, [*Orthogonality*](<10 Orthogonality - orthogonality.md#orthogonality>)
- Topic 19, [*Version Control*](<../03 Basic Tools/19 Version Control - version_control.md#version_control>)
- Topic 28, [*Decoupling*](<../05 Bend or Break/28 Decoupling - coupling.md#coupling>)
- Topic 45, [*The Requirements Pit*](<../08 Before the Project/45 The Requirements Pit - requirements.md#requirements>)
- Topic 51, [*Pragmatic Starter Kit*](<../09 Pragmatic Projects/51 Pragmatic Starter Kit - starter_kit.md#starter_kit>)

### Challenges

<a id="d24e4985"></a>
<a id="d24e4994"></a>
<a id="d24e5002"></a>
<a id="d24e5004"></a>
<a id="d24e5006"></a>
- Time for a little quantum mechanics with Schrödinger's cat.

  Suppose you have a cat in a closed box, along with a radioactive
  particle. The particle has exactly a 50% chance of fissioning into
  two. If it does, the cat will be killed. If it doesn't, the cat will
  be okay. So, is the cat dead or alive? According to Schrödinger, the
  correct answer is both (at least while the box remains closed).
  Every time a subnuclear reaction takes place that has two possible
  outcomes, the universe is cloned. In one, the event occurred, in the
  other it didn't. The cat's alive in one universe, dead in another.
  Only when you open the box do you know which universe you are in.

  No wonder coding for the future is difficult.

  But think of code evolution along the same lines as a box full of
  Schrödinger's cats: every decision results in a different version of
  the future. How many possible futures can your code support? Which
  ones are more likely? How hard will it be to support them when the
  time comes?

  Dare you open the box?
