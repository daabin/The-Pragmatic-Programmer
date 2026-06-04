Source: https://panzhongxian.cn/en/the-pragmatic-programmer/2_a_pragmatic_approach.html#essence_of_design

<a id="essence_of_design"></a>
## Topic 8. The Essence of Good Design

<a id="d24e2670"></a>
The world is full of gurus and pundits, all eager to pass on their
hard-earned wisdom when it comes to How to Design Software. There are
acronyms, lists (which seem to favor five entries), patterns, diagrams,
videos, talks, and (the internet being the internet) probably a cool
series on the Law of Demeter explained using interpretive dance.

<a id="d24e2684"></a>
And we, your gentle authors, are guilty of this too. But we'd like to
make amends by explaining something that only became apparent to us
fairly recently. First, the general statement:

**Tip 14: Good Design Is Easier to Change Than Bad Design**

<a id="d24e2701"></a>
A thing is well designed if it adapts to the people who use it. For
code, that means it must adapt by changing.
So we believe in the ETC principle: Easier to Change. ETC. That's it.

<a id="d24e2709"></a>
As far as we can tell, every design principle out there is a special
case of ETC.

<a id="d24e2711"></a>
Why is decoupling good? Because by isolating concerns we make each
easier to change. ETC.

<a id="d24e2717"></a>
Why is the single responsibility principle useful? Because a change in
requirements is mirrored by a change in just one module. ETC.

<a id="d24e2726"></a>
Why is naming important? Because good names make code easier to read,
and you have to read it to change it. ETC!

### ETC Is a Value, Not a Rule

<a id="d24e2735"></a>
Values are things that help you make decisions: should I do this, or
that? When it comes to thinking about software, ETC is a guide, helping
you choose between paths. Just like all your other values, it should be
floating just behind your conscious thought, subtly nudging you in the
right direction.

<a id="d24e2744"></a>
But how do you make that happen? Our experience is that it requires some
initial conscious reinforcement. You may need to spend a week or so
deliberately asking yourself “did the thing I just did make the overall
system easier or harder to change?” Do it when you save a file. Do it
when you write a test. Do it when you fix a bug.

<a id="d24e2746"></a>
There's an implicit premise in ETC. It assumes that a person can tell
which of many paths will be easier to change in the future. Much of
the time, common sense will be correct, and you can make an educated
guess.

<a id="d24e2748"></a>
Sometimes, though, you won't have a clue. That's OK. In those cases, we
think you can do two things.

<a id="d24e2750"></a>
First, given that you're not sure what form change will take, you can
always fall back on the ultimate “easy to change” path: try to make what
you write replaceable. That way, whatever happens in the future, this
chunk of code won't be a roadblock. It seems extreme, but actually it's
what you should be doing all the time, anyway. It's really just thinking
about keeping code decoupled and cohesive.

<a id="d24e2756"></a>
Second, treat this as a way to develop instincts. Note the situation in
your engineering day book: the choices you have, and some guesses about
change. Leave a tag in the source. Then, later, when this code has to
change, you'll be able to look back and give yourself feedback. It might
help the next time you reach a similar fork in the road.

<a id="d24e2772"></a>
The rest of the sections in this chapter have specific ideas on design,
but all are motivated by this one principle.

### Related Sections Include

- Topic 9, [*DRY—The Evils of Duplication*](<09 DRY - The Evils of Duplication - dry.md#dry>)
- Topic 10, [*Orthogonality*](<10 Orthogonality - orthogonality.md#orthogonality>)
- Topic 11, [*Reversibility*](<11 Reversibility - reversi.md#reversi>)
- Topic 14, [*Domain Languages*](<14 Domain Languages - domain_languages.md#domain_languages>)
- Topic 28, [*Decoupling*](<../05 Bend or Break/28 Decoupling - coupling.md#coupling>)
- Topic 30, [*Transforming Programming*](<../05 Bend or Break/30 Transforming Programming - function_pipelines.md#function_pipelines>)
- Topic 31, [*Inheritance Tax*](<../05 Bend or Break/31 Inheritance Tax - inheritance_tax.md#inheritance_tax>)

### Challenges

<a id="d24e2805"></a>
<a id="d24e2822"></a>
<a id="d24e2833"></a>
<a id="FNPTR-13"></a>
- Think about a design principle you use regularly. Is it intended to
  make things easy-to-change?
- Also think about languages and programming paradigms (OO, FP,
  Reactive, and so on). Do any have either big positives or big
  negatives when it comes to helping you write ETC code? Do any have
  both?

  When coding, what can you do to eliminate the negatives and accentuate
  the positives?[[13]](<Topic 15. Estimating - learn_to_estimate.md#FOOTNOTE-13>)

<a id="FNPTR-14"></a>
- Many editors have support (either built-in or via extensions) to run
  commands when you save a file. Get your editor to popup an ETC?
  message every time you save[[14]](<Topic 15. Estimating - learn_to_estimate.md#FOOTNOTE-14>) and use it as a cue to think
  about the code you just wrote. Is it easy to change?
