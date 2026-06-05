<a id="configuration"></a>
## 主题 32. 配置

> 让你所有的东西各归其位；让您业务的每个部分都有自己的时间。
>
> 本杰明·富兰克林，《十三种美德》，自传

<a id="d24e16571"></a>
当代码依赖于应用程序上线后可能更改的值时，请将这些值保留在应用程序外部。当您的应用程序将在不同的环境中运行并且可能针对不同的客户时，请将特定于环境和客户的值保留在应用程序之外。通过这种方式，您可以参数化您的应用程序；代码会适应它运行的地方。

**提示 55：使用外部配置参数化您的应用程序**

<a id="d24e16603"></a>
您可能想要放入配置数据的常见内容包括：

- 外部服务的凭据（数据库、第三方 API 等）
- 日志记录级别和目的地
- 应用程序使用的端口、IP 地址、计算机和集群名称
- 特定于环境的验证参数
- 外部设置参数，例如税率
- 特定于站点的格式详细信息
- 许可证密钥

<a id="d24e16677"></a>
基本上，寻找您知道必须更改的任何可以在代码主体之外表达的内容，并将其放入某个配置桶中。

### 静态配置

<a id="d24e16682"></a>
许多框架和相当多的自定义应用程序将配置保存在平面文件或数据库表中。如果信息位于平面文件中，趋势是使用某种现成的纯文本格式。目前 YAML 和 JSON 对此很流行。有时，用脚本语言编写的应用程序使用专用源代码文件，专门用于仅包含配置。如果信息是结构化的，并且可能会被客户更改（例如销售税率），则最好将其存储在数据库表中。当然，您可以同时使用两者，根据用途拆分配置信息。

<a id="d24e16698"></a>
无论您使用哪种形式，配置都会作为数据结构读入您的应用程序，通常是在应用程序启动时。通常，这种数据结构是全局的，这样可以使代码的任何部分更容易获取它所保存的值。

<a id="d24e16700"></a>
我们希望您不要这样做。相反，将配置信息包装在（薄）API后面。这将您的代码与配置表示的细节分离。

### 配置即服务

<a id="d24e16724"></a>
虽然静态配置很常见，但我们目前倾向于采用不同的方法。我们仍然希望配置数据保留在应用程序外部，但我们希望看到它存储在服务 API 后面，而不是保存在平面文件或数据库中。这样做有很多好处：

- 多个应用程序可以共享配置信息，身份验证和访问控制限制每个应用程序可以看到的内容
- 可以全局进行配置更改
- 配置数据可以通过专门的 UI 维护
- 配置数据变得动态

<a id="d24e16743"></a>
最后一点，即配置应该是动态的，在我们转向高可用应用程序时至关重要。我们必须停止并重新启动应用程序才能更改单个参数的想法与现代现实完全脱节。使用配置服务，应用程序的组件可以注册它们使用的参数更新的通知，并且如果参数发生更改，该服务可以向它们发送包含新值的消息。

<a id="d24e16745"></a>
无论采用何种形式，配置数据都会驱动应用程序的运行时行为。当配置值发生变化时，无需重建代码。

### 不要编写 Dodo 代码

<a id="d24e16750"></a>
如果没有外部配置，您的代码就无法发挥应有的适应性或灵活性。这是一件坏事吗？好吧，在现实世界中，不适应的物种就会死亡。

<a id="d24e16754"></a>
<a id="FNPTR-45"></a>
渡渡鸟无法适应毛里求斯岛上人类及其牲畜的存在，因此很快就灭绝了。[[45]](#FOOTNOTE-45) 这是第一次有记录的因人类原因造成的物种灭绝。

<a id="d24e16763"></a>
不要让您的项目（或您的职业）像渡渡鸟一样失败。

<a id="d24e16776"></a>
![Sketch of a dodo.](https://panzhongxian.cn/images/the-pragmatic-programmer/dodo.png)

### 相关部分包括

- 主题 9，<a href="../02%20Pragmatic%20Approach/09%20DRY%20-%20The%20Evils%20of%20Duplication%20-%20dry#dry">DRY——重复的弊端</a>
- 主题 14，<a href="../02%20Pragmatic%20Approach/14%20Domain%20Languages%20-%20domain_languages#domain_languages">领域语言</a>
- 主题 16，<a href="../03%20Basic%20Tools/16%20The%20Power%20of%20Plain%20Text%20-%20plain_text#plain_text">纯文本的力量</a>
- 主题 28，<a href="28%20Decoupling%20-%20coupling#coupling">解耦</a>

<a id="d24e16797"></a>
<a id="d24e16804"></a>
<a id="d24e16809"></a>
不要过度

在本书的第一版中，我们建议以类似的方式使用配置而不是代码，但显然我们的说明应该更具体一些。任何建议都可能走向极端或使用不当，因此以下是一些注意事项：

不要做得太过分。我们的一位早期客户决定他们应用程序中的每个字段都应该是可配置的。因此，即使是最小的更改也需要花费数周的时间，因为您必须实现该字段和所有管理代码来保存和编辑它。他们手头上有大约 40,000 个配置变量和编码噩梦。

不要因为懒惰而将决策推向配置。如果对于某个功能是否应该以这种方式工作，或者是否应该由用户选择存在真正的争论，请尝试一种方式并获得有关该决定是否良好的反馈。

<a id="d24e12284"></a>
<a id="FOOTNOTE-37"></a>
<a id="d24e12659"></a>
<a id="FOOTNOTE-38"></a>
<a id="d24e13229"></a>
<a id="FOOTNOTE-39"></a>
<a id="d24e13561"></a>
<a id="FOOTNOTE-40"></a>
<a id="d24e14358"></a>
<a id="FOOTNOTE-41"></a>
<a id="d24e14876"></a>
<a id="FOOTNOTE-42"></a>
<a id="d24e15091"></a>
<a id="FOOTNOTE-43"></a>
<a id="d24e15582"></a>
<a id="FOOTNOTE-44"></a>
<a id="d24e16757"></a>
<a id="FOOTNOTE-45"></a>
<a href="28%20Decoupling%20-%20coupling#FNPTR-37">[37]</a>所以这并不是真正的定律。它更像是德墨忒尔的好主意。

<a href="28%20Decoupling%20-%20coupling#FNPTR-38">[38]</a><https://media.pragprog.com/articles/jan_03_enbug.pdf>

<a href="29%20Juggling%20the%20Real%20World%20-%20event#FNPTR-39">[39]</a>是的，我们知道 Ruby 已经通过其 at\_exit 函数具备了这种功能。

<a href="29%20Juggling%20the%20Real%20World%20-%20event#FNPTR-40">[40]</a><https://media.pragprog.com/titles/tpp20/code/event/rxcommon/logger.js>

<a href="30%20Transforming%20Programming%20-%20function_pipelines#FNPTR-41">[41]</a>似乎第一次使用字符 |> 作为管道可以追溯到 1994 年，在关于 Isobelle/ML 语言的讨论中，存档于 <https://blogs.msdn.microsoft.com/dsyme/2011/05/17/archeological-semiotics-the-birth-of-the-pipeline-symbol-1994/>

<a href="30%20Transforming%20Programming%20-%20function_pipelines#FNPTR-42">[42]</a>我们在这里采取了自由。从技术上讲，我们确实执行以下功能。我们只是不执行其中的代码。

<a href="30%20Transforming%20Programming%20-%20function_pipelines#FNPTR-43">[43]</a>事实上，您可以使用 Elixir 的宏功能将这样的运算符添加到 Elixir 中；十六进制的 Monad 库就是一个例子。您也可以将 Elixir 与构造一起使用，但是这样您就失去了通过管道编写转换的大部分感觉。

<a href="31%20Inheritance%20Tax%20-%20inheritance_tax#FNPTR-44">[44]</a><https://www.quora.com/What-does-Alan-Kay-think-about-inheritance-in-object-oriented-programming>

[[45]](#FNPTR-45)定居者用棍棒将平静的（读作：愚蠢的）鸟打死作为运动，这并没有帮助。
