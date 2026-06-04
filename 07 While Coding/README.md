Source: https://panzhongxian.cn/en/the-pragmatic-programmer/7_while_you_are_coding.html

## Topics

- [Topic 37. Listen to Your Lizard Brain](<37 Listen to Your Lizard Brain - listen_to_your_lizard_brain.md>)
- [Topic 38. Programming by Coincidence](<38 Programming by Coincidence - coincidence.md>)
- [Topic 39. Algorithm Speed](<39 Algorithm Speed - algorithm_speed.md>)
- [Topic 40. Refactoring](<40 Refactoring - refactor.md>)
- [Topic 41. Test to Code](<41 Test to Code - test_to_build.md>)
- [Topic 42. Property-Based Testing](<42 Property-Based Testing - proptest.md>)
- [Topic 43. Stay Safe Out There](<43 Stay Safe Out There - safety.md>)
- [Topic 44. Naming Things](<44 Naming Things - naming.md>)

# Chapter 7 - While You Are Coding

<a id="coding"></a>

<a id="d24e19194"></a>
Conventional wisdom says that once a project is in the coding phase, the
work is mostly mechanical, transcribing the design into executable
statements. We think that this attitude is the single biggest reason that software projects fail, and many systems end up ugly, inefficient, poorly structured,
unmaintainable, or just plain wrong.

<a id="d24e19196"></a>
Coding is not mechanical. If it were, all the CASE tools that people
pinned their hopes on way back
in the early 1980s would have replaced programmers
long ago. There are decisions to be made every minute—decisions that
require careful thought and judgment if the resulting program is to
enjoy a long, accurate, and productive life.

<a id="d24e19202"></a>
Not all decisions are even conscious. You can better harness your instincts and nonconscious thoughts when you Topic 37, [*Listen to Your Lizard Brain*](<37 Listen to Your Lizard Brain - listen_to_your_lizard_brain.md#listen_to_your_lizard_brain>). We'll see how to listen more carefully and look at ways of actively responding to these sometimes niggling thoughts.

<a id="d24e19218"></a>
But listening to your instincts doesn't mean you can just fly on autopilot.
Developers who don't actively think about their code are programming by
coincidence—the code might work, but there's no particular reason why.
In Topic 38, [*Programming by Coincidence*](<38 Programming by Coincidence - coincidence.md#coincidence>), we advocate a more positive
involvement with the coding process.

<a id="d24e19236"></a>
While most of the code we write executes quickly, we occasionally
develop algorithms that have the potential to bog down even the fastest
processors. In Topic 39, [*Algorithm Speed*](<39 Algorithm Speed - algorithm_speed.md#algorithm_speed>), we discuss ways to
estimate the speed of code, and we give some tips on how to spot
potential problems before they happen.

<a id="d24e19254"></a>
Pragmatic Programmers think critically about all code, including our
own. We constantly see room for improvement in our programs and our
designs. In Topic 40, [*Refactoring*](<40 Refactoring - refactor.md#refactor>), we look at techniques that
help us fix up existing code continuously as we go.

<a id="d24e19267"></a>
Testing is not about finding bugs, it's about getting feedback on your code: aspects of design, the API, coupling, and so on. That means that the major benefits of testing happen when you think
about and write the tests, not just when you run them. We'll explore this idea in Topic 41, [*Test to Code*](<41 Test to Code - test_to_build.md#test_to_build>).

<a id="d24e19301"></a>
But of course when you test your own code, you might bring your own biases to the task. In Topic 42, [*Property-Based Testing*](<42 Property-Based Testing - proptest.md#proptest>) we'll see how to have the computer do some wide-ranging testing for you and how to handle the inevitable bugs that come up.

<a id="d24e19313"></a>
It's critical that you write code that is readable and easy to reason about. It's a harsh world out there, filled with bad actors who are actively trying to break into your system and cause harm. We'll discuss some very basic techniques and approaches to help you Topic 43, [*Stay Safe Out There*](<43 Stay Safe Out There - safety.md#safety>).

<a id="d24e19329"></a>
Finally, one of the hardest things in software development is Topic 44, [*Naming Things*](<44 Naming Things - naming.md#naming>). We have to name a lot of things, and in many ways the names we choose define the reality we create. You need to stay aware of any potential semantic drift while you are coding.

<a id="d24e19342"></a>
Most of us can drive a car largely on autopilot; we don't explicitly
command our foot to press a pedal, or our arm to turn the wheel—we
just think “slow down and turn right.” However, good, safe drivers are
constantly reviewing the situation, checking for potential problems, and
putting themselves into good positions in case the unexpected happens.
The same is true of coding—it may be largely routine, but keeping your
wits about you could well prevent a disaster.
