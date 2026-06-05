<a id="headlights"></a>
## 主题 27. 别跑得比车灯照得还远

> 做出预测是很困难的，尤其是对未来。
>
> 劳伦斯·“瑜伽士”·贝拉（Lawrence“Yogi”Berra），源自丹麦谚语

<a id="d24e11526"></a>
夜深了，天黑了，下着倾盆大雨。两人座的车在蜿蜒的小山路上急速行驶，几乎没有抓住拐角。一个发夹弯出现了，汽车错过了它，撞上了薄薄的护栏，在下面的山谷中猛烈地坠落。州警到达现场，高级警官悲伤地摇摇头。 “肯定跑得比他们的车灯还远。”

<a id="d24e11545"></a>
这辆超速行驶的两人座车的速度是否超过了光速？不，速度限制是固定的。警官所指的是驾驶员根据前灯的照明情况及时停车或转向的能力。

<a id="d24e11547"></a>
<a id="FNPTR-35"></a>
车头灯有一定的限制范围，称为投射距离。超过该点后，光线扩散就会变得过于分散而无法发挥作用。此外，前灯仅沿直线投射，不会照亮任何离轴的物体，例如道路上的弯道、山坡或陡坡。根据美国国家公路交通安全管理局的数据，近光灯的平均照射距离约为 160 英尺。不幸的是，时速 40 英里时的停车距离为 189 英尺，时速 70 英里时停车距离高达 464 英尺。[[35]](#FOOTNOTE-35) 事实上，实际上很容易超越你的车头灯。

<a id="d24e11557"></a>
在软件开发中，我们的“头灯”同样受到限制。我们看不到太远的未来，离轴越远，天就越黑。所以务实的程序员有一个严格的规则：

**提示 42：始终采取小步骤**

<a id="d24e11569"></a>
在继续之前，一定要采取小而深思熟虑的步骤，检查反馈并进行调整。考虑反馈率就是你的速度限制。你永远不会采取“太大”的步骤或任务。

<a id="d24e11575"></a>
我们所说的反馈到底是什么意思？任何独立证实或反驳你的行为的事情。例如：

- REPL 中的结果提供有关您对 API 和算法的理解的反馈
- 单元测试提供有关上次代码更改的反馈
- 用户演示和对话提供有关功能和可用性的反馈

<a id="d24e11622"></a>
什么任务太大了？任何需要“算命”的任务。就像汽车头灯的射程有限一样，我们只能看到未来也许一两步，最多可能几个小时或几天。除此之外，你可以很快超越有根据的猜测并进行疯狂的猜测。当您必须执行以下操作时，您可能会发现自己陷入了算命：

- 预计完成日期为未来几个月
- 规划未来维护或可扩展性的设计
- 猜测用户未来的需求
- 猜测未来技术的可用性

<a id="d24e11661"></a>
但是，我们听到你哭了，难道我们不应该为未来的维护而设计吗？是的，但仅限于一点：仅限于你能看到的最远的地方。你越需要预测未来，你犯错的风险就越大。您可以随时将代码设计为可替换的，而不是浪费精力为不确定的未来进行设计。让您可以轻松地丢弃您的代码并用更适合的代码替换它。使代码可替换还有助于内聚、耦合、解耦和 DRY，从而带来更好的整体设计。

<a id="d24e11685"></a>
尽管您可能对未来充满信心，但黑天鹅的机会总是存在。

### 黑天鹅

<a id="d24e11690"></a>
纳西姆·尼古拉斯·塔勒布 (Nassim Nicholas Taleb) 在他的著作《黑天鹅：极不可能发生的事件 [Tal10]](<../A2 Exercise Answers/README.md#d6040e970>) 中指出，历史上所有重大事件都来自引人注目的、难以预测的、超出正常预期范围的罕见事件。这些异常值虽然在统计上很少见，但却具有不成比例的影响。此外，我们自己的认知偏见往往会让我们忽视工作边缘发生的变化（参见主题 4，[*石汤和水煮田鸡*](<../01 Pragmatic Philosophy/04 Stone Soup and Boiled Frogs - stone_soup.md#stone_soup>)）。

<a id="d24e11709"></a>
<a id="FNPTR-36"></a>
在《程序员修炼之道》第一版出版期间，计算机杂志和在线论坛就以下紧迫问题展开了激烈的争论：“Motif 或 OpenLook 谁会赢得桌面 GUI 战争？”[[36]](#FOOTNOTE-36) 这是一个错误的问题。您可能从未听说过这些技术，因为它们都没有“获胜”，而且以浏览器为中心的网络很快就占据了主导地位。

**提示 43：避免算命**

<a id="d24e11734"></a>
很多时候，明天看起来很像今天。但不要指望它。

### 相关部分包括

- 主题 12，[*曳光弹*](<../02 Pragmatic Approach/12 Tracer Bullets - tracer_bullets.md#tracer_bullets>)
- 主题 13，[*原型和便利贴*](<../02 Pragmatic Approach/13 Prototypes and Post-it Notes - prototyping.md#prototyping>)
- 主题 40，[*重构*](<../07 While Coding/40 Refactoring - refactor.md#refactor>)
- 主题 41，[*测试代码*](<../07 While Coding/41 Test to Code - test_to_build.md#test_to_build>)
- 主题 48，[*敏捷的本质*](<../08 Before the Project/48 The Essence of Agility - essence_of_agility.md#essence_of_agility>)
- 主题 50，[*椰子不适合*](<../09 Pragmatic Projects/50 Coconuts Don't Cut It - do_what_works.md#do_what_works>)

<a id="d24e9114"></a>
<a id="FOOTNOTE-30"></a>
<a id="d24e10251"></a>
<a id="FOOTNOTE-31"></a>
<a id="d24e10431"></a>
<a id="FOOTNOTE-32"></a>
<a id="d24e10742"></a>
<a id="FOOTNOTE-33"></a>
<a id="d24e10955"></a>
<a id="FOOTNOTE-34"></a>
<a id="d24e11553"></a>
<a id="FOOTNOTE-35"></a>
<a id="d24e11715"></a>
<a id="FOOTNOTE-36"></a>
[[30]](<23 Design by Contract - dbc.md#FNPTR-30>)部分基于 Dijkstra、Floyd、Hoare、Wirth 等人的早期工作。

[[31]](<25 Assertive Programming - assertions.md#FNPTR-31>)在 C 和 C++ 中，这些通常作为宏实现。在 Java 中，断言默认是禁用的。使用 –enableassertions 标志调用 Java VM 以启用它们，并使其保持启用状态。

[[32]](<25 Assertive Programming - assertions.md#FNPTR-32>)<http://www.eps.mcgill.ca/jargon/jargon.html#heisenbug>

[[33]](<26 How to Balance Resources - balance_resources.md#FNPTR-33>)有关耦合代码危险的讨论，请参阅主题 28，[*解耦*](<../05 Bend or Break/28 Decoupling - coupling.md#coupling>)。

[[34]](<26 How to Balance Resources - balance_resources.md#FNPTR-34>)参见提示[这里](<../05 Bend or Break/30 Transforming Programming - function_pipelines.md#pg-donthoard>)。

[[35]](#FNPTR-35)根据 NHTSA，停止距离 = 反应距离 + 制动距离，假设平均反应时间为 1.5 秒，减速度为 17.02 英尺/秒²。

[[36]](#FNPTR-36)Motif 和 OpenLook 是基于 X-Window 的 Unix 工作站的 GUI 标准。
