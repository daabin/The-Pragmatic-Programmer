Source: https://panzhongxian.cn/en/the-pragmatic-programmer/2_a_pragmatic_approach.html#domain_languages

<a id="domain_languages"></a>
## Topic 14. Domain Languages

> The limits of language are the limits of one's world.
>
> Ludwig Wittgenstein

<a id="d24e5610"></a>
Computer languages influence how you think about a problem, and how
you think about communicating. Every language comes with a list of
features: buzzwords such as static versus dynamic typing, early versus
late binding, functional versus OO, inheritance models, mixins,
macros—all of which may suggest or obscure certain solutions. Designing
a solution with C++ in mind will produce different results than a
solution based on Haskell-style thinking, and vice versa. Conversely,
and we think more importantly, the language of the problem domain may
also suggest a programming solution.

<a id="d24e5629"></a>
We always try to write code using the vocabulary of the application
domain (see [*Maintain a Glossary*](<../08 Before the Project/45 The Requirements Pit - requirements.md#pglossary>)). In some cases, Pragmatic Programmers can go to the next
level and actually program using the vocabulary, syntax, and
semantics—the language—of the domain.

**Tip 22: Program Close to the Problem Domain**

### Some Real-World Domain Languages

<a id="d24e5642"></a>
Let's look at a few examples where folks have done just that.

#### RSpec

<a id="d24e5647"></a>
<a id="FNPTR-19"></a>
RSpec[[19]](<Topic 15. Estimating - learn_to_estimate.md#FOOTNOTE-19>) is a testing library for Ruby. It inspired
versions for most other modern languages. A test in RSpec is intended to
reflect the behavior you expect from your code.

```
describe BowlingScore do
  it "totals 12 if you score 3 four times" do
    score = BowlingScore.new
    4.times { score.add_pins(3) }
    expect(score.total).to eq(12)
  end
end
```

#### Cucumber

<a id="d24e5701"></a>
<a id="FNPTR-20"></a>
Cucumber[[20]](<Topic 15. Estimating - learn_to_estimate.md#FOOTNOTE-20>) is programming-language neutral way of
specifying tests. You run the tests using a version of Cucumber
appropriate to the language you're using. In order to support the
natural-language like syntax, you also have to write specific matchers
that recognize phrases and extract parameters for the tests.

```
Feature: Scoring

Background:
  Given an empty scorecard

Scenario: bowling a lot of 3s
  Given I throw a 3
  And I throw a 3
  And I throw a 3
  And I throw a 3
  Then the score should be 12
```

<a id="d24e5761"></a>
Cucumber tests were intended to be read by the customers of the software
(although that happens fairly rarely in practice; the following aside considers why that might be).

<a id="sb-cuc"></a>
<a id="d24e5770"></a>
<a id="d24e5790"></a>
<a id="d24e5792"></a>
Why Don't Many Business Users Read Cucumber Features?

One of the reasons that the classic gather requirements, design,
code, ship approach doesn't work is that it is anchored by the
concept that we know what the requirements are. But we rarely do. Your
business users will have a vague idea of what they want to achieve,
but they neither know nor care about the details. That's part of our
value: we intuit intent and convert it to code.

So when you force a business person to sign off on a requirements
document, or get them to agree to a set of Cucumber features, you're
doing the equivalent of getting them to check the spelling in an essay
written in Sumerian. They'll make some random changes to save face and
sign it off to get you out of their office.

Give them code that runs, however, and they can play with it. That's
where their real needs will surface.

#### Phoenix Routes

<a id="d24e5797"></a>
<a id="FNPTR-21"></a>
Many web frameworks have a routing facility, mapping incoming HTTP
requests onto handler functions in the code. Here's an example from
Phoenix.[[21]](<Topic 15. Estimating - learn_to_estimate.md#FOOTNOTE-21>)

```
scope "/", HelloPhoenix do
  pipe_through :browser # Use the default browser stack

  get "/", PageController, :index
  resources "/users", UserController
end
```

<a id="d24e5843"></a>
This says that requests starting “/” will be run through a series of
filters appropriate for browsers. A request to “/” itself will be
handled by the index function in the PageController module. The
UsersController implements the functions needed to manage a resource
accessible via the url /users.

#### Ansible

<a id="d24e5860"></a>
<a id="FNPTR-22"></a>
<a id="FNPTR-23"></a>
Ansible[[22]](<Topic 15. Estimating - learn_to_estimate.md#FOOTNOTE-22>) is a tool that configures software,
typically on a bunch of remote servers. It does this by reading a
specification that you provide, then doing whatever is needed on the
servers to make them mirror that spec. The specification can be written
in YAML,[[23]](<Topic 15. Estimating - learn_to_estimate.md#FOOTNOTE-23>) a language that builds data structures
from text descriptions:

```
---
- name: install nginx
  apt: name=nginx state=latest

- name: ensure nginx is running (and enable it at boot)
  service: name=nginx state=started enabled=yes

- name: write the nginx config file
  template: src=templates/nginx.conf.j2 dest=/etc/nginx/nginx.conf
  notify:
  - restart nginx
```

<a id="d24e5938"></a>
This example ensures that the latest version of nginx is installed on my
servers, that it is started by default, and that it uses a configuration
file that you've provided.

### Characteristics of Domain Languages

<a id="d24e5943"></a>
Let's look at these examples more closely.

<a id="d24e5945"></a>
RSpec and the Phoenix router are written in their host languages (Ruby
and Elixir). They employ some fairly devious code, including
metaprogramming and macros, but ultimately they are compiled
and run as regular code.

<a id="d24e5964"></a>
Cucumber tests and Ansible configurations are written in their own
languages. A Cucumber test is converted into code to be run
or into a datastructure, whereas Ansible specs are always converted into
a data structure that is run by Ansible itself.

<a id="d24e5976"></a>
As a result, RSpec and the router code are embedded into the code you
run: they are true extensions to your code's vocabulary. Cucumber and
Ansible are read by code and converted into some form the code can
use.

<a id="d24e5981"></a>
We call RSpec and the router examples of internal domain languages,
while Cucumber and Ansible use external languages.

### Trade-Offs Between Internal and External Languages

<a id="d24e6007"></a>
In general, an internal domain language can take advantage of the
features of its host language: the domain language you create is more
powerful, and that power comes for free. For example, you could use some
Ruby code to create a bunch of RSpec tests automatically. In this case
we can test scores where there are no spares or strikes:

```
describe BowlingScore do
  (0..4).each do |pins|
    (1..20).each do |throws|
      target = pins * throws

      it "totals #{target} if you score #{pins} #{throws} times" do
        score = BowlingScore.new
        throws.times { score.add_pins(pins) }
        expect(score.total).to eq(target)
      end
    end
  end
end
```

<a id="d24e6100"></a>
That's 100 tests you just wrote. Take the rest of the day off.

<a id="d24e6102"></a>
The downside of internal domain languages is that you're bound by the
syntax and semantics of that language. Although some languages are
remarkably flexible in this regards, you're still forced to compromise
between the language you want and the language you can implement.

<a id="d24e6104"></a>
Ultimately, whatever you come up with must still be valid syntax in your
target language. Languages with macros (such as Elixir, Clojure, and
Crystal) gives you a little more flexibility, but ultimately syntax is syntax.

<a id="d24e6106"></a>
External languages have no such restrictions. As long as you can write a
parser for the language, you're good to go. Sometimes you can use
someone else's parser (as Ansible did by using YAML), but then you're
back to making a compromise.

<a id="d24e6112"></a>
Writing a parser probably means adding new libraries and possibly tools
to your application. And writing a good parser is not a trivial job.
But, if you're feeling stout of heart, you could look at parser
generators such as bison or ANTLR, and parsing frameworks such as the
many PEG parsers out there.

<a id="d24e6132"></a>
Our suggestion is fairly simple: don't spend more effort than you save.
Writing a domain language adds some cost to your project, and you'll
need to be convinced that there are offsetting savings (potentially in
the long term).

<a id="d24e6135"></a>
In general, use off-the-shelf external languages (such as YAML, JSON, or CSV) if you can. If not, look at internal languages. We'd recommend using external languages only in cases where your language will be written by the users of your application.

### An Internal Domain Language on the Cheap

<a id="d24e6152"></a>
Finally, there's a cheat for creating internal domain languages if you don't mind the host language syntax leaking through. Don't do a bunch of metaprogramming. Instead, just write functions to do the work. In fact, this is pretty much what RSpec does:

```
describe BowlingScore do
  it "totals 12 if you score 3 four times" do
    score = BowlingScore.new
    4.times { score.add_pins(3) }
    expect(score.total).to eq(12)
  end
end
```

<a id="d24e6198"></a>
In this code, describe, it, expect, to, and eq are just Ruby methods. There's a little plumbing behind the scenes in terms of how objects are passed around, but it's all just code.
We'll explore that a little in the exercises.

### Related Sections Include

- Topic 8, [*The Essence of Good Design*](<08 The Essence of Good Design - essence_of_design.md#essence_of_design>)
- Topic 13, [*Prototypes and Post-it Notes*](<13 Prototypes and Post-it Notes - prototyping.md#prototyping>)
- Topic 32, [*Configuration*](<../05 Bend or Break/32 Configuration - configuration.md#configuration>)

### Challenges

<a id="d24e6233"></a>
<a id="d24e6255"></a>
- Could some of the requirements of your current project be
  expressed in a domain-specific language? Would it be possible to
  write a compiler or translator that could generate most of the code
  required?
- If you decide to adopt mini-languages as a way of programming
  closer to the problem domain, you're accepting that some effort will
  be required to implement them. Can you see ways in which the
  framework you develop for one project can be reused in others?

### Exercises

<a id="exercise-4"></a>
**Exercise 4** ([possible answer](<../A2 Exercise Answers/README.md#answer-4>))

<a id="d24e6276"></a>
We want to implement a mini-language to control a simple turtle-graphics system. The language consists of
single-letter commands, some followed by a single number.
For example, the following input would draw a rectangle:

```
P 2  # select pen 2
D    # pen down
W 2  # draw west 2cm
N 1  # then north 1
E 2  # then east 2
S 1  # then back south
U    # pen up
```

<a id="d24e6311"></a>
Implement the code that parses this language. It should be designed so
that it is simple to add new commands.

<a id="exercise-5"></a>
**Exercise 5** ([possible answer](<../A2 Exercise Answers/README.md#answer-5>))

<a id="d24e6321"></a>
In the previous exercise we implemented a parser for the drawing language—it was an external domain language. Now implement it again as an internal language. Don't do anything clever: just write a function for each of the commands. You may have to change the names of the commands to lower case, and maybe to wrap them inside something to provide some context.

<a id="exercise-6"></a>
**Exercise 6** ([possible answer](<../A2 Exercise Answers/README.md#answer-6>))

<a id="d24e6331"></a>
Design a BNF grammar to parse a time specification. All
of the following examples should be accepted:

```
4pm, 7:38pm, 23:42, 3:16, 3:16am
```

<a id="exercise-7"></a>
**Exercise 7** ([possible answer](<../A2 Exercise Answers/README.md#answer-7>))

<a id="d24e6353"></a>
Implement a parser for the BNF grammar in the previous exercise
using a PEG parser generator in the language of your choice.
The output should be an integer containing the number of minutes past midnight.

<a id="exercise-8"></a>
**Exercise 8** ([possible answer](<../A2 Exercise Answers/README.md#answer-8>))

<a id="d24e6370"></a>
Implement the time parser using a scripting language and regular expressions.
