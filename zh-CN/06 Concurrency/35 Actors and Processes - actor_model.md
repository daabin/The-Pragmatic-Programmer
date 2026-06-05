<a id="actor_model"></a>
## 主题 35. Actor 与进程

> 没有作家，故事就写不出来；没有演员，故事就无法栩栩如生。
>
> 安吉·玛丽·德尔桑特

<a id="d24e18102"></a>
Actor 和进程提供了实现并发的有趣方法，而无需同步对共享内存的访问。

<a id="d24e18129"></a>
然而，在我们讨论它们之前，我们需要定义我们的意思。这听起来很学术。不用担心，我们很快就会解决这一切。

<a id="d24e18133"></a>
<a id="d24e18147"></a>
<a id="d24e18150"></a>
- 参与者是一个独立的虚拟处理器，具有自己的本地（和私有）状态。每个演员都有一个邮箱。当邮箱中出现一条消息并且 Actor 处于空闲状态时，它就会启动并处理该消息。当它完成处理时，它会处理邮箱中的另一条消息，或者，如果邮箱为空，它会返回睡眠状态。

处理消息时，参与者可以创建其他参与者，将消息发送给它知道的其他参与者，并创建一个新状态，该状态将在处理下一条消息时成为当前状态。
- 进程通常是更通用的虚拟处理器，通常由操作系统实现以促进并发。流程可以被限制（按照惯例）像参与者一样行事，这就是我们在这里指的流程类型。

### Actor只能并发

<a id="d24e18170"></a>
有一些东西你在演员的定义中找不到：

<a id="d24e18177"></a>
<a id="d24e18183"></a>
<a id="d24e18189"></a>
<a id="d24e18192"></a>
- 没有任何一件事是可以控制的。没有任何东西可以安排接下来发生的事情，或者协调从原始数据到最终输出的信息传输。
- 系统中唯一的状态保存在消息和每个参与者的本地状态中。除非由收件人阅读，否则无法检查消息，并且在参与者之外无法访问本地状态。
- 所有消息都是一种方式——没有回复的概念。如果您希望参与者返回响应，您可以在发送的消息中包含您自己的邮箱地址，并且它（最终）会将响应作为另一条消息发送到该邮箱。
- 参与者处理每条消息直至完成，并且一次仅处理一条消息。

<a id="d24e18194"></a>
因此，参与者并发、异步执行，并且不共享任何内容。如果您有足够的物理处理器，则可以在每个处理器上运行一个 actor。如果您有一个处理器，那么某些运行时可以处理它们之间的上下文切换。无论哪种方式，参与者中运行的代码都是相同的。

**提示 59：使用 Actor 实现没有共享状态的并发**

### 一个简单的 Actor

<a id="d24e18205"></a>
让我们使用演员来实现我们的餐厅。在本例中，我们将有三个（顾客、服务员和馅饼盒）。

<a id="d24e18207"></a>
整体消息流将如下所示：

<a id="d24e18211"></a>
<a id="d24e18214"></a>
<a id="d24e18217"></a>
<a id="d24e18220"></a>
<a id="d24e18223"></a>
- 我们（作为某种外在的、类似上帝的存在）告诉顾客他们饿了
- 作为回应，他们会向服务员要馅饼
- 服务员会要求馅饼盒给顾客拿一些馅饼
- 如果馅饼盒有一块可用，它会将其发送给顾客，并通知服务员将其添加到账单中
- 如果没有馅饼，情况告诉服务员，服务员向顾客道歉

<a id="d24e18225"></a>
<a id="FNPTR-48"></a>
我们选择使用 Nact 库来实现 JavaScript 中的代码。<a href="36%20Blackboards%20-%20blackboards#FOOTNOTE-48">[48]</a> 我们为此添加了一个小包装器，使我们可以将 actor 编写为简单对象，其中键是它接收的消息类型，值是接收到特定消息时要运行的函数。 （大多数 Actor 系统都有类似的结构，但细节取决于宿主语言。）

<a id="d24e18239"></a>
让我们从客户开始。客户可以收到三个消息：

- 你饿了（由外部上下文发送）
- 桌子上有馅饼（馅饼盒送来的）
- 抱歉，没有馅饼（服务员送来的）

<a id="d24e18251"></a>
这是代码：

[并发/actors/index.js](http://media.pragprog.com/titles/tpp20/code/concurrency/actors/index.js)

```
const customerActor = {
  'hungry for pie': (msg, ctx, state) => {
    return dispatch(state.waiter,
                    { type: "order", customer: ctx.self, wants: 'pie' })
  },

  'put on table': (msg, ctx, _state) =>
    console.log(`${ctx.self.name} sees "${msg.food}" appear on the table`),

  'no pie left': (_msg, ctx, _state) =>
    console.log(`${ctx.self.name} sulks…`)
}
```

<a id="d24e18322"></a>
有趣的情况是，当我们收到一条“想吃馅饼”消息时，我们会向服务员发送一条消息。（我们很快就会看到顾客如何了解服务员演员。）

<a id="d24e18325"></a>
这是服务员的代码：

[并发/actors/index.js](http://media.pragprog.com/titles/tpp20/code/concurrency/actors/index.js)

```
const waiterActor = {
  "order": (msg, ctx, state) => {
    if (msg.wants == "pie") {
      dispatch(state.pieCase,
               { type: "get slice", customer: msg.customer, waiter: ctx.self })
    }
    else {
      console.dir(`Don't know how to order ${msg.wants}`);
    }
  },

  "add to order": (msg, ctx) =>
    console.log(`Waiter adds ${msg.food} to ${msg.customer.name}'s order`),

  "error": (msg, ctx) => {
    dispatch(msg.customer, { type: 'no pie left', msg: msg.msg });
    console.log(`\nThe waiter apologizes to ${msg.customer.name}: ${msg.msg}`)
  }

};
```

<a id="d24e18432"></a>
当它收到来自客户的“订单”消息时，它会检查请求是否是馅饼。如果是这样，它会向饼盒发送请求，同时将引用传递给它自己和客户。

<a id="d24e18437"></a>
饼图盒具有状态：它所保存的所有饼图切片的数组。 （再次，我们很快就会看到它是如何设置的。）当它收到来自服务员的“获取切片”消息时，它会查看是否还有剩余的切片。如果是，它将切片传递给顾客，告诉服务员更新订单，最后返回更新后的状态，其中包含少一个切片。这是代码：

[并发/actors/index.js](http://media.pragprog.com/titles/tpp20/code/concurrency/actors/index.js)

```
const pieCaseActor = {
  'get slice': (msg, context, state) => {
    if (state.slices.length == 0) {
      dispatch(msg.waiter,
               { type: 'error', msg: "no pie left", customer: msg.customer })
      return state
    }
    else {
      var slice = state.slices.shift() + " pie slice";
      dispatch(msg.customer,
               { type: 'put on table', food: slice });
      dispatch(msg.waiter,
               { type: 'add to order', food: slice, customer: msg.customer });
      return state;
    }
  }
}
```

<a id="d24e18538"></a>
尽管您经常会发现参与者是由其他参与者动态启动的，但在我们的例子中，我们将保持简单并手动启动参与者。我们还将传递每个初始状态：

- 饼图案例获取其包含的饼图切片的初始列表
- 我们会给服务员提供馅饼盒的参考信息
- 我们会给顾客提供服务员的参考

[并发/actors/index.js](http://media.pragprog.com/titles/tpp20/code/concurrency/actors/index.js)

```
const actorSystem = start();

let pieCase = start_actor(
  actorSystem,
  'pie-case',
  pieCaseActor,
  { slices: ["apple", "peach", "cherry"] });

let waiter = start_actor(
  actorSystem,
  'waiter',
  waiterActor,
  { pieCase: pieCase });
```

```
let c1 = start_actor(actorSystem,   'customer1',
                     customerActor, { waiter: waiter });
let c2 = start_actor(actorSystem,   'customer2',
                     customerActor, { waiter: waiter });
```

<a id="d24e18632"></a>
最后我们开始吧。我们的顾客很贪婪。顾客 1 想要三片馅饼，顾客 2 想要两片：

[并发/actors/index.js](http://media.pragprog.com/titles/tpp20/code/concurrency/actors/index.js)

```
dispatch(c1, { type: 'hungry for pie', waiter: waiter });
dispatch(c2, { type: 'hungry for pie', waiter: waiter });
dispatch(c1, { type: 'hungry for pie', waiter: waiter });
dispatch(c2, { type: 'hungry for pie', waiter: waiter });
dispatch(c1, { type: 'hungry for pie', waiter: waiter });
sleep(500)
  .then(() => {
    stop(actorSystem);
  })
```

<a id="d24e18699"></a>
<a id="FNPTR-49"></a>
当我们运行它时，我们可以看到参与者进行通信。<a href="36%20Blackboards%20-%20blackboards#FOOTNOTE-49">[49]</a> 您看到的顺序可能会有所不同：

```
$ node index.js
customer1 sees "apple pie slice" appear on the table
customer2 sees "peach pie slice" appear on the table
Waiter adds apple pie slice to customer1's order
Waiter adds peach pie slice to customer2's order
customer1 sees "cherry pie slice" appear on the table
Waiter adds cherry pie slice to customer1's order

The waiter apologizes to customer1: no pie left
customer1 sulks…

The waiter apologizes to customer2: no pie left
customer2 sulks…
```

### 无显式并发

<a id="d24e18763"></a>
在参与者模型中，无需编写任何代码来处理并发，因为没有共享状态。也不需要以明确的端到端“做这个、做那个”逻辑进行编码，因为参与者根据他们收到的消息自行解决。

<a id="d24e18765"></a>
也没有提及底层架构。这组组件在单处理器、多核或多台联网机器上同样可以很好地工作。

### Erlang 搭建舞台

<a id="d24e18774"></a>
Erlang 语言和运行时是 Actor 实现的绝佳示例（尽管 Erlang 的发明者没有阅读原始的 Actor 论文）。 Erlang 将参与者称为进程，但它们不是常规的操作系统进程。相反，就像我们一直在讨论的参与者一样，Erlang 进程是轻量级的（您可以在一台机器上运行数百万个进程），并且它们通过发送消息进行通信。每个人都与其他人隔离，因此不存在状态共享。

<a id="d24e18796"></a>
此外，Erlang 运行时实现了一个监督系统，该系统管理进程的生命周期，在发生故障时可能会重新启动一个或一组进程。 Erlang 还提供热代码加载：您可以替换正在运行的系统中的代码，而无需停止该系统。 Erlang 系统运行一些世界上最可靠的代码，经常引用九个九的可用性。

<a id="d24e18821"></a>
但 Erlang（及其后代 Elixir）并不是独一无二的——大多数语言都有 actor 实现。考虑将它们用于并发实现。

### 相关部分包括

- 主题 28，<a href="../05%20Bend%20or%20Break/28%20Decoupling%20-%20coupling#coupling">解耦</a>
- 主题 30，<a href="../05%20Bend%20or%20Break/30%20Transforming%20Programming%20-%20function_pipelines#function_pipelines">转变编程</a>
- 主题 36，<a href="36%20Blackboards%20-%20blackboards#blackboards">黑板</a>

### 挑战

<a id="d24e18845"></a>
<a id="d24e18852"></a>
- 您当前是否有使用互斥来保护共享数据的代码。为什么不尝试使用 actor 编写相同代码的原型呢？
- 餐厅的参与者代码仅支持订购馅饼片。将其扩展为让顾客按菜单点馅饼，并由单独的代理管理馅饼片和冰淇淋勺。安排好事情，以便它能够处理其中一个耗尽的情况。
