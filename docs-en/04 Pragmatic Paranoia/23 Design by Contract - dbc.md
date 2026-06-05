<a id="dbc"></a>
## Topic 23. Design by Contract

> Nothing astonishes men so much as common sense and plain dealing.
>
> Ralph Waldo Emerson, Essays

<a id="d24e9081"></a>
Dealing with computer systems is hard. Dealing with people is even
harder. But as a species, we've had longer to figure out issues of
human interactions. Some of the solutions we've come up with during
the last few millennia can be applied to writing software as well.
One of the best solutions for ensuring plain dealing is the
contract.

<a id="d24e9095"></a>
A contract defines your rights and responsibilities, as well as those
of the other party. In addition, there is an
agreement concerning repercussions if either party fails to abide by
the contract.

<a id="d24e9097"></a>
Maybe you have an employment contract that specifies the hours you'll
work and the rules of conduct you must follow. In return, the company
pays you a salary and other perks. Each party meets its obligations
and everyone benefits.

<a id="d24e9099"></a>
It's an idea used the world over—both formally and informally—to
help humans interact. Can we use the same concept to help software
modules interact? The answer is “yes.''

### DBC

<a id="d24e9106"></a>
<a id="FNPTR-30"></a>
Bertrand Meyer
([*Object-Oriented Software Construction* [Mey97]](<../A2 Exercise Answers/README.md#d6040e783>)) developed the concept of
Design by Contract for the language Eiffel.[[30]](<27 Don't Outrun Your Headlights - headlights.md#FOOTNOTE-30>) It is a simple yet
powerful technique that focuses on documenting (and agreeing to) the
rights and responsibilities of software modules to ensure program
correctness. What is a correct program? One that does no more and no
less than it claims to do. Documenting and verifying that claim is
the heart of Design by Contract (DBC, for short).

<a id="d24e9130"></a>
Every function and method in a software system does something.
Before it starts that something, the function may have some
expectation of the state of the world, and it may be able to make a
statement about the state of the world when it concludes. Meyer
describes these expectations and claims as follows:

<a id="d24e9151"></a>
<a id="d24e9167"></a>
<a id="d24e9187"></a>
Preconditions
:   What must be true in order for the routine to
    be called; the routine's requirements.
    A routine should never get
    called when its preconditions would be violated. It is the
    caller's responsibility to pass good data (see the box
    [here](#sb-preconditions)).

Postconditions
:   What the routine is guaranteed to do; the
    state of the world when the routine is done. The fact that the
    routine has a postcondition implies that it will
    conclude: infinite loops aren't allowed.

Class invariants
:   A class ensures that this condition is always
    true from the perspective of a caller. During internal processing
    of a routine, the invariant may not hold, but by the time the
    routine exits and control returns to the caller, the invariant must
    be true. (Note that a class cannot give unrestricted
    write-access to any data member that participates in the
    invariant.)

<a id="d24e9203"></a>
The contract between a routine and any potential caller can thus be
read as

<a id="d24e9206"></a>
> If all the routine's preconditions are met by the caller,
> the routine shall guarantee that all postconditions and invariants
> will be true when it completes.

<a id="d24e9208"></a>
If either party fails to live up to the terms of the contract, then a
remedy (which was previously agreed to) is invoked—maybe an exception
is raised, or the program terminates. Whatever happens, make no mistake
that failure to live up to the contract is a bug. It is not something
that should ever happen, which is why preconditions should not be used
to perform things such as user-input validation.

<a id="d24e9210"></a>
Some languages have better support for these concepts than others. Clojure, for example, supports pre- and post-conditions as well as the more comprehensive instrumentation provided by specs. Here's an example of a banking function to make a deposit using simple pre- and post-conditions:

```
(defn accept-deposit [account-id amount]
   { :pre [  (> amount 0.00)
             (account-open? account-id) ]
     :post [ (contains? (account-transactions account-id) %) ] }
   "Accept a deposit and return the new transaction id"
   ;; Some other processing goes here...
   ;; Return the newly created transaction:
   (create-transaction account-id :deposit amount))
```

<a id="d24e9265"></a>
There are two preconditions for the accept-deposit function. The first is that the amount is greater than zero, and the second is that the account is open and valid, as determined by some function named account-open?. There is also a postcondition: the function guarantees that the new transaction (the return value of this function, represented here by ‘%') can be found among the transactions for this account.

<a id="d24e9273"></a>
If you call accept-deposit with a positive amount for the deposit and a valid account, it will proceed to create a transaction of the appropriate type and do whatever other processing it does. However, if there's a bug in the program and you somehow passed in a negative amount for the deposit, you'll get a runtime exception:

```
Exception in thread "main"...
Caused by: java.lang.AssertionError: Assert failed: (> amount 0.0)
```

<a id="d24e9284"></a>
Similarly, this function requires that the specified account is open and valid. If it's not, you'll see that exception instead:

```
Exception in thread "main"...
Caused by: java.lang.AssertionError: Assert failed: (account-open? account-id)
```

<a id="d24e9292"></a>
Other languages have features that, while not DBC-specific, can still be used to good effect. For example, Elixir uses guard clauses to dispatch function calls against several available bodies:

```
defmodule Deposits do
  def accept_deposit(account_id, amount) when (amount > 100000) do
    # Call the manager!
  end
  def accept_deposit(account_id, amount) when (amount > 10000) do
    # Extra Federal requirements for reporting
    # Some processing...
  end
  def accept_deposit(account_id, amount) when (amount > 0) do
    # Some processing...
  end
end
```

<a id="d24e9376"></a>
In this case, calling accept\_deposit with a large enough amount may trigger additional steps and processing. Try to call it with an amount less than or equal to zero, however, and you'll get an exception informing you that you can't:

```
** (FunctionClauseError) no function clause matching in Deposits.accept_deposit/2
```

<a id="d24e9385"></a>
This is a better approach than simply checking your inputs; in this case, you simply can not call this function if your arguments are out of range.

**Tip 37: Design with Contracts**

<a id="d24e9396"></a>
In Topic 10, [*Orthogonality*](<../02 Pragmatic Approach/10 Orthogonality - orthogonality.md#orthogonality>), we recommended writing “shy” code. Here,
the emphasis is on “lazy” code:
be strict in what you will
accept before you begin, and promise as little as possible in return.
Remember, if your contract indicates that you'll accept anything and
promise the world in return, then you've got a lot of code to write!

<a id="d24e9400"></a>
In any programming language, whether it's functional, object-oriented,
or procedural, DBC forces you to think.

<a id="d24e9411"></a>
<a id="d24e9443"></a>
<a id="d24e9445"></a>
<a id="d24e9449"></a>
<a id="d24e9452"></a>
<a id="d24e9458"></a>
<a id="d24e9471"></a>
<a id="d24e9474"></a>
<a id="d24e9479"></a>
DBC and Test-Driven Development

Is Design by Contract needed in a world where developers practice unit testing, test-driven development (TDD), property-based testing, or defensive programming?

The short answer is “yes.”

DBC and testing are different approaches to the broader topic of program correctness. They both have value and both have uses in different situations.
DBC offers several advantages over specific testing approaches:

- DBC doesn't require any setup or mocking
- DBC defines the parameters for success or failure in all cases, whereas testing can only target one specific case at a time
- TDD and other testing happens only at “test time” within the build cycle. But DBC and assertions are forever: during design, development, deployment, and maintenance
- TDD does not focus on checking internal invariants within the code under test, it's more black-box style to check the public interface
- DBC is more efficient (and DRY-er) than defensive programming, where everyone has to validate data in case no one else does.

TDD is a great technique, but as with many techniques, it might invite you to concentrate on the “happy path,” and not the real world full of bad data, bad actors, bad versions, and bad specifications.

#### Class Invariants and Functional Languages

<a id="d24e9484"></a>
It's a naming thing. Eiffel is an object-oriented language, so Meyer named this idea “class
invariant.” But, really, it's more general than that. What this idea really
refers to is state. In an object-oriented language, the state is associated with
instances of classes. But other languages have state, too.

<a id="d24e9509"></a>
In a functional language, you typically pass state to functions and
receive updated state as a result. The concepts of invariants is just as
useful in these circumstances.

### Implementing DBC

<a id="d24e9535"></a>
Simply enumerating what the input domain range is, what the boundary
conditions are, and what the routine promises to deliver—or, more
importantly, what it doesn't promise to deliver—before you write the code is a huge
leap forward in writing better software. By not stating these things,
you are back to programming by coincidence (see the discussion [here](<../07 While Coding/38 Programming by Coincidence - coincidence.md#coincidence>)), which is where many projects start, finish, and
fail.

<a id="d24e9554"></a>
In languages that do not support DBC in the code, this might be as far as you can go—and that's not too bad. DBC is, after all, a design technique. Even without automatic checking, you can put the contract in the code as comments or in the unit tests and still get a very real benefit.

#### Assertions

<a id="d24e9576"></a>
While documenting these assumptions is a great start, you can get much
greater benefit by having the compiler check your contract for you.
You can partially emulate this in some languages by using
assertions: runtime checks of logical conditions (see Topic 25, [*Assertive Programming*](<25 Assertive Programming - assertions.md#assertions>)). Why only partially?
Can't you use assertions to do everything DBC can do?

<a id="d24e9597"></a>
Unfortunately, the answer is no. To begin with, in object-oriented languages there probably is no support for propagating assertions down an inheritance hierarchy. This means that if you override a base class method that has a contract, the assertions that implement that contract will not be called correctly (unless you duplicate them manually in the new code). You must remember to call the class invariant (and all base class invariants) manually before you exit every method. The basic problem is that the contract is not automatically enforced.

<a id="d24e9613"></a>
In other environments, the exceptions generated from DBC-style assertions might be turned off globally or ignored in the code.

<a id="d24e9619"></a>
Also, there is no built-in concept of “old'' values; that is, values
as they existed at the entry to a method. If you're using assertions to enforce
contracts, you must add code to the precondition to save any
information you'll want to
use in the postcondition, if the language will even allow that.
In the Eiffel language, where DBC was born, you can just use old expression.

<a id="d24e9639"></a>
Finally, conventional runtime systems and libraries are not designed to
support contracts, so these calls are not checked. This is a big loss,
because it is often at the boundary between your code and the
libraries it uses that the most problems are detected (see
Topic 24, [*Dead Programs Tell No Lies*](<24 Dead Programs Tell No Lies - crash_early.md#crash_early>) for a more detailed discussion).

<a id="sb-preconditions"></a>
<a id="d24e9655"></a>
<a id="d24e9673"></a>
<a id="d24e9694"></a>
Who's Responsible?

Who is responsible for checking the precondition, the caller or the
routine being called?
When implemented as part of the language, the
answer is neither: the precondition is tested behind the scenes
after the caller invokes the routine but before the routine itself
is entered. Thus if there is any explicit checking of parameters to
be done, it must be performed by the caller, because the
routine itself will never see parameters that violate its
precondition. (For languages without built-in support, you would
need to bracket the called routine with a preamble and/or
postamble that checks these assertions.)

Consider a program that reads a number from the console, calculates
its square root (by calling sqrt), and prints the result. The
sqrt function has a precondition—its argument must not be
negative. If the user enters a negative number at the console, it is
up to the calling code to ensure that it never gets passed to
sqrt. This calling code has many options: it could
terminate, it could issue a warning and read another number, or it
could make the number positive and append an i to the result
returned by sqrt. Whatever its choice, this is definitely not
sqrt's problem.

By expressing the domain of the square root function in the
precondition of the sqrt routine, you shift the burden of
correctness to the caller—where it belongs. You can then design
the sqrt routine secure in the knowledge that its input
will be in range.

### DBC and Crashing Early

<a id="d24e9707"></a>
DBC fits in nicely with our concept of crashing early (see
Topic 24, [*Dead Programs Tell No Lies*](<24 Dead Programs Tell No Lies - crash_early.md#crash_early>)). By using an assert or DBC mechanism to validate the preconditions, postconditions, and invariants, you can crash early and report more accurate information about the problem.

<a id="d24e9728"></a>
For example, suppose you have a method that calculates square roots. It needs a DBC precondition that restricts the domain to positive numbers. In languages that support DBC, if you pass sqrt a negative parameter, you'll get an informative error such as sqrt\_arg\_must\_be\_positive, along with a stack trace.

<a id="d24e9736"></a>
This is better than the alternative in other languages
such as Java, C, and C++
where passing a negative number to sqrt returns the special value NaN (Not a Number). It may be some time later in the program that you attempt to do some math on NaN, with surprising results.

<a id="d24e9747"></a>
It's much easier to find and diagnose the problem by crashing
early, at the site of the problem.

### Semantic Invariants

<a id="d24e9752"></a>
You can use semantic invariants to express inviolate
requirements, a kind of “philosophical contract.''

<a id="d24e9761"></a>
We once wrote a debit card transaction switch. A major requirement was
that the user of a debit card should never have the same transaction
applied to their account twice. In other words, no matter what sort of
failure mode might happen, the error should be on the side of
not processing a transaction rather than processing a duplicate
transaction.

<a id="d24e9766"></a>
This simple law, driven directly from the requirements, proved to be
very helpful in sorting out complex error recovery scenarios,
and guided the detailed design and implementation in many areas.

<a id="d24e9768"></a>
Be sure not to confuse requirements that are fixed, inviolate laws
with those that are merely policies that might change with
a new management regime. That's why we use the term semantic
invariants—it must be central to the very meaning of a thing,
and not subject to the whims of policy (which is what more dynamic
business rules are for).

<a id="d24e9790"></a>
When you find a requirement that qualifies, make sure it becomes a
well-known part of whatever documentation
you are producing—whether
it is a bulleted list in the requirements document that gets signed in
triplicate or just a big note on the common whiteboard that everyone
sees. Try to state it clearly and unambiguously. For example, in the
debit card example, we might write

<a id="d24e9797"></a>
> Err in favor of the consumer.

<a id="d24e9799"></a>
This is a clear, concise, unambiguous statement that's applicable in
many different areas of the system. It is our contract with all users
of the system, our guarantee of behavior.

### Dynamic Contracts and Agents

<a id="d24e9805"></a>
Until now, we have talked about contracts as fixed, immutable
specifications. But in the landscape of autonomous agents, this
doesn't need to be the case. By the definition of “autonomous,”
agents are free to reject requests that they do not want to
honor. They are free to renegotiate the contract—“I can't provide
that, but if you give me this, then I might provide something else.”

<a id="d24e9822"></a>
Certainly any system that relies on agent technology has a
critical dependence on contractual arrangements—even
if they are dynamically generated.

<a id="d24e9827"></a>
Imagine: with enough components and agents that can negotiate their
own contracts among themselves to achieve a goal, we might just solve
the software productivity crisis by letting software solve it for us.

<a id="d24e9829"></a>
But if we can't use contracts by hand, we won't be able to use them
automatically. So next time you design a piece of software, design its
contract as well.

### Related Sections Include

- Topic 24, [*Dead Programs Tell No Lies*](<24 Dead Programs Tell No Lies - crash_early.md#crash_early>)
- Topic 25, [*Assertive Programming*](<25 Assertive Programming - assertions.md#assertions>)
- Topic 38, [*Programming by Coincidence*](<../07 While Coding/38 Programming by Coincidence - coincidence.md#coincidence>)
- Topic 42, [*Property-Based Testing*](<../07 While Coding/42 Property-Based Testing - proptest.md#proptest>)
- Topic 43, [*Stay Safe Out There*](<../07 While Coding/43 Stay Safe Out There - safety.md#safety>)
- Topic 45, [*The Requirements Pit*](<../08 Before the Project/45 The Requirements Pit - requirements.md#requirements>)

### Challenges

- Points to ponder: If DBC is so powerful, why isn't it used more
  widely? Is it hard to come up with the contract? Does it make you
  think about issues you'd rather ignore for now? Does it force you to
  THINK!? Clearly, this is a dangerous tool!

### Exercises

<a id="exercise-14"></a>
**Exercise 14** ([possible answer](<../A2 Exercise Answers/README.md#answer-14>))

<a id="d24e9893"></a>
Design an interface to a kitchen blender. It
will eventually be a web-based, IoT-enabled
blender, but for now we just need the interface to control it. It
has ten speed settings (0 means off). You can't operate it empty,
and you can change the speed only one unit at a time (that is, from
0 to 1, and from 1 to 2, not from 0 to 2).

<a id="d24e9909"></a>
Here are the methods. Add appropriate pre- and postconditions and an
invariant.

```
int getSpeed()
void setSpeed(int x)
boolean isFull()
void fill()
void empty()
```

<a id="exercise-15"></a>
**Exercise 15** ([possible answer](<../A2 Exercise Answers/README.md#answer-15>))

<a id="d24e9931"></a>
How many numbers are in the series 0, 5, 10, 15, …, 100?
