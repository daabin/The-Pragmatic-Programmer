Source: https://panzhongxian.cn/en/the-pragmatic-programmer/3_the_basic_tools.html#get_good_at_editing

<a id="get_good_at_editing"></a>
## Topic 18. Power Editing

<a id="d24e7413"></a>
We've talked before about tools being an extension of your hand. Well,
this applies to editors more than to any other software tool. You need
to be able to manipulate text as effortlessly as possible, because
text is the basic raw material of programming.

<a id="d24e7424"></a>
In the first edition of this book we recommended using a single editor
for everything: code, documentation, memos, system administration, and
so on. We've softened that position a little. We're happy for you to use
as many editors as you want. We'd just like you to be working toward fluency in each.

**Tip 27: Achieve Editor Fluency**

<a id="d24e7432"></a>
Why is this a big deal? Are we saying you'll save lots of time? Actually
yes: over the course of a year, you might actually gain an additional
week if you make your editing just 4% more efficient and you edit for 20
hours a week.

<a id="d24e7438"></a>
But that's not the real benefit. No, the major gain is that by becoming
fluent, you no longer have to think about the mechanics of editing. The
distance between thinking something and having it appear in an editor
buffer drop way down. Your thoughts will flow, and your programming will
benefit. (If you've ever taught someone to drive, then you'll
understand the difference between someone who has to think about every
action they take and a more experienced driver who controls the car instinctively.)

### What Does “Fluent” Mean?

<a id="d24e7445"></a>
What counts as being fluent? Here's the challenge list:

<a id="d24e7458"></a>
<a id="d24e7461"></a>
<a id="d24e7464"></a>
<a id="d24e7467"></a>
<a id="d24e7470"></a>
<a id="d24e7473"></a>
<a id="d24e7476"></a>
<a id="d24e7479"></a>
<a id="d24e7482"></a>
<a id="d24e7485"></a>
<a id="d24e7488"></a>
<a id="d24e7492"></a>
- When editing text, move and make selections by character,
  word, line, and paragraph.
- When editing code, move by various syntactic units (matching
  delimiters, functions, modules, …).
- Reindent code following changes.
- Comment and uncomment blocks of code with a single command.
- Undo and redo changes.
- Split the editor window into multiple panels, and navigate between
  them.
- Navigate to a particular line number.
- Sort selected lines.
- Search for both strings and regular expressions, and repeat previous
  searches.
- Temporarily create multiple cursors based on a selection or on a
  pattern match, and edit the text at each in parallel.
- Display compilation errors in the current project.
- Run the current project's tests.

<a id="d24e7494"></a>
Can you do all this without using a mouse/trackpad?

<a id="d24e7501"></a>
You might say that your current editor can't do some of these things. Maybe it's time to switch?

### Moving Toward Fluency

<a id="d24e7506"></a>
We doubt there are more than a handful of people who know all the commands in any particular powerful editor. We don't expect you to, either. Instead, we suggest a more pragmatic approach: learn the commands that make your life easier.

<a id="d24e7511"></a>
The recipe for this is fairly simple.

<a id="d24e7513"></a>
First, look at yourself while you're editing. Every time you find yourself doing something repetitive, get into the habit of thinking “there must be a better way.” Then find it.

<a id="d24e7515"></a>
Once you've discovered a new, useful feature, you now need to get it installed into your muscle memory, so you can use it without thinking. The only way we know to do that is through repetition. Consciously look for opportunities to use your new superpower, ideally many times a day. After a week or so, you'll find you use it without thinking.

#### Growing Your Editor

<a id="d24e7520"></a>
Most of the powerful code editors are built around a basic core that is then augmented through extensions. Many are supplied with the editor, and others can be added later.

<a id="d24e7531"></a>
When you bump into some apparent limitation of the editor you're using, search around for an extension that will do the job. The chances are that you are not alone in needing that capability, and if you're lucky someone else will have published their solution.

<a id="d24e7533"></a>
Take this a step further. Dig into your editor's extension language. Work out how to use it to automate some of the repetitive things you do. Often you'll just need a line or two of code.

<a id="d24e7535"></a>
Sometimes you might take it further still, and you'll find yourself writing a full-blown extension. If so, publish it: if you had a need for it, other people will, too.

### Related Sections Include

- Topic 7, [*Communicate!*](<../01 Pragmatic Philosophy/07 Communicate! - communicate.md#communicate>)

### Challenges

<a id="d24e7549"></a>
<a id="d24e7568"></a>
<a id="d24e7573"></a>
<a id="d24e7576"></a>
<a id="d24e7583"></a>
<a id="d24e7585"></a>
<a id="d24e7588"></a>
<a id="d24e7591"></a>
- No more autorepeat.

  Everyone does it: you need to delete the last word you typed, so you
  press down on backspace and wait for autorepeat to kick in.
  In fact, we bet that your brain has done this so much that you can
  judge pretty much exactly when to release the key.

  So turn off autorepeat, and instead learn the key sequences to move,
  select, and delete by characters, words, lines, and blocks.
- This one is going to hurt.

  Lose the mouse/trackpad. For one whole week, edit using just the
  keyboard. You'll discover a bunch of stuff that you can't do without
  pointing and clicking, so now's the time to learn. Keep notes (we
  recommend going old-school and using pencil and paper) of the key
  sequences you learn.

  You'll take a productivity hit for a few days. But, as you learn to do
  stuff without moving your hands away from the home position, you'll
  find that your editing becomes faster and more fluent than it ever
  was in the past.
- Look for integrations. While writing this chapter, Dave wondered if he
  could preview the final layout (a PDF file) in an editor buffer. One
  download later, the layout is sitting alongside the original text, all
  in the editor. Keep a list of things you'd like to bring into your
  editor, then look for them.
- Somewhat more ambitiously, if you can't find a plugin or extension
  that does what you want, write one. Andy is fond of making custom, local file-based Wiki plugins
  for his favorite editors. If you can't find it, build it!
