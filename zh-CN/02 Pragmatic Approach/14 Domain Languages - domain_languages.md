<a id="domain_languages"></a>
## 主题 14. 领域语言

> 语言的界限就是一个人的世界的界限。
>
> 路德维希·维特根斯坦

<a id="d24e5610"></a>
计算机语言会影响您思考问题的方式以及交流的方式。每种语言都带有一系列功能：诸如静态类型与动态类型、早期绑定与后期绑定、函数式与面向对象、继承模型、混合、宏等流行语，所有这些都可能暗示或掩盖某些解决方案。使用 C++ 设计解决方案将产生与基于 Haskell 风格思维的解决方案不同的结果，反之亦然。相反，我们认为更重要的是，问题域的语言也可能提出编程解决方案。

<a id="d24e5629"></a>
我们总是尝试使用应用程序域的词汇来编写代码（参见[*维护术语表*](<../08 Before the Project/45 The Requirements Pit - requirements.md#pglossary>)）。在某些情况下，务实的程序员可以进入下一个级别，并使用该领域的词汇、语法和语义（即语言）进行实际编程。

**提示 22：靠近问题域进行编程**

### 一些现实世界的领域语言

<a id="d24e5642"></a>
让我们看一些人们已经这样做的例子。

#### 规格

<a id="d24e5647"></a>
<a id="FNPTR-19"></a>
RSpec[[19]](<15 Estimating - learn_to_estimate.md#FOOTNOTE-19>) 是 Ruby 的测试库。它启发了大多数其他现代语言的版本。 RSpec 中的测试旨在反映您期望代码的行为。

```
describe BowlingScore do
  it "totals 12 if you score 3 four times" do
    score = BowlingScore.new
    4.times { score.add_pins(3) }
    expect(score.total).to eq(12)
  end
end
```

#### 黄瓜

<a id="d24e5701"></a>
<a id="FNPTR-20"></a>
Cucumber[[20]](<15 Estimating - learn_to_estimate.md#FOOTNOTE-20>) 是指定测试的编程语言中立方式。您使用适合您所使用语言的 Cucumber 版本来运行测试。为了支持类似自然语言的语法，您还必须编写特定的匹配器来识别短语并提取测试参数。

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
Cucumber 测试的目的是供软件的客户阅读（尽管这种情况在实践中很少发生；下面会考虑为什么会出现这种情况）。

<a id="sb-cuc"></a>
<a id="d24e5770"></a>
<a id="d24e5790"></a>
<a id="d24e5792"></a>
为什么很多商业用户不阅读 Cucumber 功能？

经典的收集需求、设计、代码、交付方法行不通的原因之一是，它以我们知道需求是什么的概念为基础。但我们很少这样做。您的业​​务用户会对他们想要实现的目标有一个模糊的想法，但他们既不知道也不关心细节。这是我们价值的一部分：我们凭直觉感知意图并将其转换为代码。

因此，当您强迫业务人员签署需求文档，或者让他们同意一组 Cucumber 功能时，您所做的相当于让他们检查用 Sumerian 撰写的文章中的拼写。他们会随机做出一些改变来保全面子，然后签字同意让你离开他们的办公室。

然而，给他们运行的代码，他们就可以使用它。这就是他们真正的需求会浮现出来的地方。

#### 凤凰城航线

<a id="d24e5797"></a>
<a id="FNPTR-21"></a>
许多 Web 框架都有路由工具，将传入的 HTTP 请求映射到代码中的处理函数上。这是来自 Phoenix 的示例。[[21]](<15 Estimating - learn_to_estimate.md#FOOTNOTE-21>)

```
scope "/", HelloPhoenix do
  pipe_through :browser # Use the default browser stack

  get "/", PageController, :index
  resources "/users", UserController
end
```

<a id="d24e5843"></a>
这表示以“/”开头的请求将通过一系列适合浏览器的过滤器运行。对“/”本身的请求将由 PageController 模块中的索引函数处理。 UsersController 实现了管理可通过 url /users 访问的资源所需的功能。

#### 安西布尔

<a id="d24e5860"></a>
<a id="FNPTR-22"></a>
<a id="FNPTR-23"></a>
Ansible[[22]](<15 Estimating - learn_to_estimate.md#FOOTNOTE-22>) 是一种配置软件的工具，通常在一堆远程服务器上。它通过读取您提供的规范，然后执行服务器上所需的任何操作来使它们镜像该规范来实现此目的。该规范可以用 YAML、[[23]](<15 Estimating - learn_to_estimate.md#FOOTNOTE-23>) 编写，这是一种根据文本描述构建数据结构的语言：

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
此示例确保我的服务器上安装了最新版本的 nginx，默认启动它，并且使用您提供的配置文件。

### 领域语言的特点

<a id="d24e5943"></a>
让我们更仔细地看看这些例子。

<a id="d24e5945"></a>
RSpec 和 Phoenix 路由器是用它们的主机语言（Ruby 和 Elixir）编写的。他们使用了一些相当狡猾的代码，包括元编程和宏，但最终它们作为常规代码进行编译和运行。

<a id="d24e5964"></a>
Cucumber 测试和 Ansible 配置是用自己的语言编写的。 Cucumber 测试被转换为要运行的代码或数据结构，而 Ansible 规范始终转换为由 Ansible 本身运行的数据结构。

<a id="d24e5976"></a>
因此，RSpec 和路由器代码嵌入到您运行的代码中：它们是代码词汇表的真正扩展。 Cucumber 和 Ansible 通过代码读取并转换为代码可以使用的某种形式。

<a id="d24e5981"></a>
我们将 RSpec 和路由器示例称为内部域语言，而 Cucumber 和 Ansible 使用外部语言。

### 内部语言和外部语言之间的权衡

<a id="d24e6007"></a>
一般来说，内部域语言可以利用其宿主语言的功能：您创建的域语言更强大，而且这种能力是免费的。例如，您可以使用一些 Ruby 代码自动创建一堆 RSpec 测试。在这种情况下，我们可以测试没有备用或罢工的分数：

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
这是您刚刚编写的 100 个测试。这天剩下的时间请假。

<a id="d24e6102"></a>
内部域语言的缺点是您受到该语言的语法和语义的约束。尽管某些语言在这方面非常灵活，但您仍然被迫在您想要的语言和您可以实现的语言之间做出妥协。

<a id="d24e6104"></a>
最终，无论您想出什么，都必须仍然是目标语言中的有效语法。带有宏的语言（例如 Elixir、Clojure 和 Crystal）为您提供了更多的灵活性，但最终语法就是语法。

<a id="d24e6106"></a>
外部语言没有这样的限制。只要您可以为该语言编写一个解析器，就可以开始了。有时您可以使用其他人的解析器（正如 Ansible 使用 YAML 所做的那样），但随后您又要做出妥协。

<a id="d24e6112"></a>
编写解析器可能意味着向您的应用程序添加新的库和可能的工具。编写一个好的解析器并不是一项简单的工作。但是，如果您感觉很坚强，您可以查看解析器生成器（例如 bison 或 ANTLR）以及解析框架（例如许多 PEG 解析器）。

<a id="d24e6132"></a>
我们的建议相当简单：花的精力不要超过节省的精力。编写领域语言会给您的项目增加一些成本，并且您需要确信存在可抵消的节省（从长远来看可能是这样）。

<a id="d24e6135"></a>
一般来说，如果可以的话，请使用现成的外部语言（例如 YAML、JSON 或 CSV）。如果没有，请查看内部语言。我们建议仅在您的语言由应用程序的用户编写的情况下才使用外部语言。

### 廉价的内部域语言

<a id="d24e6152"></a>
最后，如果您不介意主机语言语法泄漏，那么有一个创建内部域语言的作弊方法。不要进行大量元编程。相反，只需编写函数来完成这项工作。事实上，这几乎就是 RSpec 所做的事情：

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
在此代码中，describe、it、expect、to 和 eq 只是 Ruby 方法。关于对象如何传递，幕后有一些管道，但这只是代码。我们将在练习中对此进行一些探讨。

### 相关部分包括

- 主题 8，[*优秀设计的本质*](<08 The Essence of Good Design - essence_of_design.md#essence_of_design>)
- 主题 13，[*原型和便利贴*](<13 Prototypes and Post-it Notes - prototyping.md#prototyping>)
- 主题 32，[*配置*](<../05 Bend or Break/32 Configuration - configuration.md#configuration>)

### 挑战

<a id="d24e6233"></a>
<a id="d24e6255"></a>
- 您当前项目的一些需求可以用特定领域的语言表达吗？是否有可能编写一个可以生成大部分所需代码的编译器或翻译器？
- 如果您决定采用迷你语言作为更接近问题领域的编程方式，那么您就接受了需要付出一些努力来实现它们。您能否找到为一个项目开发的框架可以在其他项目中重用的方法？

### 练习

<a id="exercise-4"></a>
**练习 4** ([可能的答案](<../A2 Exercise Answers/README.md#answer-4>))

<a id="d24e6276"></a>
我们想要实现一种迷你语言来控制简单的海龟图形系统。该语言由单字母命令组成，有些命令后跟一个数字。例如，以下输入将绘制一个矩形：

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
实现解析该语言的代码。它的设计应该使得添加新命令变得简单。

<a id="exercise-5"></a>
**练习 5** ([可能的答案](<../A2 Exercise Answers/README.md#answer-5>))

<a id="d24e6321"></a>
在上一个练习中，我们为绘图语言实现了一个解析器——它是一种外部域语言。现在再次将其实现为内部语言。不要做任何聪明的事情：只需为每个命令编写一个函数即可。您可能必须将命令的名称更改为小写，并且可能将它们包装在某些内容中以提供一些上下文。

<a id="exercise-6"></a>
**练习 6** ([可能的答案](<../A2 Exercise Answers/README.md#answer-6>))

<a id="d24e6331"></a>
设计 BNF 语法来解析时间规范。以下所有示例均应被接受：

```
4pm, 7:38pm, 23:42, 3:16, 3:16am
```

<a id="exercise-7"></a>
**练习 7** ([可能的答案](<../A2 Exercise Answers/README.md#answer-7>))

<a id="d24e6353"></a>
使用 PEG 解析器生成器以您选择的语言实现上一个练习中的 BNF 语法的解析器。输出应该是一个整数，包含午夜过后的分钟数。

<a id="exercise-8"></a>
**练习 8** ([可能的答案](<../A2 Exercise Answers/README.md#answer-8>))

<a id="d24e6370"></a>
使用脚本语言和正则表达式实现时间解析器。
