<a id="event"></a>
## 主题 29. 应对真实世界

> 事情不会自然而然地发生；它们是注定要发生的。
>
> 约翰·F·肯尼迪

<a id="d24e12677"></a>
在过去，当你的作者还拥有孩子气的英俊外表时，计算机并不是特别灵活。我们通常会根据他们的局限性来组织与他们互动的方式。

<a id="d24e12688"></a>
今天，我们期望更多：计算机必须融入我们的世界，而不是相反。我们的世界是混乱的：事情不断发生，东西四处移动，我们改变主意，……。我们编写的应用程序必须以某种方式弄清楚要做什么。

<a id="d24e12693"></a>
本节主要是关于编写这些响应式应用程序。

<a id="d24e12704"></a>
我们将从事件的概念开始。

### 活动

<a id="d24e12712"></a>
事件代表信息的可用性。它可能来自外部世界：用户单击按钮，或股票报价更新。它可能是内部的：计算结果已准备好，搜索完成。它甚至可以是像获取列表中的下一个元素一样微不足道的事情。

<a id="d24e12721"></a>
无论来源如何，如果我们编写响应事件的应用程序，并根据这些事件调整它们的操作，那么这些应用程序将在现实世界中更好地工作。他们的用户会发现它们更具交互性，并且应用程序本身将更好地利用资源。

<a id="d24e12723"></a>
但是我们如何编写这些类型的应用程序呢？如果没有某种策略，我们很快就会发现自己很困惑，我们的应用程序将是一堆紧密耦合的代码。

<a id="d24e12725"></a>
让我们看看四种有帮助的策略。

1. 有限状态机
2. 观察者模式
3. 发布/订阅
4. 反应式编程和流

### 有限状态机

<a id="d24e12846"></a>
Dave 发现他几乎每周都会使用有限状态机 (FSM) 编写代码。通常，FSM 的实现只是几行代码，但是这几行代码有助于解决大量潜在的混乱。

<a id="d24e12848"></a>
使用 FSM 非常简单，但许多开发人员却回避它们。人们似乎相信它们很困难，或者它们仅适用于您使用硬件的情况，或者您需要使用一些难以理解的库。这些都不是真的。

#### 实用主义 FSM 的剖析

<a id="d24e12853"></a>
状态机基本上只是如何处理事件的规范。它由一组状态组成，其中一个是当前状态。对于每个州，我们列出了对该州重要的事件。对于每个事件，我们定义系统的新当前状态。

<a id="d24e12858"></a>
例如，我们可能会从 websocket 接收多部分消息。第一条消息是标头。接下来是任意数量的数据消息，后面是尾随消息。这可以表示为如下的 FSM：

<a id="d24e12860"></a>
![An illustration explains a finite state machine diagram. The first state is the initial state. From the initial state, header message is passed to the reading message. The data message is imported in the reading message. From the initial state and the reading message state, the transition is done to error state and is detected and finally done. Also from the reading message state, trailer messages are accepted and finally done.](https://panzhongxian.cn/images/the-pragmatic-programmer/events_simple_fsm.png)

<a id="d24e12861"></a>
我们从“初始状态”开始。如果我们收到标题消息，我​​们就会转换到“正在阅读消息”状态。如果我们在初始状态（标有星号的行）时收到任何其他信息，我们将转换到“错误”状态，然后就完成了。

<a id="d24e12870"></a>
当我们处于“正在阅读消息”状态时，我们可以接受数据消息，在这种情况下我们可以在相同的状态下继续阅读，或者我们可以接受预告片消息，这会将我们转换到“完成”状态。任何其他情况都会导致转换到错误状态。

<a id="d24e12872"></a>
FSM 的巧妙之处在于我们可以将它们纯粹地表达为数据。这是代表我们的消息解析器的表格：

<a id="d24e12878"></a>
<a id="aevent_simple_fsm_table"></a>
![A table shows message parser information.](https://panzhongxian.cn/images/the-pragmatic-programmer/event_simple_fsm_table.png)

表格描述了有关消息解析器的信息。列标题包括标题、数据、尾部等。它们代表事件。行标题是初始的和正在阅读的。他们代表国家。第 1 行读取读数、错误、错误和错误。第 2 行读取错误、读取、完成和错误。

<a id="d24e12879"></a>
表中的行代表州。要了解事件发生时要做什么，请查找当前状态的行，然后扫描表示事件的列，该单元格的内容就是新状态。

<a id="d24e12881"></a>
处理它的代码同样简单：

[事件/简单\_fsm.rb](http://media.pragprog.com/titles/tpp20/code/event/simple_fsm.rb)

```
TRANSITIONS = {
  initial: {header: :reading},
  reading: {data: :reading, trailer: :done},
}

state = :initial

while state != :done  state != :error
  msg = get_next_message()
  state = TRANSITIONS[state][msg.msg_type] || :error
end
```

<a id="d24e12937"></a>
实现状态之间转换的代码位于第 10 行。它使用当前状态索引转换表，然后使用消息类型索引该状态的转换。如果没有匹配的新状态，则将状态设置为：error。

#### 添加动作

<a id="d24e12947"></a>
纯 FSM（例如我们刚才看到的）是一个事件流解析器。它唯一的输出是最终状态。我们可以通过添加在某些转换上触发的操作来增强它。

<a id="d24e12953"></a>
例如，我们可能需要提取源文件中的所有字符串。字符串是引号之间的文本，但字符串中的反斜杠会转义下一个字符，因此“忽略\”引号\“”是单个字符串。这是执行此操作的 FSM：

<a id="d24e12958"></a>
<a id="aevent_string_fsm"></a>
![A state diagram of three states is shown.](https://panzhongxian.cn/images/the-pragmatic-programmer/event_string_fsm.png)

状态图显示了三种状态。第一个状态是查找字符串。进程星号存在自循环。第二个状态是“串中”。从第一状态到第二状态的转换是通过“ch equals asterisk, do init result”完成的。进程“ch：任何其他内容，执行：添加到结果”存在自循环。第三种状态是“复制下一个字符”。从第二状态到第三状态的转换是通过“ch 等于反斜杠，添加到结果”来完成的。从第三状态到第二状态的转换是通过“ch 等于任何内容，添加到结果”来完成的。从第二状态到第一状态的转换是通过“ch等于双引号，do输出结果”完成的。

<a id="d24e12959"></a>
这次，每个转换都有两个标签。最上面的一个是触发它的事件，下面的一个是我们在状态之间移动时要采取的操作。

<a id="d24e12961"></a>
正如我们上次所做的那样，我们将在表格中表达这一点。然而，在这种情况下，表中的每个条目都是一个包含下一个状态和操作名称的两元素列表：

[事件/字符串\_fsm.rb](http://media.pragprog.com/titles/tpp20/code/event/strings_fsm.rb)

```
TRANSITIONS = {

  # current        new state        action to take
  #---------------------------------------------------------

  look_for_string: {
    '"'      => [ :in_string,       :start_new_string ],
    :default => [ :look_for_string, :ignore ],
  },

  in_string: {
    '"'      => [ :look_for_string, :finish_current_string ],
    '\\'     => [ :copy_next_char,  :add_current_to_string ],
    :default => [ :in_string,       :add_current_to_string ],
  },

  copy_next_char: {
    :default => [ :in_string,       :add_current_to_string ],
  },
}
```

<a id="d24e13069"></a>
我们还添加了指定默认转换的功能，如果事件与该状态的任何其他转换都不匹配，则采用该默认转换。

<a id="d24e13071"></a>
现在我们看一下代码：

[事件/字符串\_fsm.rb](http://media.pragprog.com/titles/tpp20/code/event/strings_fsm.rb)

```
state = :look_for_string
result = []

while ch = STDIN.getc
  state, action = TRANSITIONS[state][ch] || TRANSITIONS[state][:default]
  case action
  when :ignore
  when :start_new_string
    result = []
  when :add_current_to_string
    result
```

<a id="d24e13144"></a>
这与前面的示例类似，我们循环遍历事件（输入中的字符），触发转换。但它比以前的代码做了更多的事情。每次转换的结果都是一个新的状态和一个动作的名称。在返回循环之前，我们使用操作名称来选择要运行的代码。

<a id="d24e13146"></a>
这段代码非常基础，但它可以完成工作。还有许多其他变体：转换表可以使用匿名函数或函数指针来执行操作，您可以将实现状态机的代码包装在单独的类中，并具有自己的状态，等等。

<a id="d24e13148"></a>
没有什么可说的，你必须同时处理所有的状态转换。如果您正在执行在您的应用程序上注册用户的步骤，那么当用户输入详细信息、验证电子邮件、同意在线应用程序现在必须发出的 107 条不同的立法警告等时，可能会发生许多转换。将状态保存在外部存储中并使用它来驱动状态机是处理此类工作流要求的好方法。

#### 状态机是一个开始

<a id="d24e13153"></a>
状态机未被开发人员充分利用，我们鼓励您寻找应用它们的机会。但它们并不能解决与事件相关的所有问题。因此，让我们继续以其他方式来看待杂耍事件的问题。

### 观察者模式

<a id="d24e13177"></a>
在观察者模式中，我们有一个事件源（称为可观察对象）和一个对这些事件感兴趣的客户端（即观察者）列表。

<a id="d24e13221"></a>
观察者通常通过传递对要调用的函数的引用来向可观察者注册其兴趣。随后，当事件发生时，可观察对象会迭代其观察者列表并调用每个观察者传递给它的函数。该事件作为该调用的参数给出。

<a id="d24e13223"></a>
<a id="FNPTR-39"></a>
这是 Ruby 中的一个简单示例。 Terminator 模块用于终止应用程序。然而，在此之前，它会通知所有观察者应用程序将要退出。[[39]](<32 Configuration - configuration.md#FOOTNOTE-39>) 他们可能会使用此通知来整理临时资源、提交数据等：

[事件/观察者.rb](http://media.pragprog.com/titles/tpp20/code/event/observer.rb)

```
module Terminator
  CALLBACKS = []

  def self.register(callback)
    CALLBACKS
```

```
$ ruby event/observer.rb
callback 1 sees 99
callback 2 sees 99
```

<a id="d24e13336"></a>
创建可观察对象不需要太多代码：将函数引用推送到列表中，然后在事件发生时调用这些函数。这是何时不使用库的一个很好的例子。

<a id="d24e13341"></a>
观察者/可观察模式已经使用了几十年，并且对我们很有帮助。它在用户界面系统中尤其普遍，其中回调用于通知应用程序已发生某些交互。

<a id="d24e13343"></a>
但是观察者模式有一个问题：因为每个观察者都必须向可观察者注册，所以它引入了耦合。此外，由于在典型的实现中，回调是由可观察对象内联、同步处理的，因此可能会引入性能瓶颈。

<a id="d24e13346"></a>
这可以通过下一个策略“发布/订阅”来解决。

### 发布/订阅

<a id="d24e13351"></a>
发布/订阅（pubsub）概括了观察者模式，同时解决了耦合和性能问题。

<a id="d24e13372"></a>
在 pubsub 模型中，我们有发布者和订阅者。它们通过通道连接。这些通道是在单独的代码体中实现的：有时是一个库，有时是一个进程，有时是一个分布式基础设施。所有这些实现细节都对您的代码隐藏。

<a id="d24e13394"></a>
每个频道都有一个名称。订阅者注册对这些命名通道中的一个或多个感兴趣，发布者向它们写入事件。与观察者模式不同，发布者和订阅者之间的通信是在代码外部处理的，并且可能是异步的。

<a id="d24e13396"></a>
尽管您可以自己实现一个非常基本的 pubsub 系统，但您可能不想这样做。大多数云服务提供商都提供 pubsub 产品，允许您连接世界各地的应用程序。每种流行语言都至少有一个 pubsub 库。

<a id="d24e13402"></a>
Pubsub 是一种很好的解耦异步事件处理的技术。它允许在应用程序运行时添加和替换代码，而无需更改现有代码。缺点是很难看到大量使用 pubsub 的系统中发生了什么：您无法查看发布者并立即了解特定消息涉及哪些订阅者。

<a id="d24e13413"></a>
与观察者模式相比，pubsub 是通过共享接口（通道）进行抽象来减少耦合的一个很好的例子。然而，它基本上仍然只是一个消息传递系统。创建响应事件组合的系统需要的不仅仅是这些，所以让我们看看如何为事件处理添加时间维度。

### 响应式编程、流和事件

<a id="d24e13418"></a>
如果您曾经使用过电子表格，那么您就会熟悉响应式编程。如果一个单元格包含引用第二个单元格的公式，则更新第二个单元格也会导致第一个单元格更新。这些值会随着它们使用的值的变化而做出反应。

<a id="d24e13462"></a>
有许多框架可以帮助实现这种数据级反应性：在浏览器领域，React 和 Vue.js 是当前最受欢迎的框架（但是，这是 JavaScript，在本书印刷之前，这些信息就已经过时了）。

<a id="d24e13469"></a>
很明显，事件也可以用来触发代码中的反应，但了解它们并不一定容易。这就是流的用武之地。

<a id="d24e13474"></a>
流让我们将事件视为数据集合。这就好像我们有一个事件列表，当新事件到来时，列表就会变得更长。这样做的美妙之处在于，我们可以像对待任何其他集合一样对待流：我们可以操作、组合、过滤以及执行我们所熟知的所有其他数据相关的事情。我们甚至可以将事件流和常规集合结合起来。流可以是异步的，这意味着您的代码有机会在事件到达时对其进行响应。

<a id="d24e13480"></a>
当前反应式事件处理的事实上的基线是在网站 <http://reactivex.io> 上定义的，它定义了一组与语言无关的原则并记录了一些常见的实现。在这里，我们将使用 JavaScript 的 RxJs 库。

<a id="d24e13488"></a>
我们的第一个示例采用两个流并将它们压缩在一起：结果是一个新流，其中每个元素包含第一个输入流中的一个项目和另一个输入流中的一个项目。在本例中，第一个流只是五个动物名称的列表。第二个流更有趣：它是一个间隔计时器，每 500 毫秒生成一个事件。由于流被压缩在一起，因此仅当两个流上都有数据时才会生成结果，因此我们的结果流仅每半秒发出一个值：

[事件/rx0/index.js](http://media.pragprog.com/titles/tpp20/code/event/rx0/index.js)

```
import * as Observable from 'rxjs'
import { logValues }   from "../rxcommon/logger.js"

let animals  = Observable.of("ant", "bee", "cat", "dog", "elk")
let ticker   = Observable.interval(500)

let combined = Observable.zip(animals, ticker)

combined.subscribe(next => logValues(JSON.stringify(next)))
```

<a id="d24e13549"></a>
<a id="FNPTR-40"></a>
此代码使用一个简单的日志记录函数[[40]](<32 Configuration - configuration.md#FOOTNOTE-40>)，它将项目添加到浏览器窗口中的列表中。每个项目都带有自程序开始运行以来的时间（以毫秒为单位）的时间戳。这是我们的代码显示的内容：

<a id="d24e13565"></a>
![输出显示不同的时间戳。 502毫秒时输出为[“ant”, 0]； 1002毫秒时的输出为[“bee”, 1]； 1502毫秒处的输出为[“cat”, 2]； 2002毫秒时的输出为[“dog”, 3]； 2502毫秒时的输出为["elk", 4];](https://panzhongxian.cn/images/the-pragmatic-programmer/events_rxjs_0.png)

<a id="d24e13567"></a>
请注意时间戳：我们每 500 毫秒从流中获取一个事件。每个事件都包含一个序列号（由可观察的间隔创建）和列表中下一个动物的名称。在浏览器中实时观看，日志行每半秒出现一次。

<a id="d24e13572"></a>
事件流通常在事件发生时填充，这意味着填充它们的可观察量可以并行运行。下面是从远程站点获取有关用户的信息的示例。为此，我们将使用 <https://reqres.in>，这是一个提供开放 REST 接口的公共站点。作为 API 的一部分，我们可以通过对 users/«id» 执行 GET 请求来获取特定（假）用户的数据。我们的代码获取 ID 为 3、2 和 1 的用户：

[事件/rx1/index.js](http://media.pragprog.com/titles/tpp20/code/event/rx1/index.js)

```
import * as Observable from 'rxjs'
import { mergeMap }    from 'rxjs/operators'
import { ajax }        from 'rxjs/ajax'
import { logValues }   from "../rxcommon/logger.js"

let users = Observable.of(3, 2, 1)

let result = users.pipe(
  mergeMap((user) => ajax.getJSON(`https://reqres.in/api/users/${user}`))
)

result.subscribe(
  resp => logValues(JSON.stringify(resp.data)),
  err  => console.error(JSON.stringify(err))
)
```

<a id="d24e13654"></a>
代码的内部细节并不是太重要。令人兴奋的是结果，如下面的屏幕截图所示：

<a id="d24e13656"></a>
![An output is shown different timestamps. Information about id: 2 is displayed at 82 milliseconds, information about id: 1 is displayed at 132 milliseconds, and information about id: 3 is displayed at 133 milliseconds.](https://panzhongxian.cn/images/the-pragmatic-programmer/events_three_users.png)

<a id="d24e13657"></a>
查看时间戳：三个请求或三个单独的流是并行处理的，第一个返回的 id 2 花了 82 毫秒，接下来的两个请求分别在 50 和 51 毫秒后返回。

#### 事件流是异步集合

<a id="d24e13662"></a>
在前面的示例中，我们的用户 ID 列表（在可观察用户中）是静态的。但事实并非如此。也许我们想在人们登录我们的网站时收集这些信息。我们所要做的就是在创建会话时生成一个包含用户 ID 的可观察事件，并使用该可观察事件而不是静态事件。然后，当我们收到这些 ID 时，我们会获取有关用户的详细信息，并可能将它们存储在某个地方。

<a id="d24e13676"></a>
这是一个非常强大的抽象：我们不再需要将时间视为我们必须管理的东西。事件流将同步和异步处理统一在一个通用、方便的API后面。

### 事件无处不在

<a id="d24e13682"></a>
事件无处不在。有些是显而易见的：单击按钮、计时器到期。其他情况则不然：有人登录，文件中的一行与模式匹配。但无论其来源如何，围绕事件编写的代码都比其更线性的对应代码具有更高的响应速度和更好的解耦性。

### 相关部分包括

- 主题 28，[*解耦*](<28 Decoupling - coupling.md#coupling>)
- 主题 36，[*黑板*](<../06 Concurrency/36 Blackboards - blackboards.md#blackboards>)

### 练习

<a id="exercise-19"></a>
**练习 19** ([可能的答案](<../A2 Exercise Answers/README.md#answer-19>))

<a id="d24e13705"></a>
在 FSM 部分中，我们提到您可以将通用状态机实现移至其自己的类中。该类可能会通过传入转换表和初始状态来初始化。

<a id="d24e13753"></a>
尝试以这种方式实现字符串提取器。

<a id="exercise-20"></a>
**练习 20** ([可能的答案](<../A2 Exercise Answers/README.md#answer-20>))

<a id="d24e13763"></a>
其中哪些技术（可能组合使用）最适合以下情况：

<a id="d24e13767"></a>
<a id="d24e13773"></a>
<a id="d24e13776"></a>
<a id="d24e13779"></a>
- 如果您在五分钟内收到三个网络接口关闭事件，请通知操作人员。
- 如果在日落之后，并且在楼梯底部检测到运动，然后在楼梯顶部检测到运动，请打开楼上的灯。
- 您想要通知各种报告系统订单已完成。
- 为了确定客户是否有资格获得汽车贷款，应用程序需要向三个后端服务发送请求并等待响应。
