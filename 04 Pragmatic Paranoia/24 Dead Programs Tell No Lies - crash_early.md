<a id="crash_early"></a>
## Topic 24. Dead Programs Tell No Lies

<a id="d24e9942"></a>
Have you noticed that sometimes other people can detect that things
aren't well with you before you're aware of the problem yourself? It's
the same with other people's code. If something is starting to go awry
with one of our programs, sometimes it is a library or framework routine
that catches it first. Maybe we've passed in a nil value, or an empty
list. Maybe there's a missing key in that hash, or the value we thought
contained a hash really contains a list instead. Maybe there was a
network error or filesystem error that we didn't catch, and we've got
empty or corrupted data. A logic error a couple of million instructions
ago means that the selector for a case statement is no longer the
expected 1, 2, or 3. We'll hit the default case unexpectedly. That's
also one reason why each and every case/switch statement needs to have a
default clause: we want to know when the “impossible” has happened.

<a id="d24e9962"></a>
It's easy to fall into the “it can't happen” mentality.
Most of us have written code that didn't check that a file closed
successfully, or that a trace statement got written as we expected.
And all things being equal, it's likely that we didn't need to—the
code in question wouldn't fail under any normal conditions. But we're
coding defensively. We're making sure that the data is what we think it is, that the code in production is the code we think it is.
We're checking that the correct
versions of dependencies were actually loaded.

<a id="d24e9968"></a>
All errors give you information. You could convince yourself that the
error can't happen, and choose to ignore it. Instead, Pragmatic Programmers tell
themselves that if there is an error, something very, very bad has
happened. Don't forget to Read the Damn Error Message (see [*Coder in a Strange Land*](<../03 Basic Tools/20 Debugging - debug.md#readerror>)).

### Catch and Release Is for Fish

<a id="d24e9989"></a>
Some developers feel that is it good style to catch or rescue all
exceptions, re-raising them after writing some kind of message. Their
code is full of things like this (where a bare raise statement reraises the current exception):

```
try do
   add_score_to_board(score);
rescue InvalidScore
   Logger.error("Can't add invalid score. Exiting");
   raise
rescue BoardServerDown
   Logger.error("Can't add score: board is down. Exiting");
   raise
rescue StaleTransaction
   Logger.error("Can't add score: stale transaction. Exiting");
   raise
end
```

<a id="d24e10057"></a>
Here's how Pragmatic Programmers would write this:

```
add_score_to_board(score);
```

<a id="d24e10063"></a>
We prefer it for two reasons. First, the application code isn't eclipsed
by the error handling. Second, and perhaps more important, the code is
less coupled. In the verbose example, we have to list every exception
the add\_score\_to\_board method could raise. If the writer of that
method adds another exception, our code is subtly out of date. In the
more pragmatic second version, the new exception is automatically
propagated.

**Tip 38: Crash Early**

<a id="crash_discuss"></a>
### Crash, Don't Trash

<a id="d24e10088"></a>
One of the benefits of detecting problems as soon as you can is that
you can crash earlier, and crashing is often the
best thing you can do. The alternative may be to continue, writing
corrupted data to some vital database or commanding the washing
machine into its twentieth consecutive spin cycle.

<a id="d24e10090"></a>
The Erlang and Elixir languages embrace this philosophy. Joe Armstrong,
inventor of Erlang and author of [*Programming Erlang: Software for a Concurrent World* [Arm07]](<../A2 Exercise Answers/README.md#d6040e93>), is
often quoted as saying, “Defensive programming is a waste of time. Let
it crash!” In these environments, programs are designed to fail, but that
failure is managed with supervisors. A supervisor is responsible for
running code and knows what to do in case the code fails, which could
include cleaning up after it, restarting it, and so on. What happens
when the supervisor itself fails? Its own supervisor manages that event,
leading to a design composed of supervisor trees. The technique is
very effective and helps to account for the use of these languages in
high-availability, fault-tolerant systems.

<a id="d24e10122"></a>
In other environments, it may be inappropriate simply to exit a running
program. You may have claimed resources that might not get released,
or you may need to write log messages, tidy up open transactions, or
interact with other processes.

<a id="d24e10124"></a>
However, the basic principle stays
the same—when your code discovers that something that was supposed
to be impossible just happened, your program is no longer viable.
Anything it does from this point forward becomes suspect, so terminate
it as soon as possible.

<a id="d24e10126"></a>
A dead program
normally does a lot less damage than a crippled one.

### Related Sections Include

- Topic 20, [*Debugging*](<../03 Basic Tools/20 Debugging - debug.md#debug>)
- Topic 23, [*Design by Contract*](<23 Design by Contract - dbc.md#dbc>)
- Topic 25, [*Assertive Programming*](<25 Assertive Programming - assertions.md#assertions>)
- Topic 26, [*How to Balance Resources*](<26 How to Balance Resources - balance_resources.md#balance_resources>)
- Topic 43, [*Stay Safe Out There*](<../07 While Coding/43 Stay Safe Out There - safety.md#safety>)
