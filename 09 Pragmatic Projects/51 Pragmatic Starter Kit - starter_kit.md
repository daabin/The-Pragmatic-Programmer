Source: https://panzhongxian.cn/en/the-pragmatic-programmer/9_pragmatic_projects.html#starter_kit

<a id="starter_kit"></a>
## Topic 51. Pragmatic Starter Kit

> Civilization advances by extending the number of important operations we can perform without thinking.
>
> Alfred North Whitehead

<a id="d24e26649"></a>
Back when cars were a novelty, the instructions for starting a
Model-T Ford were more than two pages long. With modern cars, you just
push a button—the starting procedure is automatic and foolproof. A
person following a list of instructions might flood the engine, but the
automatic starter won't.

<a id="d24e26663"></a>
Although software development is still an industry at the Model-T stage,
we can't afford to go through two pages of instructions again and again
for some common operation. Whether it is the build and release
procedure, testing, project paperwork, or any other recurring task on
the project, it has to be automatic and repeatable on any capable
machine.

<a id="d24e26665"></a>
In addition, we want to ensure consistency and repeatability on the
project. Manual procedures leave consistency up to chance;
repeatability isn't guaranteed, especially if aspects of the procedure
are open to interpretation by different people.

<a id="d24e26667"></a>
After we wrote the first edition of The Pragmatic Programmer, we wanted to create more books to help teams develop software. We figured we should start at the beginning: what are the most basic, most important elements that every team needs regardless of methodology, language, or technology stack. And so the idea of the Pragmatic Starter Kit was born, covering these three critical and interrelated topics:

- Version Control
- Regression Testing
- Full Automation

<a id="d24e26718"></a>
These are the three legs that support every project. Here's how.

### Drive with Version Control

<a id="d24e26723"></a>
As we said in Topic 19, [*Version Control*](<../03 Basic Tools/19 Version Control - version_control.md#version_control>), you want to keep everything needed to build your project under version control. That idea becomes even more important in the context of the project itself.

<a id="d24e26727"></a>
<a id="FNPTR-80"></a>
First, it allows build machines to be ephemeral. Instead of one hallowed, creaky machine in the corner of the office that everyone is afraid to touch,[[80]](<../10 Postface/README.md#FOOTNOTE-80>) build machines and/or clusters are created on demand as spot instances in the cloud. Deployment configuration is under version control as well, so releasing to production can be handled automatically.

<a id="d24e26745"></a>
And that's the important part: at the project level, version control drives the build and release process.

**Tip 89: Use Version Control to Drive Builds, Tests, and Releases**

<a id="d24e26776"></a>
That is, build, test, and deployment are triggered via commits or pushes to version control, and built in a container in the cloud. Release to staging or production is specified by using a tag in your version control system. Releases then become a much more low-ceremony part of every day life—true continuous delivery, not tied to any one build machine or developer's machine.

<a id="testing"></a>
### Ruthless and Continuous Testing

<a id="d24e26788"></a>
Many developers test gently, subconsciously knowing where the code will break and avoiding the weak spots. Pragmatic Programmers are different. We are driven to find our bugs now, so we don't have to endure the shame of others finding our bugs later.

<a id="d24e26805"></a>
Finding bugs is somewhat like fishing with a net. We use fine, small nets (unit tests) to catch the minnows, and big, coarse nets (integration tests) to catch the killer sharks. Sometimes the fish manage to escape, so we patch any holes that we find, in hopes of catching more and more slippery defects that are swimming about in our project pool.

**Tip 90: Test Early, Test Often, Test Automatically**

<a id="d24e26835"></a>
We want to start testing as soon as we have code. Those tiny minnows
have a nasty habit of becoming giant, man-eating sharks pretty fast,
and catching a shark is quite a bit harder. So we write unit tests. A lot of unit tests.

<a id="d24e26837"></a>
In fact, a good project may well have more test code than
production code. The time it takes to produce this test code is
worth the effort. It ends up being much cheaper in the long run, and
you actually stand a chance of producing a product with close to zero
defects.

<a id="d24e26842"></a>
Additionally, knowing that you've passed the test gives you a high
degree of confidence that a piece of code is “done.''

**Tip 91: Coding Ain't Done 'Til All the Tests Run**

<a id="d24e26850"></a>
The automatic build runs all available tests. It's important to aim to “test for real,” in other words, the test environment should match the production environment closely. Any gaps are where bugs breed.

<a id="d24e26866"></a>
The build may cover several major types of software testing:
unit testing;
integration testing;
validation and verification; and
performance testing.

<a id="d24e26885"></a>
This list is by no means complete, and some specialized projects will
require various other types of testing as well. But it gives us a
good starting point.

#### Unit Testing

<a id="d24e26891"></a>
A unit test is code that exercises a module. We covered this in Topic 41, [*Test to Code*](<../07 While Coding/41 Test to Code - test_to_build.md#test_to_build>). Unit testing is the
foundation of all the other forms of testing that we'll discuss in
this section. If the parts don't work by themselves, they probably
won't work well together. All of the modules you are using
must pass their own unit tests before you can proceed.

<a id="d24e26902"></a>
Once all of the pertinent modules have passed their individual tests,
you're ready for the next stage. You need to test how all the modules
use and interact with each other throughout the system.

#### Integration Testing

<a id="d24e26907"></a>
Integration testing shows that the major subsystems that make
up the project work and play well with each other. With good
contracts in place and well tested, any integration issues can be
detected easily. Otherwise, integration becomes a fertile breeding
ground for bugs. In fact, it is often the single largest source of
bugs in the system.

<a id="d24e26919"></a>
Integration testing is really just an extension of the unit testing
we've described—you're just testing how entire subsystems honor
their contracts.

#### Validation and Verification

<a id="d24e26924"></a>
As soon as you have an executable user interface or prototype, you need to
answer an all-important question: the users told you what they wanted,
but is it what they need?

<a id="d24e26933"></a>
Does it meet the functional requirements of the system? This, too,
needs to be tested. A bug-free system that answers the wrong question
isn't very useful. Be conscious of end-user access patterns and how
they differ from developer test data (for an example, see the story
about brush strokes [here](<../03 Basic Tools/20 Debugging - debug.md#stroke>)).

#### Performance Testing

<a id="d24e26954"></a>
Performance or stress testing may be
important aspects of the project as well.

<a id="d24e26978"></a>
Ask yourself if the software meets the performance requirements under
real-world conditions—with the expected number of users, or
connections, or transactions per second. Is it scalable?

<a id="d24e26980"></a>
For some applications, you may need specialized testing hardware or
software to simulate the load realistically.

#### Testing the Tests

<a id="d24e26985"></a>
Because we can't write perfect software, it follows that we can't write
perfect test software either. We need to test the tests.

<a id="d24e26991"></a>
Think of our set of test suites as an elaborate security system,
designed to sound the alarm when a bug shows up. How better to test a
security system than to try to break in?

<a id="d24e26993"></a>
After you have written a test to detect a particular bug, cause
the bug deliberately and make sure the test complains. This ensures
that the test will catch the bug if it happens for real.

**Tip 92: Use Saboteurs to Test Your Testing**

<a id="d24e27006"></a>
<a id="FNPTR-81"></a>
If you are really serious about testing, take a separate branch of the source tree, introduce bugs on purpose, and verify that the tests will catch them. At a higher level, you can use something like Netflix's Chaos Monkey[[81]](<../10 Postface/README.md#FOOTNOTE-81>) to disrupt (i.e., “kill”) services and test your application's resilience.

<a id="d24e27023"></a>
When writing tests, make sure that alarms sound when they should.

#### Testing Thoroughly

<a id="d24e27028"></a>
Once you are confident that your tests are correct, and are finding
bugs you create, how do you know if you have tested the code base
thoroughly enough?

<a id="d24e27037"></a>
<a id="FNPTR-82"></a>
The short answer is “you don't,'' and you never will. You might look to
try coverage analysis tools that watch your code during testing and
keep track of which lines of code have been executed and which haven't.
These tools help give you a general feel for how comprehensive your
testing is, but don't expect to see 100% coverage.[[82]](<../10 Postface/README.md#FOOTNOTE-82>)

<a id="d24e27049"></a>
Even if you do happen to hit every line of code, that's not
the whole picture. What is important is the number of states
that your program may have. States are not equivalent to lines of
code. For instance, suppose you have a function that takes two
integers, each of which can be a number from 0 to 999:

```
int test(int a, int b) {
  return a / (a + b);
}
```

<a id="d24e27080"></a>
In theory, this three-line function has 1,000,000 logical states,
999,999 of which will work correctly and one that will not (when a + b
equals zero). Simply knowing that you executed this line of code doesn't
tell you that—you would need to identify all possible states of the
program. Unfortunately, in general this is a really hard problem.
Hard as in, “The sun will be a cold hard lump before you can solve it.”

**Tip 93: Test State Coverage, Not Code Coverage**

#### Property-Based Testing

<a id="d24e27097"></a>
A great way to explore how your code handles unexpected states is to
have a computer generate those states.

<a id="d24e27106"></a>
Use property-based testing techniques to generate test data according to the contracts and invariants of the code under test. We cover this topic in detail in Topic 42, [*Property-Based Testing*](<../07 While Coding/42 Property-Based Testing - proptest.md#proptest>).

### Tightening the Net

<a id="d24e27116"></a>
Finally, we'd like to reveal the single most important concept in
testing. It is an obvious one, and virtually every textbook says to
do it this way. But for some reason, most projects still do not.

<a id="d24e27127"></a>
If a bug slips through the net of existing tests, you need to add a
new test to trap it next time.

**Tip 94: Find Bugs Once**

<a id="d24e27138"></a>
Once a human tester finds a bug, it should be the last time a
human tester finds that bug.
The automated tests should be modified
to check for that particular bug from then on, every time, with no
exceptions, no matter how trivial, and no matter how much the developer
complains and says, “Oh, that will never happen again.”

<a id="d24e27152"></a>
Because it will happen again. And we just don't have the time to go
chasing after bugs that the automated tests could have found for us.
We have to spend our time writing new code—and new bugs.

### Full Automation

<a id="d24e27161"></a>
As we said at the beginning of this section, modern development relies on scripted, automatic procedures. Whether you use something as simple as shell scripts with rsync and ssh, or full-featured solutions such as Ansible, Puppet, Chef, or Salt, just don't rely on any manual intervention.

<a id="d24e27167"></a>
Once upon a time, we were at a client site where all the developers were using the same IDE. Their system administrator gave each developer a set of instructions on installing add-on packages to the IDE. These instructions filled many pages—pages full of click here, scroll there, drag this, double-click that, and do it again.

<a id="d24e27169"></a>
Not surprisingly, every developer's machine was loaded slightly differently. Subtle differences in the application's behavior occurred when different developers ran the same code. Bugs would appear on one machine but not on others. Tracking down version differences of any one component usually revealed a surprise.

**Tip 95: Don't Use Manual Procedures**

<a id="d24e27181"></a>
People just aren't as repeatable as computers are. Nor should we expect them to be. A shell script or program will execute the same instructions, in the same order, time after time. It is under version control itself, so you can examine changes to the build/release procedures over time as well (“but it used to work…”).

<a id="d24e27186"></a>
<a id="FNPTR-83"></a>
Everything depends on automation. You can't build the project on an
anonymous cloud server unless the build is fully automatic.
You can't deploy automatically if there are manual steps involved. And
once you introduce manual steps (“just for this one part…”) you've
broken a very large window.[[83]](<../10 Postface/README.md#FOOTNOTE-83>)

<a id="d24e27212"></a>
With these three legs of version control, ruthless testing, and full automation, your project will have the firm foundation you need so you can concentrate on the hard part: delighting users.

### Related Sections Include

- Topic 11, [*Reversibility*](<../02 Pragmatic Approach/11 Reversibility - reversi.md#reversi>)
- Topic 12, [*Tracer Bullets*](<../02 Pragmatic Approach/12 Tracer Bullets - tracer_bullets.md#tracer_bullets>)
- Topic 17, [*Shell Games*](<../03 Basic Tools/17 Shell Games - know_your_shell.md#know_your_shell>)
- Topic 19, [*Version Control*](<../03 Basic Tools/19 Version Control - version_control.md#version_control>)
- Topic 41, [*Test to Code*](<../07 While Coding/41 Test to Code - test_to_build.md#test_to_build>)
- Topic 49, [*Pragmatic Teams*](<49 Pragmatic Teams - teams.md#teams>)
- Topic 50, [*Coconuts Don't Cut It*](<50 Coconuts Don't Cut It - do_what_works.md#do_what_works>)

### Challenges

<a id="d24e27244"></a>
<a id="d24e27266"></a>
<a id="d24e27288"></a>
- Are your nightly or continuous builds automatic, but
  deploying to production isn't? Why? What's special about that server?
- Can you automatically test your project completely?
  Many teams are forced
  to answer “no.” Why? Is it too hard to define the acceptable
  results? Won't this make it hard to prove to the sponsors that the
  project is “done”?
- Is it too hard to test the application logic independent of the
  GUI? What does this say about the GUI? About coupling?
