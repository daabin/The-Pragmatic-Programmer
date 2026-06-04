---
sidebar_label: 4. Pragmatic Paranoia
---

## Topics

- [Topic 23. Design by Contract](<23 Design by Contract - dbc.md>)
- [Topic 24. Dead Programs Tell No Lies](<24 Dead Programs Tell No Lies - crash_early.md>)
- [Topic 25. Assertive Programming](<25 Assertive Programming - assertions.md>)
- [Topic 26. How to Balance Resources](<26 How to Balance Resources - balance_resources.md>)
- [Topic 27. Don't Outrun Your Headlights](<27 Don't Outrun Your Headlights - headlights.md>)

# Chapter 4 - Pragmatic Paranoia

**Tip 36: You Can't Write Perfect Software**

<a id="d24e8958"></a>
Did that hurt? It shouldn't. Accept it as an axiom of life. Embrace
it. Celebrate it. Because perfect software doesn't exist. No one in
the brief history of computing has ever written a piece of perfect
software. It's unlikely that you'll be the first. And unless you
accept this as a fact, you'll end up wasting time and energy
chasing an impossible dream.

<a id="d24e8964"></a>
So, given this depressing reality, how does a Pragmatic Programmer turn
it into an advantage? That's the topic of this chapter.

<a id="d24e8966"></a>
Everyone knows that they personally are the only good driver on Earth.
The rest of the world is out there to get them, blowing through stop
signs, weaving between lanes, not indicating turns, texting on the
phone, and just generally not living up to our
standards. So we drive defensively. We look out for trouble before it
happens, anticipate the unexpected, and never put ourselves into a
position from which we can't extricate ourselves.

<a id="d24e8968"></a>
The analogy with coding is pretty obvious. We are constantly interfacing
with other people's code—code that might not live up to our high
standards—and dealing with inputs that may or may not be valid. So we
are taught to code defensively. If there's any doubt, we validate all
information we're given. We use assertions to detect bad data, and distrust data from potential attackers or trolls. We check
for consistency, put constraints on database columns, and generally feel
pretty good about ourselves.

<a id="d24e8970"></a>
But Pragmatic Programmers take this a step further. They don't trust
themselves, either. Knowing that no one writes perfect code, including
themselves, Pragmatic Programmers build in defenses against their own
mistakes. We describe the first defensive measure in Topic 23, [*Design by Contract*](<23 Design by Contract - dbc.md#dbc>): clients and suppliers must agree on rights and
responsibilities.

<a id="d24e8986"></a>
In Topic 24, [*Dead Programs Tell No Lies*](<24 Dead Programs Tell No Lies - crash_early.md#crash_early>), we want to ensure that we do no
damage while we're working the bugs out. So we try to check things often
and terminate the program if things go awry.

<a id="d24e9002"></a>
Topic 25, [*Assertive Programming*](<25 Assertive Programming - assertions.md#assertions>) describes an easy method of checking
along the way—write code that actively verifies your assumptions.

<a id="d24e9026"></a>
As your programs get more dynamic, you'll find yourself juggling system
resources—memory, files, devices, and the like. In Topic 26, [*How to Balance Resources*](<26 How to Balance Resources - balance_resources.md#balance_resources>), we'll suggest ways of ensuring that you
don't drop any of the balls.

<a id="d24e9042"></a>
And most importantly, we stick to small steps always, as described in Topic 27, [*Don't Outrun Your Headlights*](<27 Don't Outrun Your Headlights - headlights.md#headlights>), so we don't fall off the edge of the cliff.

<a id="d24e9063"></a>
In a world of imperfect systems, ridiculous time scales, laughable
tools, and impossible requirements, let's play it safe. As Woody Allen said, “When everybody actually is out to get you, paranoia is just
good thinking.”
