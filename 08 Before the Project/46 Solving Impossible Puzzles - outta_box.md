<a id="outta_box"></a>
## Topic 46. Solving Impossible Puzzles

> Gordius, the King of Phrygia, once tied a knot that no one could untie. It was said that whoever solved the riddle of the Gordian Knot would rule all of Asia. So along comes Alexander the Great, who chops the knot to bits with his sword. Just a little different interpretation of the requirements, that's all…. And he did end up ruling most of Asia.

<a id="d24e24962"></a>
Every now and again, you will find yourself embroiled in the middle of
a project when a really tough puzzle comes up: some piece of
engineering that you just can't get a handle on, or perhaps some bit
of code that is turning out to be much harder to write than you
thought. Maybe it looks impossible. But is it really as hard as it
seems?

<a id="d24e24978"></a>
Consider real-world puzzles—those devious little bits of wood, wrought
iron, or plastic that seem to turn up as Christmas presents or
at garage sales. All you have to do is remove the ring, or fit the
T-shaped pieces in the box, or whatever.

<a id="d24e24980"></a>
So you pull on the ring, or try to put the Ts in the box, and quickly
discover that the obvious solutions just don't work. The puzzle can't
be solved that way. But even though it's obvious, that doesn't stop
people from trying the same thing—over and over—thinking there
must be a way.

<a id="d24e24982"></a>
Of course, there isn't. The solution lies elsewhere. The secret to
solving the puzzle is to identify the real (not imagined) constraints,
and find a solution therein. Some constraints are absolute;
others are merely preconceived notions. Absolute constraints
must be honored, however distasteful or stupid they may appear
to be.

<a id="d24e25011"></a>
On the other hand, as Alexander proved, some apparent constraints may
not be real constraints at all. Many software problems can be just as
sneaky.

<a id="pg-fppose"></a>
### Degrees of Freedom

<a id="d24e25016"></a>
The popular buzz-phrase “thinking outside the box”
encourages us to recognize constraints that might not be applicable
and to ignore them. But this phrase isn't entirely accurate. If the
“box” is the boundary of constraints and conditions, then the trick
is to find the box, which may be considerably larger than you
think.

<a id="d24e25021"></a>
The key to solving puzzles is both to recognize the constraints placed on
you and to recognize the degrees of freedom you do
have, for in those you'll find your solution. This is why some puzzles
are so effective; you may dismiss potential solutions too readily.

<a id="d24e25026"></a>
For example, can you connect all of the dots in the following puzzle
and return to the starting point with just three straight
lines—without lifting your pen from the paper or retracing your
steps ([*Math Puzzles & Games* [Hol92]](<../A2 Exercise Answers/README.md#d6040e510>))?

<a id="d24e25032"></a>
![Four dots are shown.](https://panzhongxian.cn/images/the-pragmatic-programmer/four_dots_question.png)

<a id="d24e25033"></a>
You must challenge any preconceived notions and evaluate whether or
not they are real, hard-and-fast constraints.

<a id="d24e25035"></a>
It's not whether you think inside the box or outside the box. The
problem lies in finding the box—identifying the real constraints.

**Tip 81: Don't Think Outside the Box—Find the Box**

<a id="d24e25053"></a>
When faced with an intractable problem, enumerate all the
possible avenues you have before you. Don't dismiss anything, no
matter how unusable or stupid it sounds. Now go through the list and
explain why a certain path cannot be taken. Are you sure? Can you
prove it?

<a id="d24e25061"></a>
Consider the Trojan horse—a novel solution to an intractable
problem. How do you get troops into a walled city without being
discovered? You can bet that “through the front door” was initially
dismissed as suicide.

<a id="d24e25064"></a>
Categorize and prioritize your constraints. When woodworkers begin a
project, they cut the longest pieces first, then cut the smaller
pieces out of the remaining wood. In the same manner, we want to
identify the most restrictive constraints first, and fit the remaining
constraints within them.

<a id="d24e25066"></a>
By the way, a solution to the Four Posts puzzle is shown
[at the end of the book](<../A2 Exercise Answers/README.md#fourpost>).

### Get Out of Your Own Way!

<a id="d24e25074"></a>
Sometimes you will find yourself working on a problem that seems much
harder than you thought it should be. Maybe it feels like you're
going down the wrong path—that there must be an easier way than this!
Perhaps you are running late on the schedule now, or even despair of
ever getting the system to work because this particular problem is
“impossible.”

<a id="d24e25080"></a>
This is an ideal time to do something else for a while. Work on
something different. Go walk the dog. Sleep on it.

<a id="d24e25082"></a>
Your conscious brain is aware of the problem, but your conscious brain
is really pretty dumb (no offense). So it's time to give your real
brain, that amazing associative neural net that lurks below your
consciousness, some space. You'll be amazed how often the answer will
just pop into your head when you deliberately distract yourself.

<a id="d24e25084"></a>
<a id="FNPTR-72"></a>
If that sounds too mystical for you, it isn't. Psychology
Today[[72]](<48 The Essence of Agility - essence_of_agility.md#FOOTNOTE-72>)
reports:

<a id="d24e25094"></a>
> To put it plainly—people who were distracted did better on a complex
> problem-solving task than people who put in conscious effort.

<a id="d24e25096"></a>
If you're still not willing to drop the problem for a while, the next
best thing is probably finding someone to explain it to. Often, the
distraction of simply talking about it will lead you to enlightenment.

<a id="d24e25102"></a>
Have them ask you questions such as:

<a id="d24e25110"></a>
<a id="d24e25113"></a>
<a id="d24e25116"></a>
<a id="d24e25119"></a>
- Why are you solving this problem?
- What's the benefit of solving it?
- Are the problems you're having related to edge cases? Can you
  eliminate them?
- Is there a simpler, related problem you can solve?

<a id="d24e25121"></a>
This is another example of Rubber Ducking in practice.

### Fortune Favors the Prepared Mind

<a id="d24e25126"></a>
Louis Pasteur is reported to have said:

<a id="d24e25129"></a>
> Dans les champs de l'observation le hasard ne favorise que les esprits
> préparés.
> (When it comes to observation, fortune favors the prepared mind.)

<a id="d24e25135"></a>
That is true for problem solving, too. In order to have those eureka!
moments, your nonconscious brain needs to have plenty of raw material;
prior experiences that can contribute to an answer.

<a id="d24e25140"></a>
A great way to feed your brain is to give it feedback on what works and
what doesn't work as you do your daily job. And we describe a great way
to do that using an Engineering Daybook (Topic 22, [*Engineering Daybooks*](<../03 Basic Tools/22 Engineering Daybooks - daybook.md#daybook>)).

<a id="d24e25153"></a>
And always remember the advice on the cover of The Hitchhiker's Guide to
the Galaxy: DON'T PANIC.

### Related Sections Include

- Topic 5, [*Good-Enough Software*](<../01 Pragmatic Philosophy/05 Good-Enough Software - good_enough_sw.md#good_enough_sw>)
- Topic 37, [*Listen to Your Lizard Brain*](<../07 While Coding/37 Listen to Your Lizard Brain - listen_to_your_lizard_brain.md#listen_to_your_lizard_brain>)
- Topic 45, [*The Requirements Pit*](<45 The Requirements Pit - requirements.md#requirements>)
- Andy wrote an entire book about this kind of thing: [*Pragmatic Thinking and Learning: Refactor Your Wetware* [Hun08]](<../A2 Exercise Answers/README.md#d6040e541>).

### Challenges

<a id="d24e25185"></a>
<a id="d24e25192"></a>
- Take a hard look at whatever difficult problem you are embroiled
  in today. Can you cut the Gordian knot? Do you have to do it this
  way? Do you have to do it at all?
- Were you handed a set of constraints when you signed on to your
  current project? Are they all still applicable, and is the
  interpretation of them still valid?
