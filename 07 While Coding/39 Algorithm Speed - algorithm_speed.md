<a id="algorithm_speed"></a>
## Topic 39. Algorithm Speed

<a id="d24e20127"></a>
In Topic 15, [*Estimating*](<../02 Pragmatic Approach/15 Estimating - learn_to_estimate.md#learn_to_estimate>), we talked about estimating things
such as how long it takes to walk across town, or how long a project
will take to finish. However, there is another kind of estimating that
Pragmatic Programmers use almost daily: estimating the resources that
algorithms use—time, processor, memory, and so on.

<a id="d24e20150"></a>
This kind of estimating is often crucial. Given a choice between two
ways of doing something, which do you pick? You know how long your
program runs with 1,000 records, but how will it scale to 1,000,000?
What parts of the code need optimizing?

<a id="d24e20152"></a>
It turns out that these questions can often be answered using common
sense, some analysis, and a way of writing approximations called the
Big-O notation.

### What Do We Mean by Estimating Algorithms?

<a id="d24e20162"></a>
Most nontrivial algorithms handle some kind of variable input—sorting
$ n $ strings, inverting an $ m \times n $ matrix, or decrypting a message
with an $ n $-bit key. Normally, the size of this input will affect the
algorithm: the larger the input, the longer the running time or the more
memory used.

<a id="d24e20170"></a>
If the relationship were always linear (so that the time increased in
direct proportion to the value of $ n $), this section wouldn't be
important. However, most significant algorithms are not linear. The good
news is that many are sublinear. A binary search, for example, doesn't
need to look at every candidate when finding a match. The bad news is
that other algorithms are considerably worse than linear; runtimes or
memory requirements increase far faster than $ n $. An algorithm that
takes a minute to process ten items may take a lifetime to process 100.

<a id="d24e20176"></a>
We find that whenever we write anything containing loops or recursive
calls, we subconsciously check the runtime and memory requirements. This
is rarely a formal process, but rather a quick confirmation that what
we're doing is sensible in the circumstances. However, we sometimes do
find ourselves performing a more detailed analysis. That's when Big-O
notation comes in handy.

<a id="big-o"></a>
### Big-O Notation

<a id="d24e20193"></a>
The Big-O notation, written `O()`, is a mathematical way of dealing with
approximations. When we write that a particular sort routine sorts `O()`
records in `O(n^2)` time, we are simply saying that the worst-case
time taken will vary as the square of $ n $. Double the number of
records, and the time will increase roughly fourfold. Think of the $ O $
as meaning on the order of.

<a id="d24e20210"></a>
The `O()` notation puts an upper
bound on the value of the thing we're measuring (time, memory, and so
on). If we say a function takes `O(n^2)` time, then we know that the
upper bound of the time it takes will not grow faster than $ n^2 $.
Sometimes we come up with fairly complex `O()` functions, but because
the highest-order term will dominate the value as $ n $ increases, the
convention is to remove all low-order terms, and not to bother showing
any constant multiplying factors:

```text
O(n^2 / 2 + 3n) is the same as O(n^2 / 2) is the same as O(n^2)
```

<a id="d24e20233"></a>
This is
actually a feature of the `O()` notation—one `O(n^2)` algorithm may
be 1,000 times faster than another `O(n^2)` algorithm, but you won't
know it from the notation. Big-O is never going to give you actual
numbers for time or memory or whatever: it simply tells you how these
values will change as the input changes.

<a id="d24e20241"></a>
Figure 3, [*Runtimes of various algorithms*](#fig-onotation) shows several common `O()`
notations you'll come across, along with a graph comparing running times of
algorithms in each category. Clearly, things quickly start getting
out of hand once we get over `O(n^2)`.

<a id="d24e20248"></a>
For example, suppose you've got a routine that takes one second to
process 100 records. How long will it take to process 1,000? If your
code is `O(1)`, then it will still take one second. If it's
`O(log n)`, then you'll probably be waiting about three
seconds. `O(n)` will show a linear increase to ten seconds,
while an `O(n log n)` will take some 33 seconds. If
you're unlucky enough to have an `O(n^2)` routine, then sit
back for 100 seconds while it does its stuff. And if you're using
an exponential algorithm `O(2^n)`, you might want to make a
cup of coffee—your routine should finish in about `10^263`
years. Let us know how the universe ends.

<a id="d24e20357"></a>
The `O()` notation doesn't apply just to time; you can use it to
represent any other resources used by an algorithm. For example, it
is often useful to be able to model memory consumption (see the
exercises for an example).

<a id="fig-onotation"></a>
<a id="d24e20422"></a>
<a id="aabig-o"></a>
|  |  |
| --- | --- |
| $O(1)$ | Constant (access element in array, simple statements) |
| `O(log n)` | Logarithmic (binary search). The base of the logarithm doesn't matter, so this is equivalent $O(\log{n})$. |
| $O(n)$ | Linear (sequential search) |
| $O(n\,\lg{n})$ | Worse than linear, but not much worse. (Average runtime of quicksort, heapsort) |
| `O(n^2)` | Square law (selection and insertion sorts) |
| $O(n^3)$ | Cubic (multiplication of two $n \times n$ matrices) |
| $O(C^n)$ | Exponential (traveling salesman problem, set partitioning) |

![A graph shows the runtime of various algorithms.](https://panzhongxian.cn/images/the-pragmatic-programmer/big-o.png)

Figure 3. Runtimes of various algorithms

A graph is drawn to calculate the runtime of various algorithms. The horizontal axis represents n value and the vertical axis represents the runtime value. The curves for algorithms, O (C power n): set cover, O (n squared) nested arrays, and O (n natural log n): heap sort search starts from the origin and shows a rapid increase (concave up increasing). Another curve for O (log n): binary search starts from the origin, increases to a certain height and then moves in a steady state. An increasing line for O (n): sequential search starts from the origin. Finally the steady line for O (1): array access is drawn parallel to the horizontal axis.

<a id="pg-common-sense"></a>
### Common Sense Estimation

<a id="d24e20428"></a>
You can estimate the order of many basic algorithms using common
sense.

<a id="d24e20434"></a>
<a id="d24e20468"></a>
<a id="d24e20497"></a>
<a id="d24e20516"></a>
<a id="d24e20534"></a>
Simple loops
:   If a simple loop runs from $1$ to $n$, then the
    algorithm is likely to be $O(n)$—time increases linearly with
    $n$. Examples include exhaustive searches, finding the maximum
    value in an array, and generating checksums.

Nested loops
:   If you nest a loop inside another, then your
    algorithm becomes $O(m\times n)$, where $m$ and $n$ are the two
    loops' limits. This commonly occurs in simple sorting algorithms,
    such as bubble sort, where the outer loop scans each element in the
    array in turn, and the inner loop works out where to place that
    element in the sorted result. Such sorting algorithms tend to be
    `O(n^2)`.

Binary chop
:   If your algorithm halves the set of things it
    considers each time around the loop, then it is likely to be
    logarithmic, `O(log n)`. A binary search of a sorted list, traversing a
    binary tree, and finding the first set bit in a machine word can all
    be `O(log n)`.

Divide and conquer
:   Algorithms that partition their input
    work on the two halves independently, and then combine the result
    can be $O(n\,\lg{n})$. The classic example is quicksort,
    which works
    by partitioning the data into two halves and recursively sorting
    each. Although technically `O(n^2)`, because its behavior degrades
    when it is fed sorted input, the average runtime of quicksort is
    $O(n\,\lg{n})$.

Combinatoric
:   Whenever algorithms start looking at the
    permutations of things, their running times may get out of hand.
    This is because permutations involve factorials (there are
    $5! = 5\times 4 \times 3 \times 2 \times 1 = 120$
    permutations of the
    digits from 1 to 5). Time a combinatoric algorithm for five
    elements: it will take six times longer to run it for six, and 42
    times longer for seven. Examples include algorithms for many of the acknowledged
    hard problems—the traveling salesman problem, optimally
    packing things into a container, partitioning a set of numbers so
    that each set has the same total, and so on. Often, heuristics are
    used to reduce the running times of these types of algorithms in
    particular problem domains.

### Algorithm Speed in Practice

<a id="d24e20570"></a>
It's unlikely that you'll spend much time during your career writing
sort routines. The ones in the libraries available to you will
probably outperform anything you may write without substantial effort.
However, the basic kinds of algorithms we've described earlier pop up
time and time again. Whenever you find yourself writing a simple loop,
you know that you have an $O(n)$ algorithm.
If that loop contains an
inner loop, then you're looking at $O(m \times n)$. You should be
asking yourself how large these values can get. If the numbers are
bounded, then you'll know how long the code will take to run. If the
numbers depend on external factors (such as the number of records in
an overnight batch run, or the number of names in a list of people),
then you might want to stop and consider the effect that large values
may have on your running time or memory consumption.

**Tip 63: Estimate the Order of Your Algorithms**

<a id="d24e20608"></a>
There are some approaches you can take to address potential problems.
If you have an algorithm that is `O(n^2)`, try to find a divide-and-conquer approach that will take you down to `O(n log n)`.

<a id="d24e20618"></a>
If you're not sure how long your code will take, or how much memory it
will use, try running it, varying the input record count or whatever
is likely to impact the runtime.
Then plot the results. You should
soon get a good idea of the shape of the curve. Is it curving upward,
a straight line, or flattening off as the input size increases? Three
or four points should give you an idea.

<a id="d24e20624"></a>
Also consider just what you're doing in the code itself. A simple
`O(n^2)` loop may well perform better than a complex,
`O(n log n)`
one for smaller values of $n$, particularly if the
`O(n log n)`
algorithm has an expensive inner loop.

<a id="d24e20634"></a>
In the middle of all this theory, don't forget that there are practical
considerations as well. Runtime may look like it increases linearly for
small input sets. But feed the code millions of records and suddenly the
time degrades as the system starts to thrash. If you test a sort routine
with random input keys, you may be surprised the first time it
encounters ordered input. Try to cover both the
theoretical and practical bases. After all this estimating, the only
timing that counts is the speed of your code, running in the production
environment, with real data. This leads to our next tip.

**Tip 64: Test Your Estimates**

<a id="d24e20647"></a>
If it's tricky getting accurate timings, use code profilers
to count the number of times the different steps in your algorithm get
executed, and plot these figures against the size of the input.

#### Best Isn't Always Best

<a id="d24e20657"></a>
You also need to be pragmatic about choosing appropriate
algorithms—the fastest one is not always the best for the job. Given a
small input set, a straightforward insertion sort will perform just as
well as a quicksort, and will take you less time to write and debug. You
also need to be careful if the algorithm you choose has a high setup
cost. For small input sets, this setup may dwarf the running time and
make the algorithm inappropriate.

<a id="d24e20663"></a>
Also be wary of premature optimization. It's always a good idea
to make sure an algorithm really is a bottleneck before investing your
precious time trying to improve it.

### Related Sections Include

- Topic 15, [*Estimating*](<../02 Pragmatic Approach/15 Estimating - learn_to_estimate.md#learn_to_estimate>)

### Challenges

<a id="d24e20688"></a>
<a id="d24e20724"></a>
<a id="d24e20744"></a>
- Every developer should have a feel for how algorithms are
  designed and analyzed. Robert Sedgewick has written a series of
  accessible books on the subject
  ([*Algorithms* [SW11]](<../A2 Exercise Answers/README.md#d6040e927>)[*An Introduction to the Analysis of Algorithms* [SF13]](<../A2 Exercise Answers/README.md#d6040e849>) and others).
  We recommend adding one of his books to your collection, and making a
  point of reading it.
- For those who like more detail than Sedgewick provides, read
  Donald Knuth's definitive Art of Computer Programming books,
  which analyze a wide range of algorithms.

  - [*The Art of Computer Programming, Volume 1: Fundamental Algorithms* [Knu98]](<../A2 Exercise Answers/README.md#d6040e641>)
  - [*The Art of Computer Programming, Volume 2: Seminumerical Algorithms* [Knu98a]](<../A2 Exercise Answers/README.md#d6040e675>)
  - [*The Art of Computer Programming, Volume 3: Sorting and Searching* [Knu98b]](<../A2 Exercise Answers/README.md#d6040e709>)
  - [*The Art of Computer Programming, Volume 4A: Combinatorial
    Algorithms, Part 1* [Knu11]](<../A2 Exercise Answers/README.md#d6040e610>).
- In the first exercise that follows we look at sorting arrays
  of long integers. What is the impact if the keys are more complex, and
  the overhead of key comparison is high? Does the key structure
  affect the efficiency of the sort algorithms, or is the fastest sort
  always fastest?

### Exercises

<a id="exercise-28"></a>
**Exercise 28** ([possible answer](<../A2 Exercise Answers/README.md#answer-28>))

<a id="d24e20757"></a>
<a id="FNPTR-54"></a>
We coded a set of simple sort
routines[[54]](<44 Naming Things - naming.md#FOOTNOTE-54>) in
Rust. Run them on various machines available to you. Do your figures
follow the expected curves? What can you deduce about the relative
speeds of your machines? What are the effects of various compiler
optimization settings?

<a id="exercise-29"></a>
**Exercise 29** ([possible answer](<../A2 Exercise Answers/README.md#answer-29>))

<a id="d24e20786"></a>
In [*Common Sense Estimation*](#pg-common-sense), we claimed that a binary
chop is `O(log n)`. Can you prove this?

<a id="exercise-30"></a>
**Exercise 30** ([possible answer](<../A2 Exercise Answers/README.md#answer-30>))

<a id="d24e20802"></a>
In Figure 3, [*Runtimes of various algorithms*](#fig-onotation), we claimed that
`O(log n)` is the same as `O(log10 n)` (or indeed logarithms to any base). Can you explain why?
