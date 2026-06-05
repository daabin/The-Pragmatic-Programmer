<a id="function_pipelines"></a>
## 主题 30. 变换式编程

> 如果你不能将你正在做的事情描述为一个过程，那么你就不知道自己在做什么。
>
> W. 爱德华兹·戴明 (attr)

<a id="d24e13819"></a>
所有程序都会转换数据，将输入转换为输出。然而，当我们考虑设计时，我们很少考虑创造转变。相反，我们担心类和模块、数据结构和算法、语言和框架。

<a id="d24e13838"></a>
我们认为这种对代码的关注常常忽略了要点：我们需要重新考虑将程序视为将输入转换为输出的东西。当我们这样做时，我们之前担心的许多细节就会消失。结构变得更加清晰，错误处理更加一致，耦合性也大大降低。

<a id="d24e13840"></a>
为了开始我们的调查，让我们把时间机器带回到 20 世纪 70 年代，让 Unix 程序员为我们编写一个程序，列出目录树中的五个最长的文件，其中最长的意思是“具有最多的行数”。

<a id="d24e13846"></a>
您可能希望他们找到编辑器并开始用 C 语言输入。但他们不会，因为他们正在根据我们拥有的（目录树）和我们想要的（文件列表）来考虑这个问题。然后他们会进入终端并输入如下内容：

```
$ find . -type f | xargs wc -l | sort -n | tail -5
```

<a id="d24e13909"></a>
这是一系列的转变：

<a id="d24e13916"></a>
<a id="d24e13928"></a>
<a id="d24e13943"></a>
<a id="d24e13952"></a>
寻找 。 -type f ：将当前目录 (.) 中或以下的所有文件 (-type f) 的列表写入标准输出。

xargs wc -l ：从标准输入读取行并安排它们全部作为参数传递给命令 wc -l。带有 -l 选项的 wc 程序计算每个参数中的行数，并将每个结果作为“count filename”写入标准输出。

sort -n ：对标准输入进行排序，假设每行以数字 (-n) 开头，并将结果写入标准输出。

tail -5 ：读取标准输入并将最后五行写入标准输出。

<a id="d24e13954"></a>
在我们书的目录中运行它，我们得到

```
 470 ./test_to_build.pml
 487 ./dbc.pml
 719 ./domain_languages.pml
 727 ./dry.pml
9561 total
```

<a id="d24e13969"></a>
最后一行是所有文件中的总行数（不仅仅是显示的文件），因为这就是 wc 的作用。我们可以通过从 tail 请求多一行，然后忽略最后一行来去掉它：

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

图 1. 作为一系列转换的查找管道

管道图描述了一系列转换。方法是从上到下。首先，找到应从中获取文件名的目录的名称。 wc 程序用于对行和名称列表进行排序。尾部仅由最后五行组成。最后五加总数等于头部。从头部开始，取最后五行。

<a id="d24e14068"></a>
让我们从各个步骤之间流动的数据来看这一点。我们最初的要求“行数前 5 个文件”变成了一系列转换（也显示在 [图](#fig.find) 中）。

<a id="d24e14073"></a>
目录名称 → 文件列表 → 行号列表 → 排序列表 → 最高 5 个 + 总数 → 最高 5 个

<a id="d24e14085"></a>
它几乎就像一条工业装配线：在一端输入原始数据，在另一端输出成品（信息）。

<a id="d24e14087"></a>
我们喜欢以这种方式思考所有代码。

**技巧 49：编程是关于代码的，但程序是关于数据的**

### 寻找转变

<a id="d24e14103"></a>
有时，找到转换的最简单方法是从需求开始并确定其输入和输出。现在您已经定义了代表整个程序的函数。然后您可以找到引导您从输入到输出的步骤。这是一种自上而下的方法。

<a id="d24e14112"></a>
例如，您想为玩文字游戏的人们创建一个网站，该网站可以找到可以由一组字母组成的所有单词。这里的输入是一组字母，输出是三个字母的单词、四个字母的单词等的列表：

|  |  |  |
| --- | --- | --- |
| “绿茵” | 变换为 → | 3 => ivy、lin、nil、yin 4 => inly、liny、viny 5 => 乙烯基 |

<a id="d24e14131"></a>
（是的，它们都是单词，至少根据 macOS 字典是这样。）

<a id="d24e14133"></a>
整个应用程序背后的技巧很简单：我们有一个字典，它通过签名对单词进行分组，选择签名以使包含相同字母的所有单词都具有相同的签名。最简单的签名功能就是单词中字母的排序列表。然后，我们可以通过为其生成签名来查找输入字符串，然后查看字典中的哪些单词（如果有）具有相同的签名。

<a id="d24e14140"></a>
因此，字谜查找器分为四个单独的转换：

| 步 | 转型 | 样本数据 |
| --- | --- | --- |
| 步骤0： | 初始输入 | “伊尔文” |
| 步骤一： | 三个或更多字母的所有组合 | vin, viy, vil, vny, vnl, vyl, iny, inl, iyl, nyl, viny, vinl, viyl, vnyl, inyl, 乙烯基 |
| 步骤2： | 组合的签名 | inv、常春藤、ilv、nvy、lnv、lvy、iny、iln、ily、lny、invy、ilnv、ilvy、lnvy、ilny、ilny |
| 步骤3： | 与任何签名匹配的所有字典单词的列表 | 常春藤、yin、nil、lin、viny、liny、inly、乙烯基 |
| 第4步： | 按长度分组的单词 | 3 => ivy、lin、nil、yin 4 => inly、liny、viny 5 => 乙烯基 |

#### 一路向下的转变

<a id="d24e14199"></a>
让我们从步骤 1 开始，该步骤采用一个单词并创建三个或更多字母的所有组合的列表。此步骤本身可以表示为转换列表：

| 步 | 转型 | 样本数据 |
| --- | --- | --- |
| 步骤1.0： | 初始输入 | “乙烯基塑料” |
| 步骤1.1： | 转换为字符 | 乙烯基塑料 |
| 步骤1.2： | 获取所有子集 | []、[v]、[i]、... [v,i]、[v,n]、[v,y]、... [v,i,n]、[v,i,y]、... [v,n,y,l]、[i,n,y,l]、[v,i,n,y,l] |
| 步骤1.3： | 仅那些长度超过三个字符的 | [v,i,n], [v,i,y], … [i,n,y,l], [v,i,n,y,l] |
| 步骤1.4： | 转换回字符串 | [vin,viy, … inyl,vinyl] |

<a id="d24e14247"></a>
现在我们已经可以轻松地在代码中实现每个转换（在本例中使用 Elixir）：

[函数管道/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

```
defp all_subsets_longer_than_three_characters(word) do
  word
  |> String.codepoints()
  |> Comb.subsets()
  |> Stream.filter(fn subset -> length(subset) >= 3 end)
  |> Stream.map((1))
end
```

#### |> 运算符是怎么回事？

<a id="d24e14301"></a>
<a id="FNPTR-41"></a>
Elixir 与许多其他函数式语言一样，都有一个管道运算符，有时称为前向管道或只是管道。[[41]](<32 Configuration - configuration.md#FOOTNOTE-41>) 它所做的就是获取左侧的值并将其插入右侧函数的第一个参数，因此

```
"vinyl" |> String.codepoints |> Comb.subsets()
```

<a id="d24e14374"></a>
和写作一样

```
Comb.subsets(String.codepoints("vinyl"))
```

<a id="d24e14385"></a>
（其他语言可能会将此管道值作为下一个函数的最后一个参数注入 - 这很大程度上取决于内置库的风格。）

<a id="d24e14390"></a>
您可能认为这只是语法糖。但实际上，管道运营商是一个以不同方式思考的革命性机会。使用管道意味着您会自动考虑转换数据；每次您看到|>时，您实际上看到的是数据在一个转换和下一个转换之间流动的地方。

<a id="d24e14395"></a>
许多语言都有类似的东西：Elm 和 F# 有 |>，Clojure 有 -> 和 ->>（工作方式略有不同），R 有 %>%。 Haskell 都有管道运算符，并且可以轻松声明新的管道运算符。当我们写这篇文章时，有人讨论将 |> 添加到 JavaScript 中。

<a id="d24e14485"></a>
如果您当前的语言支持类似的功能，那么您很幸运。如果没有，请参阅[*语言 X 没有管道*](#sb-no-pipelines)。

<a id="d24e14490"></a>
无论如何，回到代码。

#### 继续转型……

<a id="d24e14495"></a>
现在看主程序的第 2 步，我们将子集转换为签名。同样，这是一个简单的转换——子集列表变成签名列表：

| 步 | 转型 | 样本数据 |
| --- | --- | --- |
| 步骤2.0： | 初始输入 | vin, viy, … inyl, 乙烯基 |
| 步骤2.1： | 转换为签名 | inv、ivy … ilny、inlvy |

<a id="d24e14525"></a>
下面清单中的 Elixir 代码也同样简单：

[函数管道/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

```
defp as_unique_signatures(subsets) do
  subsets
  |> Stream.map(/1)
end
```

<a id="d24e14543"></a>
现在我们转换该签名列表：每个签名都映射到具有相同签名的已知单词列表，如果没有这样的单词则为零。然后我们必须删除 nils 并将嵌套列表展平为单个级别：

[函数管道/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

```
defp find_in_dictionary(signatures) do
  signatures
  |> Stream.map(/1)
  |> Stream.reject(/1)
  |> Stream.concat((1))
end
```

<a id="d24e14573"></a>
步骤 4，按长度对单词进行分组，是另一个简单的转换，将我们的列表转换为一个映射，其中键是长度，值是具有该长度的所有单词：

[函数管道/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

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
X 语言没有管道

管道已经存在很长时间了，但仅限于小众语言。它们最近才进入主流，许多流行语言仍然不支持这个概念。

好消息是，转换思维不需要特定的语言语法：它更像是一种设计哲学。您仍然将代码构建为转换，但将它们编写为一系列赋值：

```
const content = File.read(file_name);
const lines   = find_matching_lines(content, pattern)
const result  = truncate_lines(lines)
```

这有点乏味，但它可以完成工作。

#### 把它们放在一起

<a id="d24e14643"></a>
我们已经编写了每个单独的转换。现在是时候将它们全部串到我们的 main 函数中了：

[函数管道/anagrams/lib/anagrams.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/anagrams.ex)

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
有效吗？我们来尝试一下：

```
iex(1)> Anagrams.anagrams_in "lyvin"
%{
  3 => ["ivy", "lin", "nil", "yin"],
  4 => ["inly", "liny", "viny"],
  5 => ["vinyl"]
}
```

<a id="pg-donthoard"></a>
### 为什么这这么棒？

<a id="d24e14692"></a>
我们再看一下main函数的主体：

```
word
|> all_subsets_longer_than_three_characters()
|> as_unique_signatures()
|> find_in_dictionary()
|> group_by_length()
```

<a id="d24e14706"></a>
它只是满足我们的要求所需的一系列转换，每个转换从前一个转换获取输入并将输出传递到下一个转换。这与您所能得到的最接近的有文字的代码是一样的。

<a id="d24e14708"></a>
但还有更深层次的东西。如果您的背景是面向对象编程，那么您的反应要求您隐藏数据，将其封装在对象内。然后这些对象来回聊天，改变彼此的状态。这引入了很多耦合，这是面向对象系统难以更改的一个重要原因。

**提示 50：不要囤积状态；传递它**

<a id="d24e14729"></a>
在转型模型中，我们颠覆了这一点。不要将数据视为遍布整个系统的小数据池，而应将数据视为一条浩瀚的河流。数据成为功能的对等体：管道是代码→数据→代码→数据......的序列。数据不再像在类定义中那样与特定的函数组相关联。相反，当应用程序将输入转换为输出时，它可以自由地表示我们应用程序的展开进度。这意味着我们可以大大减少耦合：函数可以在其参数与其他函数的输出匹配的任何地方使用（和重用）。

<a id="d24e14734"></a>
是的，仍然存在一定程度的耦合，但根据我们的经验，它比 OO 风格的命令和控制更易于管理。而且，如果您使用带有类型检查的语言，当您尝试连接两个不兼容的事物时，您将收到编译时警告。

### 错误处理怎么样？

<a id="d24e14746"></a>
到目前为止，我们的转变在一个没有任何问题的世界中发挥了作用。那么我们如何在现实世界中使用它们呢？如果我们只能构建线性链，我们如何添加错误检查所需的所有条件逻辑？

<a id="d24e14752"></a>
有很多方法可以做到这一点，但它们都依赖于一个基本约定：我们从不在转换之间传递原始值。相反，我们将它们包装在数据结构（或类型）中，该数据结构还告诉我们所包含的值是否有效。例如，在 Haskell 中，这个包装器称为 Maybe。在 F# 和 Scala 中它是选项。

<a id="d24e14769"></a>
如何使用这个概念是特定于语言的。不过，一般来说，有两种编写代码的基本方法：您可以检查转换内部或外部的错误。

<a id="d24e14771"></a>
到目前为止我们使用的 Elixir 没有内置这种支持。就我们的目的而言，这是一件好事，因为我们可以从头开始展示一个实现。类似的东西应该适用于大多数其他语言。

#### 首先，选择一个代表

<a id="d24e14780"></a>
我们需要包装器的表示（携带值或错误指示的数据结构）。您可以为此使用结构，但 Elixir 已经有一个相当强大的约定：函数倾向于返回包含 {:ok, value} 或 {:error, Reason} 的元组。例如，File.open 返回 :ok 和 IO 进程或 :error 和原因代码：

```
iex(1)> File.open("/etc/passwd")
{:ok, #PID
```

<a id="d24e14823"></a>
当通过管道传递内容时，我们将使用 :ok/:error 元组作为包装器。

#### 然后在每个转换内部处理它

<a id="d24e14834"></a>
让我们编写一个函数，返回文件中包含给定字符串（截断为前 20 个字符）的所有行。我们希望将其编写为转换，因此输入将是一个文件名和一个要匹配的字符串，输出将是带有行列表的 :ok 元组或带有某种原因的 :error 元组。顶级函数应该如下所示：

[函数管道/anagrams/lib/grep.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/grep.ex)

```
def find_all(file_name, pattern) do
  File.read(file_name)
  |> find_matching_lines(pattern)
  |> truncate_lines()
end
```

<a id="d24e14859"></a>
<a id="FNPTR-42"></a>
这里没有显式的错误检查，但如果管道中的任何步骤返回错误元组，那么管道将返回该错误，而不执行后面的函数。[[42]](<32 Configuration - configuration.md#FOOTNOTE-42>) 我们使用 Elixir 的模式匹配来执行此操作：

[函数管道/anagrams/lib/grep.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/grep.ex)

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
看一下函数 find\_matching\_lines。如果其第一个参数是 :ok 元组，则它使用该元组中的内容来查找与模式匹配的行。但是，如果第一个参数不是 :ok 元组，则运行该函数的第二个版本，它仅返回该参数。这样，该函数只需将错误沿着管道转发即可。同样的事情也适用于 truncate\_lines。

<a id="d24e15013"></a>
我们可以在控制台上玩这个：

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
您可以看到管道中任何位置的错误都会立即成为管道的值。

#### 或者在管道中处理它

<a id="d24e15071"></a>
您可能正在查看 find\_matching\_lines 和 truncate\_lines 函数，认为我们已将错误处理的负担转移到转换中。你是对的。在函数调用中使用模式匹配的语言中，例如 Elixir，效果会减弱，但仍然很难看。

<a id="d24e15079"></a>
<a id="FNPTR-43"></a>
如果 Elixir 有一个管道运算符 |> 的版本，它知道 :ok/:error 元组，并在发生错误时短路执行，那就太好了。[[43]](<32 Configuration - configuration.md#FOOTNOTE-43>) 但事实上，它不允许我们以适用于许多其他语言的方式添加类似的内容。

<a id="d24e15118"></a>
我们面临的问题是，当发生错误时，我们不想在管道中进一步运行代码，并且我们不希望该代码知道这种情况正在发生。这意味着我们需要推迟运行管道函数，直到我们知道管道中的先前步骤成功为止。为此，我们需要将它们从函数调用更改为可以稍后调用的函数值。这是一种实现：

[函数管道/字谜/lib/grep1.ex](http://media.pragprog.com/titles/tpp20/code/function-pipelines/anagrams/lib/grep1.ex)

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
and\_then 函数是绑定函数的一个示例：它接受一个包装在某些内容中的值，然后将函数应用于该值，返回一个新的包装值。在管道中使用 and\_then 函数需要一些额外的标点符号，因为 Elixir 需要被告知将函数调用转换为函数值，但转换函数变得简单这一事实抵消了额外的努力：每个函数只接受一个值（以及任何额外的参数）并返回 {:ok, new\_value} 或 {:error, Reason}。

### 转换 转换编程

<a id="d24e15341"></a>
将代码视为一系列（嵌套）转换可以是一种解放编程的方法。这需要一段时间才能习惯，但一旦养成了习惯，你会发现你的代码变得更干净，你的函数更短，你的设计更扁平。

<a id="d24e15343"></a>
尝试一下。

### 相关部分包括

- 主题 8，[*优秀设计的本质*](<../02 Pragmatic Approach/08 The Essence of Good Design - essence_of_design.md#essence_of_design>)
- 主题 17，[*贝壳游戏*](<../03 Basic Tools/17 Shell Games - know_your_shell.md#know_your_shell>)
- 主题 26，[*如何平衡资源*](<../04 Pragmatic Paranoia/26 How to Balance Resources - balance_resources.md#balance_resources>)
- 主题 28，[*解耦*](<28 Decoupling - coupling.md#coupling>)
- 主题 35，[*Actor 和进程*](<../06 Concurrency/35 Actors and Processes - actor_model.md#actor_model>)

### 练习

<a id="exercise-21"></a>
**练习 21** ([可能的答案](<../A2 Exercise Answers/README.md#answer-21>))

<a id="d24e15375"></a>
您能否将以下需求表达为顶层转换？也就是说，对于每个，识别输入和输出。

1. 运费和销售税已添加到订单中
2. 您的应用程序从命名文件加载配置信息
3. 有人登录到 Web 应用程序

<a id="exercise-22"></a>
**练习 22** ([可能的答案](<../A2 Exercise Answers/README.md#answer-22>))

<a id="d24e15399"></a>
您已经确定需要验证输入字段并将其从字符串转换为 18 到 150 之间的整数。整体转换描述如下

```
field contents as string
    → [validate  convert]
        → {:ok, value} | {:error, reason}
```

<a id="d24e15409"></a>
编写构成验证和转换的各个转换。

<a id="exercise-23"></a>
**练习 23** ([可能的答案](<../A2 Exercise Answers/README.md#answer-23>))

<a id="d24e15422"></a>
在 [*语言 X 没有管道*](#sb-no-pipelines) 中我们写道：

```
const content = File.read(file_name);
const lines   = find_matching_lines(content, pattern)
const result  = truncate_lines(lines)
```

<a id="d24e15441"></a>
许多人通过将方法调用链接在一起来编写 OO 代码，并且可能会想将其编写为如下所示：

```
const result = content_of(file_name)
               .find_matching_lines(pattern)
               .truncate_lines()
```

<a id="d24e15457"></a>
这两段代码有什么区别？你认为我们更喜欢哪一个？
