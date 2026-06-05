---
sidebar_label: "A2. 练习题参考答案"
---


<!-- Legacy anchor aliases preserved for intra-book links -->
<a id="d6040e2"></a>
<a id="d6040e55"></a>
<a id="d6040e93"></a>
<a id="d6040e120"></a>
<a id="d6040e160"></a>
<a id="d6040e197"></a>
<a id="d6040e240"></a>
<a id="d6040e275"></a>
<a id="d6040e306"></a>
<a id="d6040e349"></a>
<a id="d6040e383"></a>
<a id="d6040e418"></a>
<a id="d6040e452"></a>
<a id="d6040e510"></a>
<a id="d6040e541"></a>
<a id="d6040e572"></a>
<a id="d6040e610"></a>
<a id="d6040e641"></a>
<a id="d6040e675"></a>
<a id="d6040e709"></a>
<a id="d6040e743"></a>
<a id="d6040e783"></a>
<a id="d6040e818"></a>
<a id="d6040e849"></a>
<a id="d6040e892"></a>
<a id="d6040e927"></a>
<a id="d6040e970"></a>
<a id="d6040e1004"></a>
<a id="d6040e1054"></a>
<a id="d6040e1088"></a>

<a id="answers"></a>
# 附录 2 - 练习题参考答案

<a id="answer-1"></a>
**答案 1** （来自 [练习1](<../02 Pragmatic Approach/10 Orthogonality - orthogonality.md#exercise-1>)）

<a id="d24e27826"></a>
按照我们的思维方式，Split2 类更加正交。它专注于自己的任务，分割线路，而忽略诸如线路来自何处之类的细节。这不仅使代码更易于开发，而且也使其更加灵活。 Split2 可以分割从文件读取的行、由另一个例程生成的行或通过环境传入的行。

<a id="answer-2"></a>
**答案2**（来自[练习2](<../02 Pragmatic Approach/10 Orthogonality - orthogonality.md#exercise-2>)）

<a id="d24e27842"></a>
让我们从一个断言开始：您几乎可以用任何语言编写良好的正交代码。同时，每种语言都有诱惑：可能导致耦合增加和正交性降低的特性。

<a id="d24e27844"></a>
在面向对象语言中，多重继承、异常、运算符重载和父方法重写（通过子类化）等功能提供了充足的机会以非显而易见的方式增加耦合。还有一种耦合，因为类将代码与数据耦合起来。这通常是一件好事（当耦合良好时，我们称之为内聚）。但如果你的类不够集中，它可能会导致一些非常丑陋的界面。

<a id="d24e27846"></a>
在函数式语言中，鼓励您编写大量小的、解耦的函数，并以不同的方式组合它们来解决您的问题。理论上这听起来不错。在实践中常常如此。但这里也可能发生某种形式的耦合。这些函数通常会转换数据，这意味着一个函数的结果可以成为另一个函数的输入。如果您不小心，对函数生成的数据格式进行更改可能会导致转换流中的某个位置出现故障。具有良好类型系统的语言可以帮助缓解这种情况。

<a id="answer-3"></a>
**答案 3** （来自 [练习3](<../02 Pragmatic Approach/13 Prototypes and Post-it Notes - prototyping.md#exercise-3>)）

<a id="d24e27857"></a>
低技术来拯救！在白板上用记号笔画几幅漫画——一辆汽车、一部电话和一座房子。它不一定是伟大的艺术；它也可以是伟大的艺术。简笔画轮廓很好。将描述目标页面内容的便利贴放在可点击区域上。随着会议的进行，您可以优化便利贴的绘图和位置。

<a id="answer-4"></a>
**答案 4** （来自 [练习4](<../02 Pragmatic Approach/14 Domain Languages - domain_languages.md#exercise-4>)）

<a id="d24e27868"></a>
因为我们希望使语言可扩展，所以我们将使解析器表驱动。表中的每个条目都包含命令字母、表示是否需要参数的标志以及调用以处理该特定命令的例程的名称。

[郎/turtle.c](http://media.pragprog.com/titles/tpp20/code/lang/turtle.c)

```
typedef struct {
  char  cmd;              /* the command letter */
  int hasArg;             /* does it take an argument */
  void (*func)(int, int); /* routine to call */
} Command;

static Command cmds[] = {
  { 'P',  ARG,     doSelectPen },
  { 'U',  NO_ARG,  doPenUp },
  { 'D',  NO_ARG,  doPenDown },
  { 'N',  ARG,     doPenDir },
  { 'E',  ARG,     doPenDir },
  { 'S',  ARG,     doPenDir },
  { 'W',  ARG,     doPenDir }
};
```

<a id="d24e27951"></a>
主程序非常简单：读取一行，查找命令，获取参数（如果需要），然后调用处理函数。

[郎/turtle.c](http://media.pragprog.com/titles/tpp20/code/lang/turtle.c)

```
while (fgets(buff, sizeof(buff), stdin)) {

  Command *cmd = findCommand(*buff);

  if (cmd) {
    int   arg = 0;

    if (cmd->hasArg  !getArg(buff+1, )) {
      fprintf(stderr, "'%c' needs an argument\n", *buff);
      continue;
    }

    cmd->func(*buff, arg);
  }
}
```

<a id="d24e28006"></a>
查找命令的函数对表执行线性搜索，返回匹配条目或 NULL。

[郎/turtle.c](http://media.pragprog.com/titles/tpp20/code/lang/turtle.c)

```
Command *findCommand(int cmd) {
  int i;

  for (i = 0; i
```

<a id="d24e28058"></a>
最后，使用 sscanf 读取数字参数非常简单。

[郎/turtle.c](http://media.pragprog.com/titles/tpp20/code/lang/turtle.c)

```
int getArg(const char *buff, int *result) {
  return sscanf(buff, "%d", result) == 1;
}
```

<a id="answer-5"></a>
**答案5**（来自[练习5](<../02 Pragmatic Approach/14 Domain Languages - domain_languages.md#exercise-5>)）

<a id="d24e28100"></a>
实际上，您已经在上一个练习中解决了这个问题，您为外部语言编写了一个解释器，其中将包含内部解释器。在我们的示例代码中，这是 doXxx 函数。

<a id="answer-6"></a>
**答案 6** （来自 [练习6](<../02 Pragmatic Approach/14 Domain Languages - domain_languages.md#exercise-6>)）

<a id="d24e28113"></a>
使用 BNF，时间规范可以是

|  |  |  |
| --- | --- | --- |
| 时间 | ::= | 小时安培数 | 小时 : 分钟 ampm | 小时 : 分钟 |
|  |  |  |
| 安培姆 | ::= | 是 | 下午 |
|  |  |  |
| 小时 | ::= | 数字 | 数字 数字 |
|  |  |  |
| 分钟 | ::= | 数字 数字 |
|  |  |  |
| 数字 | ::= | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

<a id="d24e28244"></a>
小时和分钟的更好定义应考虑到小时只能从 00 到 23，分钟只能从 00 到 59：

|  |  |  |
| --- | --- | --- |
| 小时 | ::= | h-十位数字 | 数字 |
| 分钟 | ::= | m-十位数字 |
| h-tens | ::= | 0 | 1 |
| m-tens | ::= | 0 | 1 | 2 | 3 | 4 | 5 |
| 数字 | ::= | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

<a id="answer-7"></a>
**答案 7** （来自 [练习7](<../02 Pragmatic Approach/14 Domain Languages - domain_languages.md#exercise-7>)）

<a id="d24e28330"></a>
这是使用 Pegjs JavaScript 库编写的解析器：

[lang/peg\_parser/time\_parser.pegjs](http://media.pragprog.com/titles/tpp20/code/lang/peg_parser/time_parser.pegjs)

```
time
  = h:hour offset:ampm              { return h + offset }
  / h:hour ":" m:minute offset:ampm { return h + m + offset }
  / h:hour ":" m:minute             { return h + m }

ampm
  = "am" { return 0 }
  / "pm" { return 12*60 }

hour
  = h:two_hour_digits { return h*60 }
  / h:digit           { return h*60 }

minute
  = d1:[0-5] d2:[0-9] { return parseInt(d1+d2, 10); }

digit
  = digit:[0-9] { return parseInt(digit, 10); }

two_hour_digits
  = d1:[01] d2:[0-9 ] { return parseInt(d1+d2, 10); }
  / d1:[2]  d2:[0-3]  { return parseInt(d1+d2, 10); }
```

<a id="d24e28375"></a>
测试表明它在使用中：

[lang/peg\_parser/test\_time\_parser.js](http://media.pragprog.com/titles/tpp20/code/lang/peg_parser/test_time_parser.js)

```
let test = require('tape');
let time_parser = require('./time_parser.js');

// time    ::= hour ampm            |
//             hour : minute ampm   |
//             hour : minute
//
//  ampm   ::= am | pm
//
//  hour   ::= digit | digit digit
//
//  minute ::= digit digit
//
//  digit  ::= 0 |1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

const h  = (val) => val*60;
const m  = (val) => val;
const am = (val) => val;
const pm = (val) => val + h(12);

let tests = {

  "1am": h(1),
  "1pm": pm(h(1)),

  "2:30": h(2) + m(30),
  "14:30": pm(h(2)) + m(30),
  "2:30pm": pm(h(2)) + m(30),

}

test('time parsing', function (t) {
    for (const string in tests) {
      let result = time_parser.parse(string)
      t.equal(result, tests[string], string);
    }
    t.end()
});
```

<a id="answer-8"></a>
**答案 8** （来自[练习8](<../02 Pragmatic Approach/14 Domain Languages - domain_languages.md#exercise-8>)）

<a id="d24e28524"></a>
这是 Ruby 中可能的解决方案：

[lang/re\_parser/time\_parser.rb](http://media.pragprog.com/titles/tpp20/code/lang/re_parser/time_parser.rb)

```
TIME_RE = %r{
(?[0-9]){0}
(?[0-1]){0}
(?[0-6]){0}
(? am | pm){0}
(?   (\g \g) | \g){0}
(? \g  \g){0}

\A(
    ( \g \g )
  | ( \g : \g \g )
  | ( \g : \g )
)\Z

}x

def parse_time(string)
  result = TIME_RE.match(string)
  if result
    result[:hour].to_i * 60 +
    (result[:minute] || "0").to_i +
    (result[:ampm] == "pm" ? 12*60 : 0)
  end
end
```

<a id="d24e28676"></a>
（此代码使用在正则表达式开头定义命名模式的技巧，然后在实际匹配中将它们引用为子模式。）

<a id="answer-9"></a>
**答案 9** （来自 [练习9](<../02 Pragmatic Approach/15 Estimating - learn_to_estimate.md#exercise-9>)）

<a id="d24e28687"></a>
我们的答案必须基于几个假设：

- 存储设备中包含了我们需要传输的信息。
- 我们知道这个人行走的速度。
- 我们知道机器之间的距离。
- 我们没有考虑与存储设备之间传输信息所需的时间。
- 存储数据的开销大致等于通过通信线路发送数据的开销。

<a id="answer-10"></a>
**答案 10** （来自 [练习10](<../02 Pragmatic Approach/15 Estimating - learn_to_estimate.md#exercise-10>)）

<a id="d24e28713"></a>
根据之前答案中的注意事项：1TB 磁带包含 8×240 或 243 位，因此 1Gbps 线路必须传输数据约 9,000 秒或大约 2.5 小时，才能传输等量的信息。如果该人以 3.5 英里/小时的恒定速度行走，那么我们的两台机器需要相距近 9 英里，通信线路才能胜过我们的快递员。否则，这个人就赢了。

<a id="answer-14"></a>
**答案 14** （来自 [练习 14](<../04 Pragmatic Paranoia/23 Design by Contract - dbc.md#exercise-14>)）

<a id="d24e28729"></a>
我们将在 Java 中显示函数签名，并在注释中显示前置条件和后置条件。

<a id="d24e28731"></a>
首先，类的不变量：

```
/**
  * @invariant getSpeed() > 0
  *        implies isFull()              // Don't run empty
  *
  * @invariant getSpeed() >= 0
  *        getSpeed()
```

<a id="d24e28756"></a>
接下来，前置条件和后置条件：

```
/**
  * @pre Math.abs(getSpeed() - x)
```

<a id="answer-15"></a>
**答案 15** （来自 [练习15](<../04 Pragmatic Paranoia/23 Design by Contract - dbc.md#exercise-15>)）

<a id="d24e28842"></a>
该系列共有 21 个术语。如果您选择 20，则您刚刚遇到了栅栏柱错误（不知道是否计算栅栏柱或栅栏柱之间的空间）。

<a id="answer-16"></a>
**答案 16** （来自 [练习16](<../04 Pragmatic Paranoia/25 Assertive Programming - assertions.md#exercise-16>)）

<a id="d24e28854"></a>
<a id="d24e28857"></a>
<a id="d24e28860"></a>
<a id="d24e28888"></a>
<a id="d24e28891"></a>
<a id="d24e28894"></a>
- 1752年9月只有19天。这样做是为了同步日历，作为格里高利宗教改革的一部分。
- 该目录可能已被另一个进程删除，您可能没有读取它的权限，驱动器可能未安装，...；你明白了。
- 我们偷偷地没有指定 a 和 b 的类型。运算符重载可能已定义 +、= 或 != 来产生意外行为。此外，a 和 b 可能是同一变量的别名，因此第二次赋值将覆盖第一个赋值中存储的值。另外，如果程序是并发的并且编写得不好，则在添加发生时 a 可能已更新。
- 在非欧几里得几何中，三角形的内角之和不会等于 180°。想象一个映射在球体表面上的三角形。
- 闰分钟可能有 61 或 62 秒。
- 根据语言的不同，数字溢出可能会导致 a+1 为负值。

<a id="answer-17"></a>
**答案 17** （来自 [练习17](<../04 Pragmatic Paranoia/26 How to Balance Resources - balance_resources.md#exercise-17>)）

<a id="d24e28907"></a>
在大多数 C 和 C++ 实现中，无法检查指针是否实际指向有效内存。一个常见的错误是释放内存块并稍后在程序中引用该内存。到那时，所指向的内存很可能已被重新分配用于其他目的。通过将指针设置为 NULL，程序员希望防止这些恶意引用——在大多数情况下，取消引用 NULL 指针将生成运行时错误。

<a id="answer-18"></a>
**答案 18** （来自 [练习18](<../04 Pragmatic Paranoia/26 How to Balance Resources - balance_resources.md#exercise-18>)）

<a id="d24e28923"></a>
通过将引用设置为 NULL，可以将指向所引用对象的指针数量减少 1。一旦该计数达到零，该对象就有资格进行垃圾回收。将引用设置为 NULL 对于长时间运行的程序非常重要，程序员需要确保内存利用率不会随着时间的推移而增加。

<a id="answer-19"></a>
**答案 19** （来自 [练习19](<../05 Bend or Break/29 Juggling the Real World - event.md#exercise-19>)）

<a id="d24e28941"></a>
一个简单的实现可以是：

[事件/字符串\_ex\_1.rb](http://media.pragprog.com/titles/tpp20/code/event/strings_ex_1.rb)

```
class FSM
  def initialize(transitions, initial_state)
    @transitions = transitions
    @state       = initial_state
  end
  def accept(event)
    @state, action = TRANSITIONS[@state][event] || TRANSITIONS[@state][:default]
  end
end
```

<a id="d24e28985"></a>
（下载此文件以获取使用此新 FSM 类的更新代码。）

<a id="answer-20"></a>
**回答 20** （来自 [练习 20](<../05 Bend or Break/29 Juggling the Real World - event.md#exercise-20>)）

<a id="d24e28997"></a>
<a id="d24e29002"></a>
<a id="d24e29007"></a>
<a id="d24e29019"></a>
<a id="d24e29021"></a>
<a id="d24e29024"></a>
<a id="d24e29026"></a>
<a id="d24e29029"></a>
<a id="d24e29031"></a>
- …五分钟内发生三个网络接口关闭事件

这可以使用状态机来实现，但它比最初出现的要棘手：如果您在第 1、4、7 和 8 分钟收到事件，那么您应该在第四个事件上触发警告，这意味着状态机需要能够处理自身重置。

因此，事件流似乎是首选技术。有一个名为 buffer 的反应函数，带有大小和偏移参数，可让您返回每组三个传入事件。然后，您可以查看组中第一个和最后一个事件的时间戳，以确定是否应触发警报。
- ......日落之后，在楼梯底部检测到运动，然后在楼梯顶部检测到运动......

这可能可以使用 pubsub 和状态机的组合来实现。您可以使用 pubsub 将事件传播到任意数量的状态机，然后让状态机确定要做什么。
- …通知各个报告系统订单已完成。

这可能最好使用 pubsub 来处理。您可能想要使用流，但这需要被通知的系统也是基于流的。
- …三个后端服务并等待响应。

这类似于我们使用流来获取用户数据的示例。

<a id="answer-21"></a>
**答案 21** （来自[练习21](<../05 Bend or Break/30 Transforming Programming - function_pipelines.md#exercise-21>)）

<a id="d24e29043"></a>
<a id="d24e29049"></a>
<a id="d24e29052"></a>
<a id="d24e29059"></a>
1. 运费和销售税添加到订单中：

   ```
   basic order → finalized order
   ```

在传统代码中，您可能有一个计算运费的函数和另一个计算税费的函数。但我们在这里考虑的是转换，因此我们将只有商品的订单转换为一种新的东西：可以发货的订单。
2. 您的应用程序从命名文件加载配置信息：

   ```
   file name → configuration structure
   ```
3. 有人登录到 Web 应用程序：

   ```
   user credentials → session
   ```

<a id="answer-22"></a>
**答案 22** （来自 [练习22](<../05 Bend or Break/30 Transforming Programming - function_pipelines.md#exercise-22>)）

<a id="d24e29073"></a>
高层转型：

```
field contents as string
    → [validate  convert]
        → {:ok, value} | {:error, reason}
```

<a id="d24e29084"></a>
可以分为：

```
field contents as string
    → [convert string to integer]
    → [check value >= 18]
    → [check value
```

<a id="d24e29098"></a>
这假设您有一个错误处理管道。

<a id="answer-23"></a>
**答案 23** （来自 [练习23](<../05 Bend or Break/30 Transforming Programming - function_pipelines.md#exercise-23>)）

<a id="d24e29108"></a>
我们先回答第二部分：我们更喜欢第一段代码。

<a id="d24e29110"></a>
在第二块代码中，每个步骤都会返回一个实现我们调用的下一个函数的对象：content\_of 返回的对象必须实现 find\_matching\_lines，依此类推。

<a id="d24e29118"></a>
这意味着 content\_of 返回的对象与我们的代码耦合。想象一下需求发生了变化，我们必须忽略以 # 字符开头的行。在转换风格中，这很容易：

```
const content     = File.read(file_name);
const no_comments = remove_comments(content)
const lines       = find_matching_lines(no_comments, pattern)
const result      = truncate_lines(lines)
```

<a id="d24e29144"></a>
我们甚至可以交换remove\_comments 和find\_matching\_lines 的顺序，它仍然可以工作。

<a id="d24e29153"></a>
但在链式风格中，这会更加困难。我们的remove\_comments 方法应该位于哪里：在content\_of 返回的对象中还是在find\_matching\_lines 返回的对象中？如果我们更改该对象，还会破坏哪些其他代码？这种耦合就是方法链接风格有时被称为火车残骸的原因。

<a id="answer-24"></a>
**回答 24** （来自 [练习24](<../06 Concurrency/36 Blackboards - blackboards.md#exercise-24>)）

<a id="d24e29180"></a>
<a id="d24e29185"></a>
<a id="d24e29187"></a>
<a id="d24e29189"></a>
<a id="d24e29194"></a>
图像处理。 ：对于并行进程之间工作负载的简单调度，共享工作队列可能就足够了。如果涉及反馈，即，如果一个处理块的结果影响其他块（如机器视觉应用程序或复杂的 3D 图像扭曲变换），您可能需要考虑黑板系统。

组日历：这可能是一个不错的选择。您可以将安排的会议和空闲时间发布到黑板上。您拥有自主运作的实体，决策的反馈很重要，并且参与者可能会来来去去。

您可能需要考虑根据搜索者来划分这种黑板系统：初级员工可能只关心直属办公室，人力资源可能只想要全球范围内讲英语的办公室，而首席执行官可能想要整个辣酱玉米饼馅。

数据格式也有一定的灵活性：我们可以自由地忽略我们不理解的格式或语言。我们必须仅了解那些相互开会的办公室的不同格式，并且我们不需要让所有参与者都暴露于所有可能格式的完全传递闭包。这将耦合减少到必要的地方，并且不会人为地限制我们。

网络监控工具：这与[抵押/贷款申请程序](<../06 Concurrency/36 Blackboards - blackboards.md#mort>)非常相似。您收到了用户发送的故障报告和自动报告的统计数据，所有这些都发布到黑板上。人类或软件代理可以分析黑板来诊断网络故障：一条线上的两个错误可能只是宇宙射线，但如果出现 20,000 个错误，则说明出现了硬件问题。正如侦探解开谋杀之谜一样，您可以让多个实体分析并贡献想法来解决网络问题。

<a id="answer-25"></a>
**答案 25** （来自 [练习 25](<../07 While Coding/38 Programming by Coincidence - coincidence.md#exercise-25>)）

<a id="d24e29207"></a>
键值对列表的假设通常是键是唯一的，并且哈希库通常通过哈希本身的行为或使用重复键的显式错误消息来强制执行这一点。然而，数组通常没有这些约束，并且会很乐意存储重复的键，除非您专门对其进行编码。因此，在这种情况下，找到的第一个与 DepositAccount 匹配的键获胜，并且忽略任何剩余的匹配条目。无法保证条目的顺序，因此有时有效，有时无效。

<a id="d24e29212"></a>
那么开发和生产的机器有什么区别呢？这只是一个巧合。

<a id="answer-26"></a>
**答案 26** （来自 [练习26](<../07 While Coding/38 Programming by Coincidence - coincidence.md#exercise-26>)）

<a id="d24e29222"></a>
纯数字字段在美国、加拿大和加勒比地区有效这一事实纯属巧合。根据 ITU 规范，国际呼叫格式以文字 + 符号开头。 \* 字符也用于某些区域设置，更常见的是，前导零可以是数字的一部分。切勿将电话号码存储在数字字段中。

<a id="answer-27"></a>
**答案 27** （来自 [练习27](<../07 While Coding/38 Programming by Coincidence - coincidence.md#exercise-27>)）

<a id="d24e29238"></a>
取决于你在哪里。在美国，体积测量以加仑为基础，即高 6 英寸、直径 7 英寸的圆柱体的体积，四舍五入到最接近的立方英寸。

<a id="d24e29240"></a>
在加拿大，食谱中的“一杯”可能意味着以下任何一项

- 1/5 英制夸脱，即 227 毫升
- 1/4 美制夸脱，即 236 毫升
- 16 公制汤匙，或 240 毫升
- 1/4 升，即 250 毫升

<a id="d24e29256"></a>
<a id="FNPTR-85"></a>
除非你说的是电饭锅，在这种情况下“一杯”就是 180 毫升。这是根据“石”得出的，“石”是一个人一年所需干米的估计量：显然约为 180 升。电饭锅的杯子为 1 gō，即石的 1/1000。所以，大约是一个人一顿饭吃的米饭量。[[85]](#FOOTNOTE-85)

<a id="answer-28"></a>
**答案 28** （来自 [练习 28](<../07 While Coding/39 Algorithm Speed - algorithm_speed.md#exercise-28>)）

<a id="d24e29275"></a>
显然，我们无法对这个练习给出任何绝对的答案。不过，我们可以给您一些建议。

<a id="d24e29277"></a>
如果您发现结果不遵循平滑曲线，您可能需要检查是否有其他活动正在使用处理器的部分功能。如果后台进程定期从您的程序中夺走周期，您可能不会得到好的数据。您可能还想检查内存：如果应用程序开始使用交换空间，性能将会急剧下降。

<a id="d24e29279"></a>
这是在我们的一台机器上运行代码的结果图：

<a id="d24e29281"></a>
<a id="aalg-speed-rust-results"></a>
![A graph is drawn for time versus input size.](https://panzhongxian.cn/images/the-pragmatic-programmer/alg-speed-rust-results.png)

绘制图表来计算使用各种算法对整数向量进行排序的时间。横轴代表输入大小（除以 1000，快速排序则除以 100,000），范围从 0 到 110，增量为 10；纵轴代表时间（以毫秒为单位），范围从 0 到 16000，增量为 4000。气泡的曲线从原点开始，显示出快速增加，并在 (110, 14000) 处结束。选择和插入的曲线从原点开始，显示出非常缓慢的增加，并在 (110, 3500) 和 (110, 3600) 处结束。快速排序的线从原点开始，显示出非常小的增长，最后结束于 (110, 1000)。

<a id="answer-29"></a>
**答案 29** （来自 [练习29](<../07 While Coding/39 Algorithm Speed - algorithm_speed.md#exercise-29>)）

<a id="d24e29290"></a>
有几种方法可以到达那里。一是扭转问题。如果数组只有一个元素，我们就不会进行循环迭代。每一次额外的迭代都会使我们可以搜索的数组大小加倍。因此，数组大小的一般公式为 $n=2^m$，其中 $m$ 是迭代次数。如果将对数取每边以 2 为底，则得到 $\lg{n} = \lg{2^m}$，根据对数的定义，它变为 $\lg{n} = m$。

<a id="answer-30"></a>
**回答 30** （来自 [练习 30](<../07 While Coding/39 Algorithm Speed - algorithm_speed.md#exercise-30>)）

<a id="d24e29310"></a>
这可能有点让人回想起中学数学，但将以 $a$ 为底的对数转换为以 $b$ 为底的对数的公式是：

$$ \log\_{b}{x} = \frac{\log\_{a}{x}}{\log\_a{b}}$$

<a id="d24e29317"></a>
因为 $\log\_a{b}$ 是一个常量，所以我们可以在 Big-O 结果中忽略它。

<a id="answer-31"></a>
**答案 31** （来自 [练习31](<../07 While Coding/42 Property-Based Testing - proptest.md#exercise-31>)）

<a id="d24e29329"></a>
我们可以测试的一个属性是，如果仓库手头有足够的物品，则订单会成功。我们可以生成随机数量的商品订单，并验证如果仓库有库存，是否返回“OK”元组。

<a id="answer-32"></a>
**答案 32** （来自 [练习32](<../07 While Coding/42 Property-Based Testing - proptest.md#exercise-32>)）

<a id="d24e29342"></a>
这是基于属性的测试的一个很好的用途。单元测试可以关注通过其他方式得出结果的个别情况，属性测试可以关注以下内容：

- 有两个箱子重叠吗？
- 板条箱的任何部分是否超过卡车的宽度或长度？
- 包装密度（板条箱使用面积除以卡车车厢面积）是否小于或等于 1？
- 如果这是要求的一部分，堆积密度是否超过最低可接受密度？

<a id="answer-33"></a>
**答案 33** （来自 [练习33](<../08 Before the Project/45 The Requirements Pit - requirements.md#exercise-33>)）

<a id="d24e29367"></a>
<a id="d24e29370"></a>
<a id="d24e29375"></a>
<a id="d24e29377"></a>
<a id="d24e29379"></a>
<a id="d24e29382"></a>
<a id="d24e29385"></a>
<a id="d24e29388"></a>
1. 这个说法听起来像是一个真正的要求：应用程序的环境可能会受到限制。
2. 就其本身而言，该声明并不是真正的要求。但要找出真正需要什么，你必须问一个神奇的问题：“为什么？”

这可能是一个企业标准，在这种情况下，实际要求应该是“所有 UI 元素必须符合 MegaCorp 用户界面标准 V12.76”。

可能这是设计团队恰好喜欢的颜色。在这种情况下，您应该考虑设计团队也喜欢改变主意的方式，并将需求表述为“所有模式窗口的背景颜色必须是可配置的。出厂时，颜色将为灰色。”更好的是更广泛的声明“应用程序的所有视觉元素（颜色、字体和语言）都必须是可配置的。”

或者它可能只是意味着用户需要能够区分模态窗口和非模态窗口。如果是这样的话，还需要进行更多的讨论。
3. 这个声明不是要求，而是架构。面对这样的事情，你必须深入挖掘用户的想法。这是缩放问题吗？还是性能？成本？安全？答案将为您的设计提供信息。
4. 潜在的要求可能更接近“系统将阻止用户在字段中输入无效条目，并在输入这些条目时警告用户。”
5. 由于某些硬件限制，此声明可能是硬性要求。

<a id="d24e29392"></a>
这是四点问题的解决方案：

<a id="fourpost"></a>
<a id="d24e29402"></a>
![Four dots are shown. Three lines make the dots to form a triangle. A footnote reads, Connect the four dots with three lines, returning to the starting point, without lifting the pen.](https://panzhongxian.cn/images/the-pragmatic-programmer/four_dots_answer.png)

<a id="d24e29265"></a>
<a id="FOOTNOTE-85"></a>
[[85]](#FNPTR-85)感谢 Avi Bryant (@avibryant) 提供的这些琐事
