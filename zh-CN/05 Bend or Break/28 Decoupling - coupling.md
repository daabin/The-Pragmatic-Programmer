<a id="coupling"></a>
## 主题 28. 解耦

> 当我们试图单独挑选出任何东西时，我们发现它与宇宙中的其他一切都息息相关。
>
> 约翰·缪尔《我在山脉的第一个夏天》

<a id="d24e11901"></a>
在主题 8 <a href="../02%20Pragmatic%20Approach/08%20The%20Essence%20of%20Good%20Design%20-%20essence_of_design#essence_of_design">优秀设计的本质</a> 中，我们声称使用良好的设计原则将使您编写的代码易于更改。耦合是变化的敌人，因为它将必须并行变化的事物连接在一起。这使得改变变得更加困难：要么你花时间追踪所有需要改变的部分，要么你花时间想知道当你“只改变一件事”而不是与其耦合的其他事情时，为什么事情会崩溃。

<a id="d24e11924"></a>
当您设计一些想要刚性的东西时，例如桥梁或塔，您可以将组件耦合在一起：

<a id="d24e11926"></a>
![A link is shown with an interconnected pattern of each component in the link.](https://panzhongxian.cn/images/the-pragmatic-programmer/links-01.png)

<a id="d24e11927"></a>
这些连杆共同作用使结构变得刚性。

<a id="d24e11929"></a>
将其与类似的东西进行比较：

<a id="d24e11931"></a>
![A link is shown that resembles a tree-like structure.](https://panzhongxian.cn/images/the-pragmatic-programmer/links-02.png)

<a id="d24e11932"></a>
这里不存在结构刚性：各个链接可以改变，其他链接只能适应它。

<a id="d24e11934"></a>
当您设计桥梁时，您希望它们保持形状；你需要他们是严格的。但是，当您设计想要更改的软件时，您想要的恰恰相反：您希望它灵活。为了保持灵活性，各个组件应该与尽可能少的其他组件耦合。

<a id="d24e11936"></a>
而且，更糟糕的是，耦合是传递的：如果 A 耦合到 B 和 C，B 耦合到 M 和 N，C 耦合到 X 和 Y，那么 A 实际上耦合到 B、C、M、N、X 和 Y。

<a id="d24e11939"></a>
这意味着您应该遵循一个简单的原则：

**提示 44：解耦代码更容易更改**

<a id="d24e11947"></a>
鉴于我们通常不会使用钢梁和铆钉进行编码，那么解耦代码意味着什么呢？在本节中我们将讨论：

- 火车残骸——方法调用链
- 全球化——静态事物的危险
- 继承——为什么子类化是危险的

<a id="d24e12011"></a>
在某种程度上，这个列表是人为的：耦合几乎可以在两段代码共享某些内容的任何时候发生，因此当您阅读下面的内容时，请留意底层模式，以便您可以将它们应用到您的代码中。并留意耦合的一些症状：

<a id="d24e12022"></a>
<a id="d24e12034"></a>
<a id="d24e12037"></a>
<a id="d24e12044"></a>
- 不相关的模块或库之间的古怪依赖关系。
- 对一个模块的“简单”更改会通过系统中的不相关模块传播或破坏系统中其他地方的内容。
- 害怕更改代码的开发人员，因为他们不确定什么会受到影响。
- 每个人都必须参加的会议，因为没有人确定谁会受到变化的影响。

### 火车残骸

<a id="d24e12053"></a>
我们都见过（并且可能写过）这样的代码：

```
public void applyDiscount(customer, order_id, discount) {
  totals = customer
           .orders
           .find(order_id)
           .getTotals();
  totals.grandTotal = totals.grandTotal - discount;
  totals.discount   = discount;
}
```

<a id="d24e12098"></a>
我们从客户对象获取对某些订单的引用，使用它来查找特定订单，然后获取订单的总计集。使用这些总计，我们从订单总计中减去折扣，并用该折扣更新它们。

<a id="d24e12100"></a>
这段代码遍历了五个抽象级别，从客户到总金额。最终，我们的顶级代码必须知道客户对象公开订单，订单有一个 find 方法，该方法接受订单 id 并返回订单，并且订单对象有一个总计对象，该对象具有用于总计和折扣的 getter 和 setter。这是很多隐性知识。但更糟糕的是，如果这段代码要继续工作，很多事情将来都无法改变。火车中的所有车厢都耦合在一起，就像火车残骸中的所有方法和属性一样。

<a id="d24e12111"></a>
让我们想象一下，企业决定任何订单的折扣都不能超过 40%。我们应该把执行该规则的代码放在哪里？

<a id="d24e12113"></a>
你可能会说它属于我们刚刚编写的 applyDiscount 函数。这当然是答案的一部分。但按照现在的代码，您无法知道这就是完整的答案。任何地方的任何代码段都可以在总计对象中设置字段，如果该代码的维护者没有收到备忘录，它就不会根据新策略进行检查。

<a id="d24e12124"></a>
看待这个问题的一种方法是思考责任。当然，总计对象应该负责管理总计。但事实并非如此：它实际上只是一个任何人都可以查询和更新的一堆字段的容器。

<a id="d24e12129"></a>
解决这个问题的方法是应用我们所说的东西：

**提示 45：告诉，不要问**

<a id="d24e12145"></a>
该原则表明，您不应根据对象的内部状态做出决策，然后更新该对象。这样做完全破坏了封装的好处，并且这样做会在整个代码中传播实现的知识。因此，我们火车失事的第一个修复是将折扣委托给总对象：

```
public void applyDiscount(customer, order_id, discount) {
  customer
    .orders
    .find(order_id)
    .getTotals()
    .applyDiscount(discount);
}
```

<a id="d24e12182"></a>
对于客户对象及其订单，我们存在同样类型的“告诉不要询问”(TDA) 问题：我们不应该获取其订单列表并搜索它们。我们应该直接从客户那里获取我们想要的订单：

```
public void applyDiscount(customer, order_id, discount) {
  customer
    .findOrder(order_id)
    .getTotals()
    .applyDiscount(discount);
}
```

<a id="d24e12218"></a>
同样的事情也适用于我们的订单对象及其总计。为什么外界必须知道订单的实现使用单独的对象来存储其总计？

```
public void applyDiscount(customer, order_id, discount) {
  customer
    .findOrder(order_id)
    .applyDiscount(discount);
}
```

<a id="d24e12246"></a>
这就是我们可能会停下来的地方。

<a id="d24e12248"></a>
此时，您可能会认为 TDA 会让我们向客户添加 applyDiscountToOrder(order\_id) 方法。而且，如果盲目地遵循，它就会发生。

<a id="d24e12254"></a>
但 TDA 并不是自然法则；而是自然法则。这只是帮助我们认识问题的一种模式。在这种情况下，我们很乐意公开客户有订单的事实，并且我们可以通过询问客户对象来找到其中一个订单。这是一个务实的决定。

<a id="d24e12256"></a>
在每个应用程序中都有某些通用的顶级概念。在此应用程序中，这些概念包括客户和订单。将订单完全隐藏在客户对象中是没有意义的：它们有自己的存在。因此，我们可以毫无问题地创建公开订单对象的 API。

#### 得墨忒尔法则

<a id="d24e12267"></a>
<a id="FNPTR-37"></a>
人们经常谈论与耦合有关的德米特定律 (LoD)。 LoD 是 Ian Holland 在 80 年代末编写的一组指南<a href="32%20Configuration%20-%20configuration#FOOTNOTE-37">[37]</a>。他创建它们是为了帮助 Demeter 项目的开发人员保持其功能的简洁和解耦。

<a id="d24e12288"></a>
LoD 规定 C 类中定义的方法只能调用：

- C 中的其他实例方法
- 其参数
- 它在堆栈和堆中创建的对象中的方法
- 全局变量

<a id="d24e12306"></a>
在本书的第一版中，我们花了一些时间来描述 LoD。在接下来的 20 年里，那朵玫瑰的花朵已经凋谢了。我们现在不喜欢“全局变量”子句（原因我们将在下一节中讨论）。我们还发现，在实践中使用它很困难：这有点像每当调用方法时都必须解析法律文档。

<a id="d24e12310"></a>
然而，这个原则仍然是合理的。我们只是推荐一种更简单的方式来表达几乎相同的事情：

**提示 46：不要链接方法调用**

<a id="d24e12318"></a>
尽量不要有多个“。”当你访问某些东西时。访问某些内容还涵盖使用中间变量的情况，如以下代码所示：

```
# This is pretty poor style
amount = customer.orders.last().totals().amount;

# and so is this…
orders = customer.orders;
last   = orders.last();
totals = last.totals();
amount = totals.amount;
```

<a id="d24e12367"></a>
一点规则有一个很大的例外：如果您链接的东西真的非常不可能改变，则该规则不适用。实际上，应用程序中的任何内容都应该被认为可能会发生变化。第三方库中的任何内容都应被视为易失性，特别是如果已知该库的维护者会在版本之间更改 API。然而，该语言附带的库可能非常稳定，因此我们会对以下代码感到满意：

```
people
.sort_by {|person| person.age }
.first(10)
.map {| person | person.name }
```

<a id="d24e12394"></a>
20 年前，当我们编写第一版时，Ruby 代码就可以工作，并且当我们进入老程序员之家时（现在的任何一天......），它可能仍然可以工作。

#### 链条和管道

<a id="d24e12399"></a>
在主题 30 中，<a href="30%20Transforming%20Programming%20-%20function_pipelines#function_pipelines">转变编程</a> 我们讨论将函数组合到管道中。这些管道转换数据，将其从一个函数传递到下一个函数。这与方法调用的火车失事不同，因为我们不依赖隐藏的实现细节。

<a id="d24e12417"></a>
这并不是说管道不会引入一些耦合：它们确实会引入耦合。管道中一个函数返回的数据格式必须与下一个函数接受的格式兼容。

<a id="d24e12433"></a>
我们的经验是，这种形式的耦合对更改代码的障碍远小于火车残骸引入的形式。

### 全球化的弊端

<a id="d24e12445"></a>
全局可访问的数据是应用程序组件之间耦合的潜在根源。每条全局数据的行为就好像应用程序中的每个方法突然获得了一个附加参数：毕竟，该全局数据在每个方法中都可用。

<a id="d24e12462"></a>
全局耦合代码有很多原因。最明显的是，全局实现的更改可能会影响系统中的所有代码。当然，在实践中，影响相当有限。问题实际上归结为要知道你已经找到了所有需要改变的地方。

<a id="d24e12464"></a>
当需要拆分代码时，全局数据也会产生耦合。

<a id="d24e12466"></a>
人们已经对代码重用的好处进行了很多讨论。我们的经验是，重用可能不是创建代码时的主要关注点，但使代码可重用的想法应该成为编码例程的一部分。当您使代码可重用时，您可以为其提供干净的接口，从而将其与其余代码解耦。这允许您提取方法或模块，而无需拖动其他所有内容。如果您的代码使用全局数据，那么将其与其他数据分开就变得很困难。

<a id="d24e12477"></a>
当您为使用全局数据的代码编写单元测试时，您会遇到此问题。您会发现自己编写了一堆设置代码来创建一个全局环境，只是为了让您的测试能够运行。

**提示 47：避免全局数据**

#### 全局数据包括单例

<a id="d24e12515"></a>
在上一节中，我们小心地讨论了全局数据而不是全局变量。这是因为人们经常告诉我们“看！没有全局变量。我将其全部作为实例数据包装在单例对象或全局模块中。”

<a id="d24e12525"></a>
再试一次，斯基皮。如果您拥有的只是一个带有一堆导出实例变量的单例，那么它仍然只是全局数据。它只是有一个更长的名字。

<a id="d24e12527"></a>
因此，人们采用这个单例并将所有数据隐藏在方法后面。现在，他们不再使用 Config.log\_level 编码，而是使用 Config.log\_level() 或 Config.getLogLevel()。这更好，因为这意味着您的全球数据背后有一些智能。如果您决定更改日志级别的表示形式，则可以通过在配置 API 中新旧之间的映射来保持兼容性。但您仍然只有一组配置数据。

#### 全球数据包括外部资源

<a id="d24e12541"></a>
任何可变的外部资源都是全局数据。如果您的应用程序使用数据库、数据存储、文件系统、服务API等，则它有陷入全球化陷阱的风险。同样，解决方案是确保您始终将这些资源包装在您控制的代码后面。

**提示 48：如果它足够重要到全局，请将其包装在 API 中**

### 继承增加了耦合

<a id="d24e12565"></a>
子类化的误用（一个类从另一个类继承状态和行为）非常重要，因此我们在其自己的部分（主题 31，<a href="31%20Inheritance%20Tax%20-%20inheritance_tax#inheritance_tax">遗产税</a>）中对其进行讨论。

### 再说一次，一切都是为了改变

<a id="d24e12595"></a>
耦合代码很难改变：一个地方的改变可能会对代码中的其他地方产生二次影响，而且通常是在难以找到的地方，只有在生产一个月后才会被发现。

<a id="d24e12597"></a>
让你的代码保持低调：让它只处理它直接知道的事情，将有助于保持你的应用程序解耦，这将使它们更容易改变。

### 相关部分包括

<a id="FNPTR-38"></a>
- 主题 8，<a href="../02%20Pragmatic%20Approach/08%20The%20Essence%20of%20Good%20Design%20-%20essence_of_design#essence_of_design">优秀设计的本质</a>
- 主题 9，<a href="../02%20Pragmatic%20Approach/09%20DRY%20-%20The%20Evils%20of%20Duplication%20-%20dry#dry">DRY——重复的弊端</a>
- 主题 10，<a href="../02%20Pragmatic%20Approach/10%20Orthogonality%20-%20orthogonality#orthogonality">正交性</a>
- 主题 11，<a href="../02%20Pragmatic%20Approach/11%20Reversibility%20-%20reversi#reversi">可逆性</a>
- 主题 29，<a href="29%20Juggling%20the%20Real%20World%20-%20event#event">杂耍现实世界</a>
- 主题 30，<a href="30%20Transforming%20Programming%20-%20function_pipelines#function_pipelines">转变编程</a>
- 主题 31，<a href="31%20Inheritance%20Tax%20-%20inheritance_tax#inheritance_tax">遗产税</a>
- 主题 32，<a href="32%20Configuration%20-%20configuration#configuration">配置</a>
- 主题 33，<a href="../06%20Concurrency/33%20Breaking%20Temporal%20Coupling%20-%20temporal_coupling#temporal_coupling">打破时间耦合</a>
- 主题 34，<a href="../06%20Concurrency/34%20Shared%20State%20Is%20Incorrect%20State%20-%20shared_state#shared_state">共享状态是不正确的状态</a>
- 主题 35，<a href="../06%20Concurrency/35%20Actors%20and%20Processes%20-%20actor_model#actor_model">Actor 和进程</a>
- 主题 36，<a href="../06%20Concurrency/36%20Blackboards%20-%20blackboards#blackboards">黑板</a>
- 我们在 2003 年软件构建文章《调试的艺术》中讨论了“告诉，不要问”。<a href="32%20Configuration%20-%20configuration#FOOTNOTE-38">[38]</a>
