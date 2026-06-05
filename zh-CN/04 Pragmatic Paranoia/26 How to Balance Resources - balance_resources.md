<a id="balance_resources"></a>
## 主题 26. 如何平衡资源

> 点燃蜡烛就是投下阴影……
>
> 乌苏拉·K·勒吉恩，地海巫师

<a id="d24e10621"></a>
每当我们编码时，我们都会管理资源：内存、事务、线程、网络连接、文件、计时器——各种可用性有限的东西。大多数时候，资源使用遵循可预测的模式：分配资源、使用它，然后释放它。

<a id="d24e10635"></a>
然而，许多开发人员没有一致的计划来处理资源分配和释放。因此，让我们提出一个简单的提示：

**提示 40：完成你开始的事情**

<a id="d24e10645"></a>
这个技巧在大多数情况下都很容易应用。它只是意味着分配资源的函数或对象应该负责释放它。让我们通过查看一些错误代码的示例来了解它是如何应用的——Ruby 程序的一部分，打开一个文件，从中读取客户信息，更新一个字段，然后将结果写回。我们消除了错误处理以使示例更清晰：

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
乍一看，例程 update\_customer 看起来很合理。它似乎实现了我们需要的逻辑——读取记录，更新余额，并将记录写回。然而，这种整洁却隐藏着一个大问题。例程 read\_customer 和 write\_customer 紧密耦合[[33]](<27 Don't Outrun Your Headlights - headlights.md#FOOTNOTE-33>) — 它们共享实例变量 customer\_file。 read\_customer 打开文件并将文件引用存储在 customer\_file 中，然后 write\_customer 使用该存储的引用在完成时关闭文件。这个共享变量甚至不会出现在 update\_customer 例程中。

<a id="d24e10763"></a>
为什么这样不好？让我们考虑一下不幸的维护程序员，他被告知规范已更改 - 仅当新值不为负时才应更新余额。他们进入源代码并更改 update\_customer：

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
测试期间一切似乎都很好。然而，当代码投入生产时，几个小时后它就会崩溃，抱怨打开的文件太多。事实证明，在某些情况下 write\_customer 没有被调用。发生这种情况时，文件不会被关闭。

<a id="d24e10807"></a>
对于这个问题的一个非常糟糕的解决方案是处理 update\_customer: 中的特殊情况。

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
这将解决问题——无论新的余额如何，文件现在都将被关闭——但现在的修复意味着三个例程通过共享变量 customer\_file 耦合，并且跟踪文件何时打开或不打开将开始变得混乱。我们正在陷入陷阱，如果我们继续这样下去，事情就会开始迅速走下坡路。这不平衡啊！

<a id="d24e10861"></a>
完成你开始的提示告诉我们，理想情况下，分配资源的例程也应该释放它。我们可以通过稍微重构代码来应用它：

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
我们不再保留文件引用，而是更改了代码以将其作为参数传递。[[34]](<27 Don't Outrun Your Headlights - headlights.md#FOOTNOTE-34>) 现在，文件的所有责任都在 update\_customer 例程中。它打开文件并（完成它开始的操作）在返回之前关闭它。该例程平衡了文件的使用：打开和关闭位于同一位置，显然每次打开都会有相应的关闭。重构还删除了一个丑陋的共享变量。

<a id="d24e10964"></a>
我们还可以做出另一个小但重要的改进。在许多现代语言中，您可以将资源的生命周期范围限制为某种封闭的块。在 Ruby 中，有一个文件打开的变体，它将打开的文件引用传递给一个块，如下所示在 do 和 end 之间：

```
def update_customer(transaction_amount)
  File.open(@name + ".rec", "r+") do |file|       # >--
    read_customer(file)                           #    |
    @balance = @balance.add(transaction_amount,2) #    |
    write_customer(file)                          #    |
  end                                             #
```

<a id="d24e11029"></a>
在这种情况下，在块的末尾，文件变量超出范围并且外部文件被关闭。时期。无需记住关闭文件并释放源代码，这肯定会发生在您身上。

<a id="d24e11034"></a>
当有疑问时，缩小范围总是值得的。

**提示 41：本地行动**

<a id="d24e11045"></a>
<a id="d24e11057"></a>
<a id="d24e11059"></a>
随着时间的推移保持平衡

在本主题中，我们主要关注正在运行的进程使用的临时资源。但您可能需要考虑您可能留下的其他混乱。

例如，您的日志文件是如何处理的？您正在创建数据并耗尽存储空间。是否有什么东西可以旋转日志并清理它们？对于您要删除的非官方调试文件怎么样？如果您要在数据库中添加日志记录，是否有类似的流程来使它们过期？对于您创建的任何占用有限资源的事物，请考虑如何平衡它。

你还留下什么？

### 巢穴分配

<a id="d24e11064"></a>
资源分配的基本模式可以扩展到一次需要多个资源的例程。还有两个建议：

<a id="d24e11079"></a>
<a id="d24e11082"></a>
- 按照与分配资源的顺序相反的顺序释放资源。这样，如果一个资源包含对另一资源的引用，您就不会孤立资源。
- 在代码中的不同位置分配同一组资源时，请始终以相同的顺序分配它们。这将减少死锁的可能性。 （如果进程 A 声明了资源 1 并且即将声明资源 2，而进程 B 已经声明了资源 2 并且正在尝试获取资源 1，则两个进程将永远等待。）

<a id="d24e11098"></a>
无论我们使用哪种资源（事务、网络连接、内存、文件、线程、窗口），基本模式都适用：分配资源的人应该负责释放它。然而，在某些语言中我们可以进一步发展这个概念。

### 对象和异常

<a id="d24e11105"></a>
分配和释放之间的平衡让人想起面向对象类的构造函数和析构函数。该类代表一种资源，构造函数为您提供该资源类型的特定对象，析构函数将其从您的范围中删除。

<a id="d24e11126"></a>
如果您使用面向对象的语言进行编程，您可能会发现将资源封装在类中很有用。每次您需要特定的资源类型时，您就实例化该类的一个对象。当对象超出范围或被垃圾收集器回收时，对象的析构函数将释放包装的资源。

<a id="d24e11128"></a>
当您使用异常可能干扰资源释放的语言时，此方法具有特别的优势。

### 平衡和例外

<a id="d24e11137"></a>
支持异常的语言可能会使资源释放变得棘手。如果抛出异常，如何保证异常之前分配的所有内容都已整理完毕？答案在某种程度上取决于语言支持。通常你有两种选择：

1. 使用变量作用域（例如，C++ 或 Rust 中的堆栈变量）
2. 在 try...catch 块中使用 finally 子句

<a id="d24e11171"></a>
根据 C++ 或 Rust 等语言中常见的作用域规则，当变量通过返回、块退出或异常超出作用域时，变量的内存将被回收。但您也可以连接到变量的析构函数来清理任何外部资源。在此示例中，名为accounts的Rust变量将在超出范围时自动关闭关联的文件：

```
{
  let mut accounts = File::open("mydata.txt")?; // >--
  // use 'accounts'                             //    |
  ...                                           //    |
}                                               //
```

<a id="d24e11219"></a>
如果语言支持，另一个选项是finally 子句。 finally 子句将确保指定的代码将运行，无论 try…catch 块中是否引发异常：

```
try
  // some dodgy stuff
catch
  // exception was raised
finally
  // clean up in either case
```

<a id="d24e11256"></a>
然而，有一个问题。

#### 异常反模式

<a id="d24e11262"></a>
我们经常看到人们写这样的东西：

```
begin
   thing = allocate_resource()
   process(thing)
finally
   deallocate(thing)
end
```

<a id="d24e11292"></a>
你能看出出了什么问题吗？

<a id="d24e11294"></a>
如果资源分配失败并引发异常会发生什么？ finally 子句会捕获它，并尝试释放从未分配过的东西。

<a id="d24e11302"></a>
在有异常的环境中处理资源释放的正确模式是

```
thing = allocate_resource()
begin
   process(thing)
finally
   deallocate(thing)
end
```

### 当你无法平衡资源时

<a id="d24e11323"></a>
有时基本的资源分配模式并不合适。这通常出现在使用动态数据结构的程序中。一个例程将分配一块内存区域并将其链接到某个更大的结构中，它可能会在其中保留一段时间。

<a id="d24e11332"></a>
这里的技巧是建立内存分配的语义不变量。您需要决定谁负责聚合数据结构中的数据。当您解除分配顶层结构时会发生什么？您有三个主要选择：

<a id="d24e11345"></a>
<a id="d24e11348"></a>
<a id="d24e11351"></a>
- 顶级结构还负责释放它包含的任何子结构。然后，这些结构会递归地删除它们包含的数据，依此类推。
- 顶层结构被简单地释放。它指向的任何结构（在其他地方未引用）都是孤立的。
- 如果顶级结构包含任何子结构，则它拒绝释放自身。

<a id="d24e11353"></a>
这里的选择取决于每个单独数据结构的情况。但是，您需要明确每个决定，并一致地执行您的决定。在过程语言（例如 C）中实现这些选项中的任何一个都可能是一个问题：数据结构本身并不活跃。在这些情况下，我们的首选是为每个主要结构编写一个模块，为该结构提供标准的分配和释放设施。 （该模块还可以提供调试打印、序列化、反序列化和遍历挂钩等设施。）

### 检查余额

<a id="d24e11373"></a>
因为务实的程序员不信任任何人，包括我们自己，所以我们认为构建实际检查资源是否确实被适当释放的代码始终是一个好主意。对于大多数应用程序来说，这通常意味着为每种类型的资源生成包装器，并使用这些包装器来跟踪所有分配和释放。在代码中的某些点，程序逻辑将指示资源将处于某种状态：使用包装器来检查这一点。例如，一个为请求提供服务的长时间运行的程序可能会在其主处理循环的顶部有一个点，等待下一个请求到达。这是确保自上次循环执行以来资源使用量没有增加的好地方。

<a id="d24e11389"></a>
在较低但同样有用的级别上，您可以投资一些工具来检查正在运行的程序是否存在内存泄漏。

### 相关部分包括

- 主题 24，[*死程序不会说谎*](<24 Dead Programs Tell No Lies - crash_early.md#crash_early>)
- 主题 30，[*转变编程*](<../05 Bend or Break/30 Transforming Programming - function_pipelines.md#function_pipelines>)
- 主题 33，[*打破时间耦合*](<../06 Concurrency/33 Breaking Temporal Coupling - temporal_coupling.md#temporal_coupling>)

### 挑战

- 尽管没有保证方法可以确保您始终释放资源，但某些设计技术如果一致应用，将会有所帮助。在本文中，我们讨论了为主要数据结构建立语义不变量如何指导内存释放决策。考虑一下主题 23 [*按合同设计*](<23 Design by Contract - dbc.md#dbc>) 如何帮助完善这个想法。

<a id="exercise-17"></a>
**练习 17** ([可能的答案](<../A2 Exercise Answers/README.md#answer-17>))

<a id="d24e11458"></a>
一些 C 和 C++ 开发人员在释放其引用的内存后，会特意将指针设置为 NULL。为什么这是个好主意？

<a id="exercise-18"></a>
**练习 18** ([可能的答案](<../A2 Exercise Answers/README.md#answer-18>))

<a id="d24e11499"></a>
一些 Java 开发人员在使用完对象后，特意将对象变量设置为 NULL。为什么这是个好主意？
