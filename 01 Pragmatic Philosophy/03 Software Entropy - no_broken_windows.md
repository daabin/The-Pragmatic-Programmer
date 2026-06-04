<a id="no_broken_windows"></a>
## Topic 3. Software Entropy

<a id="d24e1065"></a>
While software development is immune from almost all physical laws,
the inexorable increase in
entropy hits us hard. Entropy is a term from physics
that refers to the amount of “disorder” in a system. Unfortunately,
the laws of thermodynamics guarantee that the entropy in the universe
tends toward a maximum. When disorder increases in software,
we call it “software rot.” Some folks might call it by the more
optimistic term, “technical debt,” with the implied notion that they'll
pay it back someday. They probably won't.

<a id="d24e1082"></a>
Whatever the name, though, both debt and rot can spread uncontrollably.

<a id="d24e1084"></a>
There are many factors that can contribute to software rot. The most
important one seems to be the psychology, or culture, at work on a
project. Even if you are a team of one, your project's psychology can
be a very delicate thing. Despite the best-laid plans and the best
people, a project can still experience ruin and decay during its
lifetime. Yet there are other projects that, despite enormous
difficulties and constant setbacks, successfully fight nature's
tendency toward disorder and manage to come out pretty well.

<a id="d24e1086"></a>
What makes the difference?

<a id="d24e1088"></a>
<a id="FNPTR-5"></a>
In inner cities, some buildings are beautiful and clean, while others
are rotting hulks. Why? Researchers in the field of crime and urban
decay discovered a fascinating trigger mechanism, one that very
quickly turns a clean, intact, inhabited building into a smashed and
abandoned derelict.[[5]](<07 Communicate - communicate.md#FOOTNOTE-5>)

<a id="d24e1094"></a>
A broken window.

<a id="d24e1096"></a>
One broken window, left unrepaired for any substantial length of time,
instills in the inhabitants of the building a sense of abandonment—a
sense that the powers that be don't care about the building. So
another window gets broken. People start littering. Graffiti appears.
Serious structural damage begins. In a relatively short span of time,
the building becomes damaged beyond the owner's desire to fix it, and
the sense of abandonment becomes reality.

<a id="d24e1098"></a>
<a id="FNPTR-6"></a>
Why would that make a difference? Psychologists have done studies[[6]](<07 Communicate - communicate.md#FOOTNOTE-6>)
that show hopelessness can be contagious. Think of the flu virus in close quarters. Ignoring a clearly broken situation reinforces the ideas that perhaps nothing can be fixed, that no one cares, all is doomed; all negative thoughts which can spread among team members, creating a vicious spiral.

**Tip 5: Don't Live with Broken Windows**

<a id="d24e1119"></a>
Don't leave “broken windows'' (bad designs, wrong decisions, or poor
code) unrepaired. Fix each one as soon as it is discovered. If there
is insufficient time to fix it properly, then board it
up. Perhaps you can comment out the offending code, or display a
“Not Implemented” message, or substitute dummy data instead. Take
some action to prevent further damage and to show that you're on top
of the situation.

<a id="d24e1127"></a>
We've seen clean, functional systems deteriorate pretty quickly once
windows start breaking. There are other factors that can contribute to
software rot, and we'll touch on some of them elsewhere, but neglect
accelerates the rot faster than any other factor.

<a id="d24e1132"></a>
You may be thinking that no one has the time to go around cleaning up
all the broken glass of a project. If so,
then you'd better plan on getting a dumpster, or moving to another
neighborhood. Don't let entropy win.

### First, Do No Harm

<a id="d24e1137"></a>
Andy once had an acquaintance who was obscenely rich. His
house was immaculate, loaded with priceless antiques, objets
d'art, and so on. One day, a tapestry that was hanging a little too
close to a fireplace caught on fire. The fire department
rushed in to save the day—and his house. But before they dragged their
big, dirty hoses into the house, they stopped—with the fire
raging—to roll out a mat between the front door and the source of the
fire.

<a id="d24e1149"></a>
They didn't want to mess up the carpet.

<a id="d24e1151"></a>
Now that sounds pretty extreme. Surely the fire department's first
priority is to put out the fire, collateral damage be damned. But they
clearly had assessed the situation, were confident of their ability to
manage the fire, and were careful not to inflict unnecessary damage to
the property. That's the way it must be with software: don't cause
collateral damage just because there's a crisis of some sort. One broken
window is one too many.

<a id="d24e1153"></a>
One broken window—a badly designed piece of code, a poor
management decision that the team must live with for the duration of
the project—is all it takes to start the decline. If you find
yourself working on a project with quite a few broken windows, it's
all too easy to slip into the mindset of “All the rest of this code
is crap, I'll just follow suit.” It doesn't matter if the project has
been fine up to this point. In the original experiment leading to the
“Broken Window Theory,” an abandoned car sat for a week untouched.
But once a single window was broken, the car was stripped and turned
upside down within hours.

<a id="d24e1158"></a>
By the same token, if you find yourself on a project where
the code is pristinely beautiful—cleanly written, well designed, and
elegant—you will likely take extra special care not to mess it up,
just like the firefighters. Even if there's a fire raging (deadline,
release date, trade show demo, etc.), you don't want to be the first
one to make a mess and inflict additional damage.

<a id="d24e1163"></a>
Just tell yourself, “No broken windows.”

### Related Sections Include

- Topic 10, [*Orthogonality*](<../02 Pragmatic Approach/10 Orthogonality - orthogonality.md#orthogonality>)
- Topic 40, [*Refactoring*](<../07 While Coding/40 Refactoring - refactor.md#refactor>)
- Topic 44, [*Naming Things*](<../07 While Coding/44 Naming Things - naming.md#naming>)

### Challenges

<a id="d24e1183"></a>
<a id="d24e1205"></a>
- Help strengthen your team by surveying your project
  neighborhood. Choose two or three broken windows and
  discuss with your colleagues what the problems are and what could be
  done to fix them.
- Can you tell when a window first gets broken? What is your
  reaction? If it was the result of someone else's decision, or a
  management edict, what can you do about it?
