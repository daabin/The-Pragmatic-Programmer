Source: https://panzhongxian.cn/en/the-pragmatic-programmer/4_pragmatic_paranoia.html#assertions

<a id="assertions"></a>
## Topic 25. Assertive Programming

> There is a luxury in self-reproach. When we blame ourselves we feel no one else has a right to blame us.
>
> Oscar Wilde, The Picture of Dorian Gray

<a id="d24e10166"></a>
It seems that there's a mantra that every programmer must memorize
early in his or her career. It is a fundamental tenet of computing, a core
belief that we learn to apply to requirements, designs, code, comments,
just about everything we do. It goes

<a id="d24e10198"></a>
> This can never happen…

<a id="d24e10200"></a>
“This application will never be used abroad, so why
internationalize it?” “count can't be negative.” “Logging
can't fail.”

<a id="d24e10205"></a>
Let's not practice this kind of self-deception, particularly when
coding.

**Tip 39: Use Assertions to Prevent the Impossible**

<a id="d24e10215"></a>
<a id="FNPTR-31"></a>
Whenever you find yourself thinking “but of course that could never happen,” add code to check it. The easiest way to do this is with assertions. In many language implementations, you'll find some form of assert that checks a Boolean condition.[[31]](<Topic 27. Don't Outrun Your Headlights - headlights.md#FOOTNOTE-31>) These checks can be invaluable. If a parameter or a result should never be null, then check for it explicitly:

```
assert (result != null);
```

<a id="d24e10270"></a>
In the Java implementation, you can (and should) add a descriptive string:

```
assert result != null  result.size() > 0 : "Empty result from XYZ";
```

<a id="d24e10287"></a>
Assertions are also useful checks on an algorithm's operation. Maybe
you've written a clever sort algorithm, named my\_sort. Check that it works:

```
books = my_sort(find("scifi"))
assert(is_sorted?(books))
```

<a id="d24e10305"></a>
Don't use assertions in place of real error handling. Assertions
check for things that should never happen: you don't want to be
writing code such as the following:

```
puts("Enter 'Y' or 'N': ")
ans = gets[0] # Grab first character of response
assert((ch == 'Y') || (ch == 'N'))    # Very bad idea!
```

<a id="d24e10338"></a>
And just because most assert implementations will terminate the
process when an assertion fails, there's no reason why versions you
write should. If you need to free resources, catch the assertion's
exception or trap the exit, and run your own error handler. Just make
sure the code you execute in those dying milliseconds doesn't rely on
the information that triggered the assertion failure in the first place.

### Assertions and Side Effects

<a id="d24e10346"></a>
It's embarrassing when the code we add to detect errors actually ends
up creating new errors. This can happen with assertions if evaluating
the condition has side effects. For example, it would be a
bad idea to code something such as

```
while (iter.hasMoreElements()) {
  assert(iter.nextElement() != null);
  Object obj = iter.nextElement();
  // ....
}
```

<a id="d24e10388"></a>
The .nextElement() call in the assertion has the side effect of
moving the iterator past the element being fetched, and so the loop
will process only half the elements in the collection. It would be
better to write

```
while (iter.hasMoreElements()) {
  Object obj = iter.nextElement();
  assert(obj != null);
  // ....
}
```

<a id="d24e10421"></a>
<a id="FNPTR-32"></a>
This problem is a kind of
Heisenbug[[32]](<Topic 27. Don't Outrun Your Headlights - headlights.md#FOOTNOTE-32>)—debugging
that changes the
behavior of the system being debugged.

<a id="d24e10435"></a>
(We also believe that nowadays, when most languages have decent support for iterating functions over collections, this kind of explicit loop is unnecessary and bad form.)

### Leave Assertions Turned On

<a id="d24e10442"></a>
There is a common misunderstanding about assertions. It goes
something like this:

<a id="d24e10449"></a>
> Assertions add some overhead to code. Because they check for things
> that should never happen, they'll get triggered only by a bug in the
> code. Once the code has been tested and shipped, they are no longer
> needed, and should be turned off to make the code run faster.
> Assertions are a debugging facility.

<a id="d24e10451"></a>
There are two patently wrong assumptions here. First, they assume that
testing finds all the bugs. In reality, for any complex program you are
unlikely to test even a minuscule percentage of the permutations your
code will be put through. Second, the optimists are forgetting that your
program runs in a dangerous world. During testing, rats probably won't
gnaw through a communications cable, someone playing a game won't
exhaust memory, and log files won't fill the storage partition. These
things might happen when your program runs in a production environment.
Your first line of defense is checking for any possible error, and your
second is using assertions to try to detect those you've missed.

<a id="d24e10462"></a>
Turning off assertions when you deliver a program to production is
like crossing a high wire without a net because you once made it
across in practice. There's dramatic value, but it's hard to get life
insurance.

<a id="d24e10465"></a>
Even if you do have performance issues, turn off only those
assertions that really hit you. The sort example above
may be a critical part of your application, and may need to be fast.
Adding the check means another pass through the data, which might be
unacceptable. Make that particular check optional, but leave the rest in.

<a id="d24e10510"></a>
<a id="d24e10532"></a>
<a id="d24e10534"></a>
Use Assertions in Production, Win Big Money

A former neighbor of Andy's headed up a small startup company that made network devices. One of their secrets to success was the decision to leave assertions in place in production releases. These assertions were well crafted to report all the pertinent data leading to the failure, and presented via a nice-looking UI to the end user. This level of feedback, from real users under actual conditions, allowed the developers to plug the holes and fix these obscure, hard-to-reproduce bugs, resulting in remarkably stable, bullet-proof software.

This small, unknown company had such a solid product, it was soon acquired for hundreds of millions of dollars.

Just sayin'.

<a id="exercise-16"></a>
**Exercise 16** ([possible answer](<../A2 Exercise Answers/README.md#answer-16>))

<a id="d24e10546"></a>
A quick reality check. Which of these “impossible” things can
happen?

- A month with fewer than 28 days
- Error code from a system call: can't access the current directory
- In C++: a = 2; b = 3; but (a + b) does not equal 5
- A triangle with an interior angle sum ≠ 180°
- A minute that doesn't have 60 seconds
- (a + 1) <= a

### Related Sections Include

- Topic 23, [*Design by Contract*](<23 Design by Contract - dbc.md#dbc>)
- Topic 24, [*Dead Programs Tell No Lies*](<24 Dead Programs Tell No Lies - crash_early.md#crash_early>)
- Topic 42, [*Property-Based Testing*](<../07 While Coding/42 Property-Based Testing - proptest.md#proptest>)
- Topic 43, [*Stay Safe Out There*](<../07 While Coding/43 Stay Safe Out There - safety.md#safety>)
