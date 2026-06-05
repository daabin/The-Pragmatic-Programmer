<a id="plain_text"></a>
## Topic 16. The Power of Plain Text

<a id="d24e6849"></a>
As Pragmatic Programmers, our base material isn't wood or iron, it's
knowledge. We gather requirements as knowledge, and then express that
knowledge in our designs, implementations, tests, and documents. And we
believe that the best format for storing knowledge persistently is
plain text. With plain text, we give ourselves the ability to
manipulate knowledge, both manually and programmatically, using
virtually every tool at our disposal.

<a id="d24e6871"></a>
The problem with most binary formats is that the context necessary
to understand the data is separate from the data itself. You are
artificially divorcing the data from its meaning. The data may as
well be encrypted; it is absolutely meaningless without the
application logic to parse it. With plain text, however, you can
achieve a self-describing data stream that is independent of
the application that created it.

### What Is Plain Text?

<a id="d24e6885"></a>
Plain text is made up of printable characters in a form that conveys information. It can be as simple as a shopping list:

```
* milk
* lettuce
* coffee
```

<a id="d24e6897"></a>
or as complex as the source of this book (yes, it's in plain text, much to the chagrin of the publisher, who wanted us to use a word processor).

<a id="d24e6899"></a>
The information part is important. The following is not useful plain text:

```
hlj;uijn bfjxrrctvh jkni'pio6p7gu;vh bjxrdi5rgvhj
```

<a id="d24e6905"></a>
Neither is this:

```
Field19=467abe
```

<a id="d24e6912"></a>
The reader has no idea what the significance of 467abe
may be. We like our plain text to be understandable
to humans.

**Tip 25: Keep Knowledge in Plain Text**

### The Power of Text

<a id="d24e6933"></a>
Plain text doesn't mean that the text is unstructured; HTML, JSON, YAML,
and so on are all plain text. So are the majority of the fundamental
protocols on the net, such as HTTP, SMTP, IMAP, and so on. And that's for some good reasons:

- Insurance against obsolescence
- Leverage existing tools
- Easier testing

#### Insurance Against Obsolescence

<a id="d24e6976"></a>
Human-readable forms of data, and self-describing data, will outlive all
other forms of data and the applications that created them. Period. As
long as the data survives, you will have a chance to be able to use
it—potentially long after the original application that wrote it is
defunct.

<a id="d24e6982"></a>
You can parse such a file with only partial knowledge of its format;
with most binary files, you must know all the details of the entire
format in order to parse it successfully.

<a id="d24e6988"></a>
<a id="FNPTR-24"></a>
Consider a data file from some legacy system that you are
given.[[24]](<22 Engineering Daybooks - daybook.md#FOOTNOTE-24>) You know little about the original application; all
that's important to you is that it maintained a list of clients' Social
Security numbers, which you need to find and extract. Among the data,
you see

```
123-45-6789
...
567-89-0123
...
901-23-4567
```

<a id="d24e7006"></a>
Recognizing the format of a Social Security number, you
can quickly write a small program to extract that data—even if
you have no information on anything else in the file.

<a id="d24e7008"></a>
But imagine if the file had been formatted this way instead:

```
AC27123456789B11P
...
XY43567890123QTYL
...
6T2190123456788AM
```

<a id="d24e7022"></a>
You may not have recognized the significance of the numbers quite as easily. This is the difference between human readable and
human understandable.

<a id="d24e7033"></a>
While we're at it, FIELD10 doesn't help much either. Something
like

```
123-45-6789
```

<a id="d24e7042"></a>
makes the exercise a no-brainer—and ensures that the data will outlive
any project that created it.

#### Leverage

<a id="d24e7047"></a>
Virtually every tool in the computing universe, from version control
systems to editors to command-line tools, can operate on plain text.

<a id="d24e7056"></a>
<a id="d24e7068"></a>
<a id="d24e7070"></a>
The Unix Philosophy

Unix is famous for being designed around the philosophy of small,
sharp tools, each intended to do one thing well. This philosophy is
enabled by using a common underlying format—the line-oriented,
plain-text file. Databases used for system administration (users
and passwords, networking configuration, and so on) are all kept as
plain-text files. (Some systems also maintain a
binary form of certain databases as a performance optimization. The
plain-text version is kept as an interface to the binary version.)

When a system crashes, you may be faced with only a minimal
environment to restore it (you may not be able to access graphics
drivers, for instance). Situations such as this can really make you
appreciate the simplicity of plain text.

Plain text is also easier to search. If you can't remember which configuration file manages your system backups, a quick grep -r backup /etc should tell you.

<a id="d24e7075"></a>
For instance, suppose you have a production deployment of a large
application with a complex site-specific configuration file. If this file is in plain text, you could place it under
a version control system (see Topic 19, [*Version Control*](<19 Version Control - version_control.md#version_control>)),
so that you automatically keep a history of all changes. File comparison
tools such as diff and fc allow you to see at a glance what changes
have been made, while sum allows you to generate a checksum to monitor
the file for accidental (or malicious) modification.

#### Easier Testing

<a id="d24e7100"></a>
If you use plain text to create synthetic data to drive system tests,
then it is a simple matter to add, update, or modify the test data
without having to create any special tools to do so. Similarly, plain-text output from regression tests can be trivially analyzed with
shell commands or a simple script.

### Lowest Common Denominator

<a id="d24e7112"></a>
Even in the future of blockchain-based intelligent agents that travel
the wild and dangerous internet autonomously, negotiating data
interchange among themselves, the ubiquitous text file will still be
there. In fact, in heterogeneous environments the advantages of plain
text can outweigh all of the drawbacks. You need to ensure that all
parties can communicate using a common standard. Plain text is that
standard.

### Related Sections Include

- Topic 17, [*Shell Games*](<17 Shell Games - know_your_shell.md#know_your_shell>)
- Topic 21, [*Text Manipulation*](<21 Text Manipulation - text_manip.md#text_manip>)
- Topic 32, [*Configuration*](<../05 Bend or Break/32 Configuration - configuration.md#configuration>)

### Challenges

<a id="d24e7132"></a>
<a id="d24e7145"></a>
<a id="d24e7148"></a>
<a id="d24e7153"></a>
- Design a small address book database (name, phone number, and
  so on) using a straightforward binary representation in your
  language of choice. Do this before reading the rest of this
  challenge.

  - Translate that format into a plain-text format using XML or JSON.
  - For each version, add a new, variable-length field called
    directions in which you might enter directions to each person's
    house.

  What issues come up regarding versioning and extensibility? Which form
  was easier to modify? What about converting existing data?
