Source: https://panzhongxian.cn/en/the-pragmatic-programmer/5_bend_or_break.html#function_pipelines

<a id="function_pipelines"></a>
## Topic 30. Transforming Programming

> If you can't describe what you are doing as a process, you don't know what you're doing.
>
> W. Edwards Deming, (attr)

<a id="d24e13819"></a>
All programs transform data, converting an input into an output. And yet
when we think about design, we rarely think about creating
transformations. Instead we worry about classes and modules, data
structures and algorithms, languages and frameworks.

<a id="d24e13838"></a>
We think that this focus on code often misses the point: we need to get
back to thinking of programs as being something that transforms inputs
into outputs. When we do, many of the details we previously worried
about just evaporate. The structure becomes clearer, the error handling
more consistent, and the coupling drops way down.

<a id="d24e13840"></a>
To start our investigation, let's take the time machine back to the
1970s and ask a Unix programmer to write us a program that lists the
five longest files in a directory tree, where longest means “having the
largest number of lines.”

<a id="d24e13846"></a>
You might expect them to reach for an editor and start typing in C. But
they wouldn't, because they are thinking about this in terms of what we
have (a directory tree) and what we want (a list of files). Then they'd
go to a terminal and type something like:

```
$ find . -type f | xargs wc -l | sort -n | tail -5
```

<a id="d24e13909"></a>
This is a series of transformations:

<a id="d24e13916"></a>
<a id="d24e13928"></a>
<a id="d24e13943"></a>
<a id="d24e13952"></a>
find . -type f
:   Write a list of all the files (-type f) in or below the current
    directory (.) to standard output.

xargs wc -l
:   Read lines from standard input and arrange for them all to be passed
    as arguments to the command wc -l. The wc program with the -l
    option counts the number of lines in each of its arguments and writes
    each
    result as “count filename” to standard output.

sort -n
:   Sort standard input assuming each line starts with a number (-n),
    writing the result to standard output.

tail -5
:   Read standard input and write just the last five lines to standard
    output.

<a id="d24e13954"></a>
Run this in our book's directory and we get

```
 470 ./test_to_build.pml
 487 ./dbc.pml
 719 ./domain_languages.pml
 727 ./dry.pml
9561 total
```

<a id="d24e13969"></a>
That last line is the total number of lines in all the files (not just
those shown), because that's what wc does. We can strip it off by
requesting one more line from tail, and then ignoring the last line:

```
$ find . -type f | xargs wc -l | sort -n | tail -6 | head -5
     470 ./debug.pml
     470 ./test_to_build.pml
     487 ./dbc.pml
     719 ./domain_languages.pml
     727 ./dry.pml
```

<a id="fig.find"></a>
<a id="d24e14067"></a>
<a id="awc-pipeline"></a>
![A pipeline diagram depicts the series of transformations.](https://panzhongxian.cn/images/the-pragmatic-programmer/wc-pipeline.png)

Figure 1. The find pipeline as a series of transformations

A pipeline diagram describes a series of transformations. The approach is from top to bottom. First, find the name of the directory from where the file names should be taken. The wc program is used to sort a list of lines and names. The tail portion consist of only the last five lines. Last five plus total equals the head portion. From the head portion, last five lines are taken.

<a id="d24e14068"></a>
Let's look at this in terms of the data that flows between the
individual steps.
Our original requirement, “top 5 files in terms of lines,” becomes a
series of transformations (also show in [the figure](#fig.find)).

<a id="d24e14073"></a>
directory name
→ list of files
→ list with line numbers
→ sorted list
→ highest five + total
→ highest five

<a id="d24e14085"></a>
It's almost like an industrial assembly line: feed raw data in one end
and the finished product (information) comes out the other.

<a id="d24e14087"></a>
And we like to think about all code this way.

**Tip 49: Programming Is About Code, But Programs Are About Data**

### Finding Transformations

<a id="d24e14103"></a>
Sometimes the easiest way to find the transformations is to start with
the requirement and determine its inputs and outputs. Now you've
defined the function representing the overall program. You can then
find steps that lead you from input to output. This is a top-down
approach.

<a id="d24e14112"></a>
For example, you want to create a website for folks playing word
games that finds all the words that can be made from a set of letters.
Your input here is a set of letters, and your output is a list of three-letter words, four-letter words, and so on:

|  |  |  |
| --- | --- | --- |
| "lvyin" | is transformed to → | 3 => ivy, lin, nil, yin  4 => inly, liny, viny  5 => vinyl |

<a id="d24e14131"></a>
(Yes, they are all words, at least according to the macOS dictionary.)

<a id="d24e14133"></a>
The trick behind the overall application is simple: we have a dictionary
which groups words by a signature, chosen so that all words containing
the same letters will have the same signature. The simplest signature
function is just the sorted list of letters in the word. We can then
look up an input string by generating a signature for it, and then
seeing which words (if any) in the dictionary have that same signature.

<a id="d24e14140"></a>
Thus the anagram finder breaks down into four separate
transformations:

| Step | Transformation | Sample data |
| --- | --- | --- |
| Step 0: | Initial input | "ylvin" |
| Step 1: | All combinations of three or more letters | vin, viy, vil, vny, vnl, vyl, iny, inl, iyl, nyl, viny, vinl, viyl, vnyl, inyl, vinyl |
| Step 2: | Signatures of the combinations | inv, ivy, ilv, nvy, lnv, lvy, iny, iln, ily, lny, invy, ilnv, ilvy, lnvy, ilny, ilnvy |
| Step 3: | List of all dictionary words which match any of the signatures | ivy, yin, nil, lin, viny, liny, inly, vinyl |
| Step 4: | Words grouped by length | 3 => ivy, lin, nil, yin  4 => inly, liny, viny  5 => vinyl |

#### Transformations All the Way Down

<a id="d24e14199"></a>
Let's start by looking at step 1, which takes a word and creates a list
of all combinations of three or more letters. This step can itself be
expressed as a list of transformations:

| Step | Transformation | Sample data |
| --- | --- | --- |
| Step 1.0: | Initial input | "vinyl" |
| Step 1.1: | Convert to characters | v, i, n, y, l |
| Step 1.2: | Get all subsets | [], [v], [i], … [v,i], [v,n], [v,y], … [v,i,n], [v,i,y], … [v,n,y,l], [i,n,y,l], [v,i,n,y,l] |
| Step 1.3: | Only those longer than three characters | [v,i,n], [v,i,y], … [i,n,y,l], [v,i,n,y,l] |
| Step 1.4: | Convert back to strings | [vin,viy, … inyl,vinyl] |

<a id="d24e14247"></a>
We've now reached the point where we can easily implement each
transformation in code (using Elixir in this case):

[function-pipelines/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

```
defp all_subsets_longer_than_three_characters(word) do
  word
  |> String.codepoints()
  |> Comb.subsets()
  |> Stream.filter(fn subset -> length(subset) >= 3 end)
  |> Stream.map((1))
end
```

#### What's with the |> Operator?

<a id="d24e14301"></a>
<a id="FNPTR-41"></a>
Elixir, along with many other functional languages, has a pipeline
operator, sometimes called a forward pipe or just
a pipe.[[41]](<Topic 32. Configuration - configuration.md#FOOTNOTE-41>) All it does is take the value on its
left and insert it as the
first parameter of the function on its right, so

```
"vinyl" |> String.codepoints |> Comb.subsets()
```

<a id="d24e14374"></a>
is the same as writing

```
Comb.subsets(String.codepoints("vinyl"))
```

<a id="d24e14385"></a>
(Other languages may inject this piped value as the last parameter of
the next function—it largely depends on the style of the built-in
libraries.)

<a id="d24e14390"></a>
You might think that this is just syntactic sugar. But in a very real
way the pipeline operator is a revolutionary opportunity
to think differently. Using a pipeline means that you're automatically
thinking in terms of transforming data; each time you see |> you're
actually seeing a place where data is flowing between one transformation
and the next.

<a id="d24e14395"></a>
Many languages have something similar: Elm, and F# have |>, Clojure has -> and ->> (which work a little differently), R has %>%. Haskell both has pipe operators and makes it easy to declare new ones. As we write this, there's talk of adding |> to JavaScript.

<a id="d24e14485"></a>
If your current language supports something similar, you're in luck. If
it doesn't, see [*Language X Doesn't Have Pipelines*](#sb-no-pipelines).

<a id="d24e14490"></a>
Anyway, back to the code.

#### Keep on Transforming…

<a id="d24e14495"></a>
Now look at Step 2 of the main program, where we convert the subsets
into signatures. Again, it's a simple transformation—a list of subsets
becomes a list of signatures:

| Step | Transformation | Sample data |
| --- | --- | --- |
| Step 2.0: | initial input | vin, viy, … inyl, vinyl |
| Step 2.1: | convert to signatures | inv, ivy … ilny, inlvy |

<a id="d24e14525"></a>
The Elixir code in the following listing is just as simple:

[function-pipelines/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

```
defp as_unique_signatures(subsets) do
  subsets
  |> Stream.map(/1)
end
```

<a id="d24e14543"></a>
Now we transform that list of signatures: each signature gets mapped to
the list of known words with the same signature, or nil if there are
no such words. We then have to remove the nils and flatten the nested
lists into a single level:

[function-pipelines/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

```
defp find_in_dictionary(signatures) do
  signatures
  |> Stream.map(/1)
  |> Stream.reject(/1)
  |> Stream.concat((1))
end
```

<a id="d24e14573"></a>
Step 4, grouping the words by length, is another simple transformation,
converting our list into a map where the keys are the lengths, and the
values are all words with that length:

[function-pipelines/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

```
defp group_by_length(words) do
  words
  |> Enum.sort()
  |> Enum.group_by(/1)
end
```

<a id="sb-no-pipelines"></a>
<a id="d24e14596"></a>
<a id="d24e14621"></a>
<a id="d24e14637"></a>
Language X Doesn't Have Pipelines

Pipelines have been around for a long time, but only in niche languages. They've only moved into the mainstream recently, and many popular languages still don't support the concept.

The good news is that thinking in transformations doesn't require a particular language syntax: it's more a philosophy of design. You still construct your code as transformations, but you write them as a series of assignments:

```
const content = File.read(file_name);
const lines   = find_matching_lines(content, pattern)
const result  = truncate_lines(lines)
```

It's a little more tedious, but it gets the job done.

#### Putting It All Together

<a id="d24e14643"></a>
We've written each of the individual transformations. Now it's time to
string them all together into our main function:

[function-pipelines/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

```
  def anagrams_in(word) do
    word
    |> all_subsets_longer_than_three_characters()
    |> as_unique_signatures()
    |> find_in_dictionary()
    |> group_by_length()
end
```

<a id="d24e14667"></a>
Does it work? Let's try it:

```
iex(1)> Anagrams.anagrams_in "lyvin"
%{
  3 => ["ivy", "lin", "nil", "yin"],
  4 => ["inly", "liny", "viny"],
  5 => ["vinyl"]
}
```

<a id="pg-donthoard"></a>
### Why Is This So Great?

<a id="d24e14692"></a>
Let's look at the body of the main function again:

```
word
|> all_subsets_longer_than_three_characters()
|> as_unique_signatures()
|> find_in_dictionary()
|> group_by_length()
```

<a id="d24e14706"></a>
It's simply a chain of the transformations needed to meet our
requirement, each taking input from the previous transformation and
passing output to the next. That comes about as close to literate code
as you can get.

<a id="d24e14708"></a>
But there's something deeper, too. If your background is object-oriented
programming, then your reflexes demand that you hide data, encapsulating
it inside objects. These objects then chatter back and forth, changing
each other's state. This introduces a lot of coupling, and it is a big
reason that OO systems can be hard to change.

**Tip 50: Don't Hoard State; Pass It Around**

<a id="d24e14729"></a>
In the transformational model, we turn that on its head. Instead of little pools of data spread all over the system, think of data as a mighty river, a flow. Data becomes a
peer to functionality: a pipeline is a sequence of code → data →
code → data…. The data is no longer tied to a particular group of
functions, as it is in a class definition. Instead it is free to
represent the unfolding progress of our application as it transforms
its inputs into its outputs. This means that we can greatly reduce
coupling: a function can be used (and reused) anywhere its parameters
match the output of some other function.

<a id="d24e14734"></a>
Yes, there is still a degree of coupling, but in our experience it's
more manageable than the OO-style of command and control. And, if you're
using a language with type checking, you'll get compile-time warnings
when you try to connect two incompatible things.

### What About Error Handling?

<a id="d24e14746"></a>
So far our transforms have worked in a world where nothing goes wrong.
How can we use them in the real world, though? If we can only build
linear chains, how can we add all that conditional logic that we need
for error checking?

<a id="d24e14752"></a>
There are many ways of doing this, but they all rely on a basic
convention: we never pass raw values between transformations. Instead,
we wrap them in a data structure (or type) which also tells us if the
contained value is valid. In Haskell, for example, this wrapper is
called Maybe. In F# and Scala it's Option.

<a id="d24e14769"></a>
How you use this concept is language specific. In general, though, there
are two basic ways of writing the code: you can handle checking for
errors inside your transformations or outside them.

<a id="d24e14771"></a>
Elixir, which we've used so far, doesn't have this support built in. For
our purposes this is a good thing, as we get to show an implementation
from the ground up. Something similar should work in most other
languages.

#### First, Choose a Representation

<a id="d24e14780"></a>
We need a representation for our wrapper (the data structure that
carries around a value or an error indication). You can use structures
for this, but Elixir already has a pretty strong convention: functions
tend to return a tuple containing either {:ok, value} or {:error,
reason}. For example, File.open returns either :ok and an IO
process or :error and a reason code:

```
iex(1)> File.open("/etc/passwd")
{:ok, #PID
```

<a id="d24e14823"></a>
We'll use the :ok/:error tuple as our wrapper when passing things
through a pipeline.

#### Then Handle It Inside Each Transformation

<a id="d24e14834"></a>
Let's write a function that returns all the lines in a file that contain
a given string, truncated to the first 20 characters. We want to write
it as a transformation, so the input will be a file name and a string to
match, and the output will be either an :ok tuple with a list of lines
or an :error tuple with some kind of reason. The top-level function
should look something like this:

[function-pipelines/anagrams/lib/grep.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/grep.ex)

```
def find_all(file_name, pattern) do
  File.read(file_name)
  |> find_matching_lines(pattern)
  |> truncate_lines()
end
```

<a id="d24e14859"></a>
<a id="FNPTR-42"></a>
There's no explicit error checking here, but if any step in the pipeline
returns an error tuple then the pipeline will return that error without
executing the functions that follow.[[42]](<Topic 32. Configuration - configuration.md#FOOTNOTE-42>) We do this using Elixir's
pattern matching:

[function-pipelines/anagrams/lib/grep.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/grep.ex)

```
defp find_matching_lines({:ok, content}, pattern) do
  content
  |> String.split(~r/\n/)
  |> Enum.filter(?(1, pattern))
  |> ok_unless_empty()
end

defp find_matching_lines(error, _), do: error

# ----------

defp truncate_lines({ :ok, lines }) do
  lines
  |> Enum.map((1, 0, 20))
  |> ok()
end

defp truncate_lines(error), do: error

# ----------

defp ok_unless_empty([]),     do: error("nothing found")
defp ok_unless_empty(result), do: ok(result)

defp ok(result),    do: { :ok,    result }
defp error(reason), do: { :error, reason }
```

<a id="d24e14996"></a>
Have a look at the function find\_matching\_lines. If its first
parameter is an :ok tuple, it uses the content in that tuple to find
lines matching the pattern. However, if the first parameter is not an
:ok tuple, the second version of the function runs, which just returns
that parameter. This way the function simply forwards an error down the
pipeline. The same thing applies to truncate\_lines.

<a id="d24e15013"></a>
We can play with this at the console:

```
iex> Grep.find_all "/etc/passwd", ~r/www/
{:ok, ["_www:*:70:70:World W", "_wwwproxy:*:252:252:"]}
```

```
iex> Grep.find_all "/etc/passwd", ~r/wombat/
{:error, "nothing found"}
iex> Grep.find_all "/etc/koala", ~r/www/
{:error, :enoent}
```

<a id="d24e15066"></a>
You can see that an error anywhere in the pipeline immediately becomes
the value of the pipeline.

#### Or Handle It in the Pipeline

<a id="d24e15071"></a>
You might be looking at the find\_matching\_lines and truncate\_lines
functions thinking that we've moved the burden of error handling into
the transformations. You'd be right. In a language which uses pattern
matching in function calls, such as Elixir, the effect is lessened, but
it's still ugly.

<a id="d24e15079"></a>
<a id="FNPTR-43"></a>
It would be nice if Elixir had a version of the pipeline operator |>
that knew about the :ok/:error tuples and which short-circuited
execution when an error occurred.[[43]](<Topic 32. Configuration - configuration.md#FOOTNOTE-43>) But the fact that it
doesn't allows us to add something similar, and in a way that is
applicable to a number of other languages.

<a id="d24e15118"></a>
The problem we face is that when an error occurs we don't want to run
code further down the pipeline, and that we don't want that code to know
that this is happening. This means that we need to defer running
pipeline functions until we know that previous steps in the pipeline
were successful. To do this, we'll need to change them from function
calls into function values that can be called later. Here's one
implementation:

[function-pipelines/anagrams/lib/grep1.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/grep1.ex)

```
defmodule Grep1 do

  def and_then({ :ok, value }, func), do: func.(value)
  def and_then(anything_else, _func), do: anything_else

  def find_all(file_name, pattern) do
    File.read(file_name)
    |> and_then((1, pattern))
    |> and_then((1))
  end

  defp find_matching_lines(content, pattern) do
    content
    |> String.split(~r/\n/)
    |> Enum.filter(?(1, pattern))
    |> ok_unless_empty()
  end

  defp truncate_lines(lines) do
    lines
    |> Enum.map((1, 0, 20))
    |> ok()
  end

  defp ok_unless_empty([]),     do: error("nothing found")
  defp ok_unless_empty(result), do: ok(result)

  defp ok(result),    do: { :ok, result }
  defp error(reason), do: { :error, reason }
end
```

<a id="d24e15290"></a>
The and\_then function is an example of a bind function: it takes a
value wrapped in something, then applies a function to that value,
returning a new wrapped value. Using the and\_then function in the
pipeline takes a little extra punctuation because Elixir needs to be
told to convert function calls into function values, but that extra
effort is offset by the fact that the transforming functions become
simple: each just takes a value (and any extra parameters) and returns
{:ok, new\_value} or {:error, reason}.

### Transformations Transform Programming

<a id="d24e15341"></a>
Thinking of code as a series of (nested) transformations can be a
liberating approach to programming. It takes a while to get used to, but
once you've developed the habit you'll find your code becomes cleaner,
your functions shorter, and your designs flatter.

<a id="d24e15343"></a>
Give it a try.

### Related Sections Include

- Topic 8, [*The Essence of Good Design*](<../02 Pragmatic Approach/08 The Essence of Good Design - essence_of_design.md#essence_of_design>)
- Topic 17, [*Shell Games*](<../03 Basic Tools/17 Shell Games - know_your_shell.md#know_your_shell>)
- Topic 26, [*How to Balance Resources*](<../04 Pragmatic Paranoia/26 How to Balance Resources - balance_resources.md#balance_resources>)
- Topic 28, [*Decoupling*](<28 Decoupling - coupling.md#coupling>)
- Topic 35, [*Actors and Processes*](<../06 Concurrency/35 Actors and Processes - actor_model.md#actor_model>)

### Exercises

<a id="exercise-21"></a>
**Exercise 21** ([possible answer](<../A2 Exercise Answers/README.md#answer-21>))

<a id="d24e15375"></a>
Can you express the following requirements as a top-level
transformation? That is, for each, identify the input and the output.

1. Shipping and sales tax are added to an order
2. Your application loads configuration information from a named
   file
3. Someone logs in to a web application

<a id="exercise-22"></a>
**Exercise 22** ([possible answer](<../A2 Exercise Answers/README.md#answer-22>))

<a id="d24e15399"></a>
You've identified the need to validate and convert an input field from a
string into an integer between 18 and 150. The overall transformation is described by

```
field contents as string
    → [validate  convert]
        → {:ok, value} | {:error, reason}
```

<a id="d24e15409"></a>
Write the individual transformations that make up validate & convert.

<a id="exercise-23"></a>
**Exercise 23** ([possible answer](<../A2 Exercise Answers/README.md#answer-23>))

<a id="d24e15422"></a>
In [*Language X Doesn't Have Pipelines*](#sb-no-pipelines) we wrote:

```
const content = File.read(file_name);
const lines   = find_matching_lines(content, pattern)
const result  = truncate_lines(lines)
```

<a id="d24e15441"></a>
Many people write OO code by chaining together method calls, and might
be tempted to write this as something like:

```
const result = content_of(file_name)
               .find_matching_lines(pattern)
               .truncate_lines()
```

<a id="d24e15457"></a>
What's the difference between these two pieces of code? Which do you
think we prefer?
