<a id="naming"></a>
## Topic 44. Naming Things

> The beginning of wisdom is to call things by their proper name.
>
> Confucius

<a id="d24e23783"></a>
What's in a name? When we're programming, the answer is “everything!”

<a id="d24e23794"></a>
We create names for applications, subsystems, modules, functions,
variables—we're constantly creating new things and bestowing names on
them. And those names are very, very important, because they reveal a
lot about your intent and belief.

<a id="d24e23800"></a>
We believe that things should be named according to the role they play
in your code. This means that, whenever you create something, you need
to pause and think “what is my motivation to create this?”

<a id="d24e23802"></a>
This is a powerful question, because it takes you out of the immediate
problem-solving mindset and makes you look at the bigger picture. When
you consider the role of a variable or function, you're thinking about
what is special about it, about what it can do, and what it interacts
with. Often, we find ourselves realizing that what we were about to do
made no sense, all because we couldn't come up with an appropriate name.

<a id="d24e23804"></a>
<a id="FNPTR-67"></a>
There's some science behind the idea that names are deeply meaningful.
It turns out that the brain can read and understand words really fast:
faster than many other activities. This means that words have a certain
priority when we try to make sense of something. This can be
demonstrated using the Stroop effect.[[67]](#FOOTNOTE-67)

<a id="d24e23811"></a>
<a id="FNPTR-68"></a>
Look at the following panel.
It has a list of color names or shades, and each is shown in a color or
shade. But the names and colors don't necessarily match. Here's part one
of the challenge—say aloud the name of each color as
written:[[68]](#FOOTNOTE-68)

<a id="d24e23822"></a>
![A figure shows the names of various colors such as, magenta, blue, red, green, yellow, cyan, and black. The color of the fonts may or may not represent the name of the color.](https://panzhongxian.cn/images/the-pragmatic-programmer/stroop_color.png)

<a id="d24e23825"></a>
Now repeat this, but instead say aloud the color used to draw the word.
Harder, eh? It's easy to be fluent when reading, but way harder when
trying to recognize colors.

<a id="d24e23828"></a>
Your brain treats written words as something to be respected. We need to
make sure the names we use live up to this.

<a id="d24e23830"></a>
Let's look at a couple of examples:

<a id="d24e23834"></a>
<a id="d24e23840"></a>
<a id="d24e23858"></a>
<a id="d24e23879"></a>
<a id="d24e23893"></a>
<a id="d24e23911"></a>
<a id="d24e23920"></a>
<a id="d24e23924"></a>
- We're authenticating people who access our site that sells jewelry
  made from old graphics cards:

  ```
  let user = authenticate(credentials)
  ```

  The variable is user because it's always user. But why? It means nothing. How about customer, or buyer? That way we
  get constant reminders as we code of what this person is trying to do,
  and what that means to us.
- We have an instance method that discounts an order:

  ```
  public void deductPercent(double amount)
      // ...
  ```

  Two things here. First, deductPercent is what it does and not why
  it does it. Then the name of the parameter amount is at best
  misleading: is it an absolute amount, a percentage?

  Perhaps this would be better:

  ```
  public void applyDiscount(Percentage discount)
    // ...
  ```

  The method name now makes its intent clear. We've also changed the
  parameter from a double to a Percentage, a type we've defined. We
  don't know about you, but when dealing with percentages we never know
  if the value is supposed to be between 0 and 100 or 0.0 and 1.0. Using
  a type documents what the function expects.
- We have a module that does interesting things with Fibonacci numbers.
  One of those things is to calculate the $n^{th}$ number in
  the sequence. Stop and think what you'd call this function.

  Most people we ask would call it fib. Seems reasonable, but remember
  it will normally be called in the context of its module, so the call
  would be Fib.fib(n). How about calling it of or nth
  instead:

  ```
  Fib.of(0)    # => 0
  Fib.nth(20)  # => 4181
  ```

<a id="d24e23954"></a>
When naming things, you're constantly looking for ways of clarifying
what you mean, and that act of clarification will lead you to a better
understanding of your code as you write it.

<a id="d24e23958"></a>
However, not all names have to be candidates for a literary prize.

<a id="d24e23963"></a>
<a id="d24e23988"></a>
<a id="d24e23993"></a>
The Exception That Proves the Rule

While we strive for clarity in code, branding is a different matter entirely.

There's a well-established tradition that projects and project teams
should have obscure, “clever” names. Names of Pokémon, Marvel
superheroes, cute mammals, Lord of the Rings characters, you name it.

Literally.

### Honor the Culture

<a id="d24e24002"></a>
<a id="FNPTR-69"></a>
Most introductory computer texts will admonish you never to use single letter variables such as i, j, or k.[[69]](#FOOTNOTE-69)

<a id="d24e24068"></a>
We think they're wrong. Sort of.

<a id="d24e24070"></a>
In fact, it depends on the culture of that particular programming language or environment. In the C programming language, i, j, and k are traditionally used as loop increment variables, s is used for a character string, and so on. If you program in that environment, that's what you are used to seeing and it would be jarring (and hence wrong) to violate that norm. On the other hand, using that convention in a different environment where it's not expected is just as wrong. You'd never do something heinous like this Clojure example which assigns a string to variable i:

```
(let [i "Hello World"]
        (println i))
```

<a id="d24e24103"></a>
Some language communities prefer camelCase, with embedded capital
letters, while others prefer snake\_case with embedded underscores to
separate words. The languages themselves will of course accept either,
but that doesn't make it right. Honor the local culture.

<a id="d24e24127"></a>
Some languages allow a subset of Unicode in names. Get a sense of what
the community expects before going all cute with names like ɹǝsn or
εξέρχεται.

### Consistency

<a id="d24e24140"></a>
Emerson is famous for writing “A foolish consistency is the hobgoblin of
little minds…,” but Emerson wasn't on a team of programmers.

<a id="d24e24149"></a>
Every project has its own vocabulary: jargon words that have a special
meaning to the team. “Order” means one thing to a team creating an
online store, and something very different to a team whose app charts
the lineage of religious groups. It's important that everyone on the
team knows what these words mean, and that they use them consistently.

<a id="d24e24155"></a>
One way is to encourage a lot of communication. If everyone pair
programs, and pairs switch frequently, then jargon will spread
osmotically.

<a id="d24e24161"></a>
Another way is to have a project glossary, listing the terms that have
special meaning to the team. This is an informal document, possibly
maintained on a wiki, possibly just index cards on a wall somewhere.

<a id="d24e24180"></a>
After a while, the project jargon will take on a life of its own. As
everyone gets comfortable with the vocabulary, you'll be able to use the
jargon as a shorthand, expressing a lot of meaning accurately and
concisely. (This is exactly what a pattern language is.)

### Renaming Is Even Harder

<a id="d24e24199"></a>
No matter how much effort you put in up front, things change. Code is refactored, usage shifts, meaning becomes subtly altered. If you aren't vigilant about updating names as you go, you can quickly descend into a nightmare much worse than meaningless names: misleading names. Have
you ever had someone explain inconsistencies in code such as,
“The routine called getData really writes data to an archive file”?

<a id="d24e24211"></a>
As we discuss in Topic 3, [*Software Entropy*](<../01 Pragmatic Philosophy/03 Software Entropy - no_broken_windows.md#no_broken_windows>), when you spot a problem, fix it—right here and now. When you see a name that no longer expresses the intent, or is misleading or confusing, fix it. You've got full regression tests, so you'll spot any instances you may have missed.

**Tip 74: Name Well; Rename When Needed**

<a id="d24e24230"></a>
If for some reason you can't change the now-wrong name, then you've got a bigger problem: an ETC violation (see Topic 8, [*The Essence of Good Design*](<../02 Pragmatic Approach/08 The Essence of Good Design - essence_of_design.md#essence_of_design>)). Fix that first, then change the offending name. Make renaming easy, and do it often.

<a id="d24e24241"></a>
Otherwise you'll have to explain to the new folks on the team that
getData really writes data to a file, and you'll have to do it with a straight face.

### Related Sections Include

- Topic 3, [*Software Entropy*](<../01 Pragmatic Philosophy/03 Software Entropy - no_broken_windows.md#no_broken_windows>)
- Topic 40, [*Refactoring*](<40 Refactoring - refactor.md#refactor>)
- Topic 45, [*The Requirements Pit*](<../08 Before the Project/45 The Requirements Pit - requirements.md#requirements>)

### Challenges

<a id="d24e24264"></a>
<a id="d24e24276"></a>
<a id="d24e24285"></a>
<a id="d24e24290"></a>
- When you find a function or method with an overly generic name, try
  and rename it to express all the things it really does. Now it's an
  easier target for refactoring.
- In our examples, we suggested using more specific names such as
  buyer instead of the more traditional and generic user. What other
  names do you habitually use that could be better?
- Are the names in your system congruent with user terms from the
  domain? If not, why? Does this cause a Stroop-effect style cognitive
  dissonance for the team?
- Are names in your system hard to change? What can you do to fix that
  particular broken window?

<a id="d24e19779"></a>
<a id="FOOTNOTE-50"></a>
<a id="d24e19806"></a>
<a id="FOOTNOTE-51"></a>
<a id="d24e19838"></a>
<a id="FOOTNOTE-52"></a>
<a id="d24e20031"></a>
<a id="FOOTNOTE-53"></a>
<a id="d24e20760"></a>
<a id="FOOTNOTE-54"></a>
<a id="d24e20868"></a>
<a id="FOOTNOTE-55"></a>
<a id="d24e21094"></a>
<a id="FOOTNOTE-56"></a>
<a id="d24e21113"></a>
<a id="FOOTNOTE-57"></a>
<a id="d24e21418"></a>
<a id="FOOTNOTE-58"></a>
<a id="d24e21550"></a>
<a id="FOOTNOTE-59"></a>
<a id="d24e21560"></a>
<a id="FOOTNOTE-60"></a>
<a id="d24e21590"></a>
<a id="FOOTNOTE-61"></a>
<a id="d24e23107"></a>
<a id="FOOTNOTE-62"></a>
<a id="d24e23245"></a>
<a id="FOOTNOTE-63"></a>
<a id="d24e23419"></a>
<a id="FOOTNOTE-64"></a>
<a id="d24e23629"></a>
<a id="FOOTNOTE-65"></a>
<a id="d24e23722"></a>
<a id="FOOTNOTE-66"></a>
<a id="d24e23809"></a>
<a id="FOOTNOTE-67"></a>
<a id="d24e23814"></a>
<a id="FOOTNOTE-68"></a>
<a id="d24e24054"></a>
<a id="FOOTNOTE-69"></a>
[[50]](<38 Programming by Coincidence - coincidence.md#FNPTR-50>)Note from the battle-scarred: UTC is there for a reason. Use it.

[[51]](<38 Programming by Coincidence - coincidence.md#FNPTR-51>)<https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation>

[[52]](<38 Programming by Coincidence - coincidence.md#FNPTR-52>)See Topic 50, [*Coconuts Don't Cut It*](<../09 Pragmatic Projects/50 Coconuts Don't Cut It - do_what_works.md#do_what_works>).

[[53]](<38 Programming by Coincidence - coincidence.md#FNPTR-53>)You can also go too far here. We once knew a developer who rewrote all source he was given because he had his own naming conventions.

[[54]](<39 Algorithm Speed - algorithm_speed.md#FNPTR-54>)<https://media-origin.pragprog.com/titles/tpp20/code/algorithm_speed/sort/src/main.rs>

[[55]](<40 Refactoring - refactor.md#FNPTR-55>)And yes, we did voice our concerns over the title.

[[56]](<40 Refactoring - refactor.md#FNPTR-56>)Originally spotted in [*UML Distilled: A Brief Guide to the Standard Object Modeling Language* [Fow00]](<../A2 Exercise Answers/README.md#d6040e349>).

[[57]](<40 Refactoring - refactor.md#FNPTR-57>)This is excellent advice in general (see Topic 27, [*Don't Outrun Your Headlights*](<../04 Pragmatic Paranoia/27 Don't Outrun Your Headlights - headlights.md#headlights>)).

[[58]](<41 Test to Code - test_to_build.md#FNPTR-58>)Some folks argue that test-first and test-driven development
are two different things, saying that the intents of
the two are different. However, historically, test-first (which
comes from eXtreme Programming) was identical to what people now
call TDD.

[[59]](<41 Test to Code - test_to_build.md#FNPTR-59>)<https://ronjeffries.com/categories/sudoku>. A big “thank you” to Ron for letting us use this story.

[[60]](<41 Test to Code - test_to_build.md#FNPTR-60>)<http://norvig.com/sudoku.html>

[[61]](<41 Test to Code - test_to_build.md#FNPTR-61>)We've been trying since at least 1986, when Cox and Novobilski
coined the term “software IC” in their Objective-C book
Object-Oriented Programming [*Object-Oriented Programming: An Evolutionary Approach* [CN91]](<../A2 Exercise Answers/README.md#d6040e197>).

[[62]](<43 Stay Safe Out There - safety.md#FNPTR-62>)See Topic 20, [*Debugging*](<../03 Basic Tools/20 Debugging - debug.md#debug>).

[[63]](<43 Stay Safe Out There - safety.md#FNPTR-63>)Remember our good friend, little Bobby Tables
(<https://xkcd.com/327>)? While you're reminiscing have a
look at <https://bobby-tables.com>, which lists ways of
sanitizing data passed to database queries.

[[64]](<43 Stay Safe Out There - safety.md#FNPTR-64>)This technique has proven to be successful at the CPU chip
level, where
well-known exploits target debugging and administrative facilities.
Once cracked, the entire machine is left exposed.

[[65]](<43 Stay Safe Out There - safety.md#FNPTR-65>)NIST Special Publication 800-63B: Digital Identity Guidelines: Authentication and Lifecycle Management, available free online at <https://doi.org/10.6028/NIST.SP.800-63b>

[[66]](<43 Stay Safe Out There - safety.md#FNPTR-66>)Unless you have a PhD in cryptography, and even then only with major peer review, extensive field trials with a bug bounty, and budget for long-term maintenance.

[[67]](#FNPTR-67)[*Studies of Interference in Serial Verbal Reactions* [Str35]](<../A2 Exercise Answers/README.md#d6040e892>)

[[68]](#FNPTR-68)We have two versions of this panel. One uses different colors, and the other uses shades of gray. If you're seeing this in black and white and want the color version, or if you're having trouble distinguishing colors and want to try the grayscale version, pop over to <https://pragprog.com/the-pragmatic-programmer/stroop-effect>.

[[69]](#FNPTR-69)Do you know why i is commonly used as a loop variable? The
answer comes from over 60 years ago, when variables starting with
I through N were integers in the original FORTRAN. And FORTRAN
was in turn influenced by algebra.
