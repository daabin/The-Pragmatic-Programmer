Source: https://panzhongxian.cn/en/the-pragmatic-programmer/6_concurrency.html#temporal_coupling

<a id="temporal_coupling"></a>
## Topic 33. Breaking Temporal Coupling

<a id="d24e16957"></a>
“What is temporal coupling all about?”, you may ask. It's
about time.

<a id="d24e16962"></a>
Time is an often ignored aspect of software architectures. The only time
that preoccupies us is the time on the schedule, the time left until we
ship—but this is not what we're talking about here. Instead, we are
talking about the role of time as a design element of the software
itself. There are two aspects of time that are important to us:
concurrency (things happening at the same time) and ordering (the
relative positions of things in time).

<a id="d24e16997"></a>
We don't usually approach programming with either of these aspects in
mind. When people first sit down to design an architecture or write a
program, things tend to be linear. That's the way most people
think—do this and then always do that. But thinking this
way leads to temporal coupling: coupling in time. Method
A must always be called before method B; only one report can
be run at a time; you must wait for the screen to redraw before the
button click is received. Tick must happen before tock.

<a id="d24e17014"></a>
This approach is not very flexible, and not very realistic.

<a id="d24e17016"></a>
We need to allow for concurrency and to think about decoupling any time
or order dependencies. In doing so, we can gain flexibility and reduce
any time-based dependencies in many areas of development: workflow
analysis, architecture, design, and deployment. The result will be
systems that are easier to reason about, that potentially respond
faster and more reliably.

### Looking for Concurrency

<a id="d24e17021"></a>
<a id="FNPTR-46"></a>
On many projects, we need to model and analyze the application workflows
as part of the design. We'd like to find out what can happen at the
same time, and what must happen in a strict order. One way to do this
is to capture the workflow using a notation such as the activity
diagram.[[46]](<Topic 36. Blackboards - blackboards.md#FOOTNOTE-46>)

**Tip 56: Analyze Workflow to Improve Concurrency**

<a id="d24e17072"></a>
An activity diagram consists of a set of actions drawn as rounded boxes.
The arrow leaving an action leads to either another action (which can
start once the first action completes) or to a thick line called a
synchronization bar. Once all the actions leading into a
synchronization bar are complete, you can then proceed along any arrows
leaving the bar. An action with no arrows leading into it can be
started at any time.

<a id="d24e17082"></a>
You can use activity diagrams to maximize parallelism by identifying
activities that could be performed in parallel, but aren't.

<a id="d24e17096"></a>
For instance, we may be writing the software for a robotic piña colada
maker. We're told that the steps are:

|  |  |
| --- | --- |
| 1. Open blender 2. Open piña colada mix 3. Put mix in blender 4. Measure 1/2 cup white rum 5. Pour in rum 6. Add 2 cups of ice | 1. Close blender 2. Liquefy for 1 minute 3. Open blender 4. Get glasses 5. Get pink umbrellas 6. Serve |

<a id="d24e17156"></a>
However, a bartender would lose their job if they followed these steps,
one by one, in order. Even though they describe these actions serially,
many of them could be performed in parallel. We'll use the following activity diagram to capture and reason about
potential concurrency.

<a id="d24e17158"></a>
<a id="apina-colada"></a>
![An activity diagram represents the task carried out in a robotic piña coloda maker.](https://panzhongxian.cn/images/the-pragmatic-programmer/pina-colada.png)

An activity diagram illustrates the potential concurrency of the tasks in a robotic piña coloda maker. There are twelve tasks. The first task, open blender and the second task, open mix happens parallely. Similarly, the first task, open blender and fourth task, measure rum happens parallely. The third task put mix in blender, sixth task add two cups ice, and the fifth task pour in rum happens parallely. The fifth task leads to the seventh task, close blender. The eighth task is blend, the ninth task is open blender. The tenth task get glasses, eleventh task get pink umbrellas, and the ninth task open blender leads to the final task, serve.

<a id="d24e17160"></a>
It can be eye-opening to see where the dependencies really exist. In
this instance, the top-level tasks (1, 2, 4, 10, and 11) can all happen
concurrently, up front. Tasks 3, 5, and 6 can happen in parallel later.
If you were in a piña colada-making contest, these optimizations may
make all the difference.

<a id="d24e17165"></a>
<a id="d24e17190"></a>
<a id="d24e17192"></a>
<a id="d24e17204"></a>
<a id="d24e17206"></a>
Faster Formatting

This book is written in plain text. To build the version to be printed,
or an ebook, or whatever, that text is fed through a pipeline of
processors. Some look for particular constructs (bibliography
citations, index entries, special markup for tips, and so on). Other
processors operate on the document as a whole.

Many of the processors in the pipeline have to access external
information (reading files, writing files, piping through external
programs). All this relatively slow speed work gives us the opportunity
to exploit concurrency: in fact each step in the pipeline executes
concurrently, reading from the previous step and writing to the next.

In addition, some parts of the process are relatively processor
intensive. One of these is the conversion of mathematical formulae. For
various historical reasons each equation can take up to 500ms to
convert. To speed things up, we take advantage of parallelism. Because
each formula is independent of the others, we convert each in its own
parallel process and collect the results back into the book as they
become available.

As a result, the book builds much, much faster on multicore machines.

(And, yes, we did indeed discover a number of concurrency errors in our pipeline
along the way….)

### Opportunities for Concurrency

<a id="d24e17211"></a>
Activity diagrams show the potential areas of concurrency, but have
nothing to say about whether these areas are worth exploiting. For
example, in the piña colada example, a bartender would need five hands
to be able to run all the potential initial tasks at once.

<a id="d24e17213"></a>
And that's where the design part comes in. When we look at the
activities, we realize that number 8, liquify, will take a minute.
During that time, our bartender can get the glasses and umbrellas
(activities 10 and 11) and probably still have time to serve another
customer.

<a id="d24e17215"></a>
And that's what we're looking for when we're designing for concurrency.
We're hoping to find activities that take time, but not time in our
code. Querying a database, accessing an external service, waiting for
user input: all these things would normally stall our program until they
complete. And these are all opportunities to do something more
productive than the CPU equivalent of twiddling one's thumbs.

### Opportunities for Parallelism

<a id="d24e17229"></a>
Remember the distinction: concurrency is a software mechanism, and
parallelism is a hardware concern. If we have multiple processors,
either locally or remotely, then if we can split work out among them we
can reduce the overall time things take.

<a id="d24e17240"></a>
The ideal things to split this way are pieces of work that are
relatively independent—where each can proceed without waiting for
anything from the others. A common pattern is to take a large piece of
work, split it into independent chunks, process each in parallel, then
combine the results.

<a id="d24e17242"></a>
An interesting example of this in practice is the way the compiler for
the Elixir language works. When it starts, it splits the project it is
building into modules, and compiles each in parallel. Sometimes a module
depends on another, in which case its compilation pauses until the
results of the other module's build become available. When the top-level
module completes, it means that all dependencies have been compiled. The
result is a speedy compilation that takes advantage of all the cores
available.

### Identifying Opportunities Is the Easy Part

<a id="d24e17266"></a>
Back to your applications. We've identified places where it will benefit
from concurrency and parallelism. Now for the tricky part: how can we
implement it safely. That's the topic of the rest of the chapter.

### Related Sections Include

- Topic 10, [*Orthogonality*](<../02 Pragmatic Approach/10 Orthogonality - orthogonality.md#orthogonality>)
- Topic 26, [*How to Balance Resources*](<../04 Pragmatic Paranoia/26 How to Balance Resources - balance_resources.md#balance_resources>)
- Topic 28, [*Decoupling*](<../05 Bend or Break/28 Decoupling - coupling.md#coupling>)
- Topic 36, [*Blackboards*](<36 Blackboards - blackboards.md#blackboards>)

### Challenges

- How many tasks do you perform in parallel when you get ready for
  work in the morning? Could you express this in a UML activity
  diagram? Can you find some way to get ready more quickly by
  increasing concurrency?
