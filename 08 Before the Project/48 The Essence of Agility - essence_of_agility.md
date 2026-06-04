Source: https://panzhongxian.cn/en/the-pragmatic-programmer/8_before_the_project.html#essence_of_agility

<a id="essence_of_agility"></a>
## Topic 48. The Essence of Agility

> You keep using that word, I do not think it means what you think it means.
>
> Inigo Montoya, The Princess Bride

<a id="d24e25436"></a>
Agile is an adjective: it's how you do something. You can be an agile
developer. You can be on a team that adopts agile practices, a team that
responds to change and setbacks with agility. Agility is your style, not
you.

**Tip 83: Agile Is Not a Noun; Agile Is How You Do Things**

<a id="d24e25456"></a>
<a id="FNPTR-73"></a>
As we write this, almost 20 years after the inception of the Manifesto
for Agile Software Development,[[73]](#FOOTNOTE-73) we see many, many developers
successfully applying its values. We see many fantastic teams who find
ways to take these values and use them to guide what they do, and how
they change what they do.

<a id="d24e25465"></a>
<a id="FNPTR-74"></a>
But we also see another side of agility. We see teams and companies
eager for off-the-shelf solutions: Agile-in-a-Box. And we see many
consultants and companies all too happy to sell them what they want. We
see companies adopting more layers of management, more formal reporting,
more specialized developers, and more fancy job titles which just mean
“someone with a clipboard and a stopwatch.”[[74]](#FOOTNOTE-74)

<a id="d24e25472"></a>
We feel that many people have lost sight of the true meaning of agility,
and we'd like to see folks return to the basics.

<a id="d24e25478"></a>
Remember the values from the manifesto:

<a id="d24e25483"></a>
> We are uncovering better ways of developing
> software by doing it and helping others do it.
> Through this work we have come to value:

<a id="d24e25516"></a>
<a id="d24e25521"></a>
<a id="d24e25526"></a>
<a id="d24e25531"></a>
> - **Individuals and interactions** over processes and tools
> - **Working software** over comprehensive documentation
> - **Customer collaboration** over contract negotiation
> - **Responding to change** over following a plan

<a id="d24e25537"></a>
> That is, while there is value in the items on
> the right, we value the items on the left more.

<a id="d24e25539"></a>
Anyone selling you something that increases the importance on things on
the right over things on the left clearly doesn't value the same things
that we and the other manifesto writers did.

<a id="d24e25543"></a>
And anyone selling you a solution-in-a-box hasn't read the introductory
statement. The values are motivated and informed by the continuous act
of uncovering better ways to produce software. This is not a static
document. It's suggestions for a generative process.

### There Can Never Be an Agile Process

<a id="d24e25548"></a>
In fact, whenever someone says “do this, and you'll be agile,” they are
wrong. By definition.

<a id="d24e25550"></a>
Because agility, both in the physical world and in software development,
is all about responding to change, responding to the unknowns you
encounter after you set out. A running gazelle doesn't go in a straight
line. A gymnast makes hundreds of corrections a second as they respond
to changes in their environment and minor errors in their foot
placement.

<a id="d24e25552"></a>
So it is with teams and individual developers. There is no single plan
you can follow when you develop software. Three of the four values tell
you that. They're all about gathering and responding to feedback.

<a id="d24e25558"></a>
The values don't tell you what to do. They tell you what to look for
when you decide for yourself what to do.

<a id="d24e25560"></a>
These decisions are always contextual: they depend on who you are, the
nature of your team, your application, your tooling, your company, your
customer, the outside world; an incredibly large number of factors, some
major and some trivial. No fixed, static plan can survive this
uncertainty.

### So What Do We Do?

<a id="d24e25565"></a>
No one can tell you what to do. But we think we can tell you something
about the spirit with which you do it. It all boils down to how you deal
with uncertainty. The manifesto suggests that you do this by gathering
and acting on feedback. So here's our recipe for working in an agile
way:

|  |
| --- |
|  |
| 1. Work out where you are. |
|  |
| 2. Make the smallest meaningful step towards where you want to be. |
|  |
| 3. Evaluate where you end up, and fix anything you broke. |
|  |

<a id="d24e25597"></a>
Repeat these steps until you're done. And use them recursively, at every
level of everything you do.

<a id="d24e25599"></a>
Sometimes even the most trivial-seeming decision becomes important when
you gather feedback.

<a id="d24e25603"></a>
<a id="d24e25611"></a>
<a id="d24e25625"></a>
“Now my code needs to get the account owner.

```
let user = accountOwner(accountID);
```

Hmmm… user is a useless name. I'll make it owner.

```
let owner = accountOwner(accountID);
```

But now that feels a little redundant. What am I actually trying to do
here? The story says that I'm sending this person an email, so I need to
find their email address. Maybe I don't need the whole account owner at
all.

```
let email = emailOfAccountOwner(accountID);
```

<a id="d24e25634"></a>
By applying the feedback loop at a really low level (the naming of a
variable) we've actually improved the design of the overall system,
reducing the coupling between this code and the code that deals with accounts.

<a id="d24e25645"></a>
The feedback loop also applies at the highest level of a project. Some
of our most successful work has happened when we started working on a
client's requirements, took a single step, and realized that what we
were about to do wasn't necessary, that the best solution didn't even
involve software.

<a id="d24e25647"></a>
This loop applies outside the scope of a single project. Teams should
apply it to review their process and how well it worked. A team that
doesn't continuously experiment with their process is not an agile
team.

### And This Drives Design

<a id="d24e25652"></a>
In Topic 8, [*The Essence of Good Design*](<../02 Pragmatic Approach/08 The Essence of Good Design - essence_of_design.md#essence_of_design>) we assert that the measure of design is
how easy the result of that design is to change: a good design produces something
that's easier to change than a bad design.

<a id="d24e25660"></a>
And this discussion about agility explains why that's the case.

<a id="d24e25665"></a>
You make a change, and discover you don't like it. Step 3 in our list
says we have to be able to fix what we break. To make our feedback loop
efficient, this fix has to be as painless as possible. If it isn't,
we'll be tempted to shrug it off and leave it unfixed. We talk about
this effect in Topic 3, [*Software Entropy*](<../01 Pragmatic Philosophy/03 Software Entropy - no_broken_windows.md#no_broken_windows>). To make this whole
agile thing work, we need to practice good design, because good design
makes things easy to change. And if it's easy to change, we can adjust,
at every level, without any hesitation.

<a id="d24e25669"></a>
That is agility.

### Related Sections Include

- Topic 27, [*Don't Outrun Your Headlights*](<../04 Pragmatic Paranoia/27 Don't Outrun Your Headlights - headlights.md#headlights>)
- Topic 40, [*Refactoring*](<../07 While Coding/40 Refactoring - refactor.md#refactor>)
- Topic 50, [*Coconuts Don't Cut It*](<../09 Pragmatic Projects/50 Coconuts Don't Cut It - do_what_works.md#do_what_works>)

### Challenges

<a id="d24e25688"></a>
The simple feedback loop isn't just for software. Think of other
decisions you've made recently. Could any of them have been improved by
thinking about how you might be able to undo them if things didn't take
you in the direction you were going? Can you think of ways you can
improve what you do by gathering and acting on feedback?

<a id="d24e24577"></a>
<a id="FOOTNOTE-70"></a>
<a id="d24e24647"></a>
<a id="FOOTNOTE-71"></a>
<a id="d24e25089"></a>
<a id="FOOTNOTE-72"></a>
<a id="d24e25461"></a>
<a id="FOOTNOTE-73"></a>
<a id="d24e25468"></a>
<a id="FOOTNOTE-74"></a>
[[70]](<Topic 45. The Requirements Pit - requirements.md#FNPTR-70>)Does a week
sound like a long time? It really isn't, particularly when you're
looking at processes in which management and workers occupy
different worlds. Management will give you one view of how
things operate, but
when you get down on the floor, you'll find a very different
reality—one that will take time to assimilate.

[[71]](<Topic 45. The Requirements Pit - requirements.md#FNPTR-71>)<https://www.wired.com/1999/01/eno/>

[[72]](<Topic 46. Solving Impossible Puzzles - outta_box.md#FNPTR-72>)<https://www.psychologytoday.com/us/blog/your-brain-work/201209/stop-trying-solve-problems>

[[73]](#FNPTR-73)<https://agilemanifesto.org>

[[74]](#FNPTR-74)For more on just how bad that approach can be, see [*The Tyranny of Metrics* [Mul18]](<../A2 Exercise Answers/README.md#d6040e818>).
