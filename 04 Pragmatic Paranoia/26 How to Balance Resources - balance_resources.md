<a id="balance_resources"></a>
## Topic 26. How to Balance Resources

> To light a candle is to cast a shadow...
>
> Ursula K. Le Guin, A Wizard of Earthsea

<a id="d24e10621"></a>
We all manage resources whenever we code: memory, transactions, threads,
network connections, files, timers—all kinds of things with limited
availability. Most of the time, resource usage follows a predictable
pattern: you allocate the resource, use it, and then deallocate it.

<a id="d24e10635"></a>
However, many developers have no consistent plan for dealing with
resource allocation and deallocation. So let us suggest a simple tip:

**Tip 40: Finish What You Start**

<a id="d24e10645"></a>
This tip is easy to apply in most circumstances. It simply means that
the function or object that allocates a resource should be responsible
for deallocating it. Let's see how it applies by looking at an example
of some bad code—part of a Ruby program that opens a file, reads
customer information from it, updates a field, and writes the result
back. We've eliminated error handling to make the example clearer:

```
def read_customer
  @customer_file = File.open(@name + ".rec", "r+")
  @balance       = BigDecimal(@customer_file.gets)
end

def write_customer
  @customer_file.rewind
  @customer_file.puts @balance.to_s
  @customer_file.close
end

def update_customer(transaction_amount)
  read_customer
  @balance = @balance.add(transaction_amount,2)
  write_customer
end
```

<a id="d24e10721"></a>
<a id="FNPTR-33"></a>
At first sight, the routine update\_customer looks reasonable. It
seems to implement the logic we require—reading a record, updating
the balance, and writing the record back out. However, this tidiness
hides a major problem. The routines read\_customer and
write\_customer are tightly
coupled[[33]](<27 Don't Outrun Your Headlights - headlights.md#FOOTNOTE-33>)—they share
the instance variable
customer\_file. read\_customer opens the file
and stores the file reference in customer\_file, and then write\_customer uses
that stored reference to close the file when it finishes. This shared
variable doesn't even appear in the update\_customer routine.

<a id="d24e10763"></a>
Why is this bad? Let's consider the unfortunate maintenance programmer
who is told that the specification has changed—the balance should
be updated only if the new value is not negative. They go into
the source and change update\_customer:

```
def update_customer(transaction_amount)
  read_customer
  if (transaction_amount >= 0.00)
    @balance = @balance.add(transaction_amount,2)
    write_customer
  end
end
```

<a id="d24e10799"></a>
All seems fine during testing. However, when the code goes into
production, it collapses after several hours, complaining of too many
open files. It turns out that write\_customer is not getting called in
some circumstances. When that happens, the file is not getting closed.

<a id="d24e10807"></a>
A very bad solution to this problem would be to deal with the special
case in update\_customer:.

```
def update_customer(transaction_amount)
  read_customer
  if (transaction_amount >= 0.00)
    @balance += BigDecimal(transaction_amount, 2)
    write_customer
  else
    @customer_file.close # Bad idea!
  end
end
```

<a id="d24e10853"></a>
This will fix the problem—the file will now get closed regardless of
the new balance—but the fix now means that three routines are
coupled through the shared variable customer\_file, and keeping track of when the file is open or not is going to start to get messy. We're falling into a trap, and
things are going to start going downhill rapidly if we continue on
this course. This is not balanced!

<a id="d24e10861"></a>
The finish what you start tip tells us that, ideally, the
routine that allocates a resource should also free it. We can apply it
here by refactoring the code slightly:

```
def read_customer(file)
  @balance=BigDecimal(file.gets)
end

def write_customer(file)
  file.rewind
  file.puts @balance.to_s
end

def update_customer(transaction_amount)
  file=File.open(@name + ".rec", "r+")          # >--
  read_customer(file)                           #    |
  @balance = @balance.add(transaction_amount,2) #    |
  file.close                                    #
```

<a id="d24e10948"></a>
<a id="FNPTR-34"></a>
Instead of holding on to the file reference, we've changed the code to pass it as a parameter.[[34]](<27 Don't Outrun Your Headlights - headlights.md#FOOTNOTE-34>) Now all the responsibility for the file is in the
update\_customer routine. It opens the file and (finishing what
it starts) closes it before returning. The routine balances the use of
the file: the open and close are in the same place, and it is
apparent that for every open there will be a corresponding close. The
refactoring also removes an ugly shared variable.

<a id="d24e10964"></a>
There's another small but important improvement we can make. In many modern languages, you can scope the lifetime of a resource to an enclosed block of some sort. In Ruby, there's a variation of the file open that passes in the open file reference to a block, shown here between the do and the end:

```
def update_customer(transaction_amount)
  File.open(@name + ".rec", "r+") do |file|       # >--
    read_customer(file)                           #    |
    @balance = @balance.add(transaction_amount,2) #    |
    write_customer(file)                          #    |
  end                                             #
```

<a id="d24e11029"></a>
In this case, at the end of the block the file variable goes out of
scope and the external file is closed. Period. No need to remember to
close the file and release the source, it is guaranteed to happen for
you.

<a id="d24e11034"></a>
When in doubt, it always pays to reduce scope.

**Tip 41: Act Locally**

<a id="d24e11045"></a>
<a id="d24e11057"></a>
<a id="d24e11059"></a>
Balancing Over Time

In this topic we're mostly looking at ephemeral resources used by your running process. But you might want to consider what other messes you might be leaving behind.

For instance, how are your logging files handled? You are creating data and using up storage space. Is there something in place to rotate the logs and clean them up? How about for your unofficial debug files you're dropping? If you're adding logging records in a database, is there a similar process in place to expire them? For anything that you create that takes up a finite resource, consider how to balance it.

What else are you leaving behind?

### Nest Allocations

<a id="d24e11064"></a>
The basic pattern for resource allocation can be extended for
routines that need more than one resource at a time. There are just
two more suggestions:

<a id="d24e11079"></a>
<a id="d24e11082"></a>
- Deallocate resources in the opposite order to that in which you allocate them. That way you won't orphan resources if one resource contains references to another.
- When allocating the same set of resources in different places in your code, always allocate them in the same order. This will reduce the possibility of deadlock. (If process A claims resource1 and is about to claim resource2, while process B has claimed resource2 and is trying to get resource1, the two processes will wait forever.)

<a id="d24e11098"></a>
It doesn't matter what kind of resources we're using—transactions, network connections,
memory, files, threads, windows—the basic pattern
applies: whoever allocates a resource should be responsible for
deallocating it. However, in some languages we can develop the concept
further.

### Objects and Exceptions

<a id="d24e11105"></a>
The equilibrium between allocations and deallocations is reminiscent
of an object-oriented class's constructor
and destructor. The class
represents a
resource, the constructor gives you a particular object of that
resource type, and the destructor removes it from your scope.

<a id="d24e11126"></a>
If you are programming in an object-oriented language, you may find it
useful to encapsulate resources in classes.
Each time you need a
particular resource type, you instantiate an object of that class.
When the object goes out of scope, or is reclaimed by the garbage
collector, the object's destructor then deallocates the wrapped resource.

<a id="d24e11128"></a>
This approach has particular benefits when you're working with
languages where exceptions can interfere with
resource deallocation.

### Balancing and Exceptions

<a id="d24e11137"></a>
Languages that support exceptions can make resource deallocation
tricky. If an exception is thrown, how do you guarantee that
everything allocated prior to the exception is tidied up? The answer
depends to some extent on the language support. You generally have two choices:

1. Use variable scope (for example, stack variables in C++ or Rust)
2. Use a finally clause in a try…catch block

<a id="d24e11171"></a>
With usual scoping rules in languages such as C++ or Rust, the variable's memory will be reclaimed when the variable goes out of scope via a return, block exit, or exception. But you can also hook in to the variable's destructor to cleanup any external resources. In this example, the Rust variable named accounts will automatically close the associated file when it goes out of scope:

```
{
  let mut accounts = File::open("mydata.txt")?; // >--
  // use 'accounts'                             //    |
  ...                                           //    |
}                                               //
```

<a id="d24e11219"></a>
The other option, if the language supports it, is the finally clause.
A finally clause will ensure that the specified code will run whether or not an exception was raised in the try…catch block:

```
try
  // some dodgy stuff
catch
  // exception was raised
finally
  // clean up in either case
```

<a id="d24e11256"></a>
However, there is a catch.

#### An Exception Antipattern

<a id="d24e11262"></a>
We commonly see folks writing something like this:

```
begin
   thing = allocate_resource()
   process(thing)
finally
   deallocate(thing)
end
```

<a id="d24e11292"></a>
Can you see what's wrong?

<a id="d24e11294"></a>
What happens if the resource allocation fails and raises an exception?
The finally clause will catch it, and try to deallocate a thing
that was never allocated.

<a id="d24e11302"></a>
The correct pattern for handling resource deallocation in an environment
with exceptions is

```
thing = allocate_resource()
begin
   process(thing)
finally
   deallocate(thing)
end
```

### When You Can't Balance Resources

<a id="d24e11323"></a>
There are times when the basic resource allocation pattern just isn't
appropriate. Commonly this is found in programs that use dynamic data
structures.
One routine will allocate an area of memory and link it
into some larger structure, where it may stay for some time.

<a id="d24e11332"></a>
The trick here is to establish a semantic invariant
for memory
allocation.
You need to decide who is responsible for data in an
aggregate data structure. What happens when you deallocate the
top-level structure? You have three main options:

<a id="d24e11345"></a>
<a id="d24e11348"></a>
<a id="d24e11351"></a>
- The top-level structure is also responsible for freeing any
  substructures that it contains. These structures then recursively
  delete data they contain, and so on.
- The top-level structure is simply deallocated. Any structures
  that it pointed to (that are not referenced elsewhere) are orphaned.
- The top-level structure refuses to deallocate itself if it
  contains any substructures.

<a id="d24e11353"></a>
The choice here depends on the circumstances of each individual data
structure. However, you need to make it explicit for each, and
implement your decision consistently. Implementing any of these
options in a procedural language such as C can be a problem: data
structures themselves are not active. Our preference in these
circumstances is to write a module
for each major structure that
provides standard allocation and deallocation facilities for that
structure. (This module can also provide facilities such as debug
printing, serialization, deserialization, and traversal hooks.)

### Checking the Balance

<a id="d24e11373"></a>
Because Pragmatic Programmers trust no one, including ourselves, we feel that it is
always a good idea to build code that actually checks that resources
are indeed freed appropriately. For most applications, this normally
means producing wrappers
for each type of resource, and using these
wrappers to keep track of all allocations and deallocations. At
certain points in your code, the program logic will dictate that the
resources will be in a certain state: use the wrappers to check this.
For example, a long-running program that services requests will
probably have a single point at the top of its main processing loop
where it waits for the next request to arrive. This is a good place to
ensure that resource usage has not increased since the last execution
of the loop.

<a id="d24e11389"></a>
At a lower, but no less useful level, you can invest in tools that
(among other things) check your running programs for memory leaks.

### Related Sections Include

- Topic 24, [*Dead Programs Tell No Lies*](<24 Dead Programs Tell No Lies - crash_early.md#crash_early>)
- Topic 30, [*Transforming Programming*](<../05 Bend or Break/30 Transforming Programming - function_pipelines.md#function_pipelines>)
- Topic 33, [*Breaking Temporal Coupling*](<../06 Concurrency/33 Breaking Temporal Coupling - temporal_coupling.md#temporal_coupling>)

### Challenges

- Although there are no guaranteed ways of ensuring that you always
  free resources, certain design techniques, when applied
  consistently, will help. In the text we discussed how establishing a
  semantic invariant for major data structures could direct memory
  deallocation decisions. Consider how Topic 23, [*Design by Contract*](<23 Design by Contract - dbc.md#dbc>), could help refine
  this idea.

<a id="exercise-17"></a>
**Exercise 17** ([possible answer](<../A2 Exercise Answers/README.md#answer-17>))

<a id="d24e11458"></a>
Some C and C++ developers make a point of setting a
pointer to NULL after they deallocate the memory it
references. Why is this a good idea?

<a id="exercise-18"></a>
**Exercise 18** ([possible answer](<../A2 Exercise Answers/README.md#answer-18>))

<a id="d24e11499"></a>
Some Java developers make a point of setting an object variable to
NULL after they have finished using the object. Why is this a
good idea?
