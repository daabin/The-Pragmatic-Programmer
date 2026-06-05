<a id="inheritance_tax"></a>
## 主题 31. 继承税

> 你想要一根香蕉，但你得到的是一只拿着香蕉的大猩猩和整个丛林。
>
> 乔·阿姆斯特朗

<a id="d24e15478"></a>
您使用面向对象语言进行编程吗？你使用继承吗？

<a id="d24e15504"></a>
如果是这样，停下来吧！这可能不是您想要做的。

<a id="d24e15506"></a>
让我们看看为什么。

### 一些背景

<a id="d24e15511"></a>
继承首次出现于 1969 年的 Simula 67 中。它是一个优雅的解决方案，解决了在同一列表中对多种类型的事件进行排队的问题。 Simula 方法是使用称为前缀类的东西。你可以写这样的东西：

```
link CLASS car;
  ... implementation of car

link CLASS bicycle;
  ... implementation of bicycle
```

<a id="d24e15542"></a>
link是一个前缀类，增加了链表的功能。这使您可以将汽车和自行车添加到等待（例如）交通灯的事物列表中。在当前的术语中，链接将是父类。

<a id="d24e15550"></a>
Simula 程序员使用的心智模型是，实例数据和类链接的实现被预先添加到类汽车和自行车的实现中。链接部分几乎被视为一个承载汽车和自行车的容器。这给了它们一种多态性：汽车和自行车都实现了链接接口，因为它们都包含链接代码。

<a id="d24e15574"></a>
<a id="FNPTR-44"></a>
Simula 之后出现了 Smalltalk。 Smalltalk 的创建者之一 Alan Kay 在 2019 年 Quora 回答<a href="32%20Configuration%20-%20configuration#FOOTNOTE-44">[44]</a> 中描述了为什么 Smalltalk 具有继承性：

<a id="d24e15590"></a>
> 因此，当我设计 Smalltalk-72 时，它是一种乐趣，同时
> 考虑 Smalltalk-71——我认为使用它会很有趣
> 类似 Lisp 的动力学，用“微分编程”做实验
> （意思是：完成“除了这个之外”的各种方法）。

<a id="d24e15592"></a>
这纯粹是为了行为而进行子类化。

<a id="d24e15594"></a>
这两种继承方式（实际上有相当多的共同点）在接下来的几十年中得到了发展。 Simula 方法表明继承是一种组合类型的方法，这种方法在 C++ 和 Java 等语言中得到了延续。 Smalltalk 学派认为继承是一种动态的行为组织，这一点在 Ruby 和 JavaScript 等语言中得到了体现。

<a id="d24e15615"></a>
因此，现在我们面临着一代 OO 开发人员，他们出于以下两个原因之一使用继承：他们不喜欢类型，或者他们喜欢类型。

<a id="d24e15618"></a>
那些不喜欢打字的人可以通过使用继承将通用功能从基类添加到子类中来节省手指：User 类和 Product 类都是 ActiveRecord::Base 的子类。

<a id="d24e15629"></a>
喜欢类型的人使用继承来表达类之间的关系：汽车是一种车辆。

<a id="d24e15637"></a>
不幸的是，两种继承都有问题。

### 使用继承共享代码的问题

<a id="d24e15642"></a>
继承就是耦合。子类不仅与父类、父类的父类耦合，而且使用子类的代码也与所有祖先类耦合。这是一个例子：

```
class Vehicle
  def initialize
    @speed = 0
  end
  def stop
    @speed = 0
  end
  def move_at(speed)
    @speed = speed
  end
end

class Car
```

<a id="d24e15757"></a>
当顶层调用 my\_car.move\_at 时，被调用的方法位于 Car 的父级 Vehicle 中。

<a id="d24e15768"></a>
现在负责Vehicle的开发者改变了API，所以move\_at变成了set\_velocity，实例变量@speed变成了@velocity。

<a id="d24e15785"></a>
API 的更改预计会破坏车辆类的客户端。但顶层并非如此：就其而言，它使用的是汽车。 Car类在实现方面做了什么，不是顶层代码关心的，但它仍然会崩溃。

<a id="d24e15796"></a>
类似地，实例变量的名称纯粹是内部实现细节，但是当 Vehicle 更改时，它也会（默默地）破坏 Car.

<a id="d24e15804"></a>
如此多的耦合。

#### 使用继承构建类型的问题

<a id="d24e15810"></a>
![A block diagram shows that Car and Bicycle fall under the same category "vehicle".](https://panzhongxian.cn/images/the-pragmatic-programmer/class_diagram_simple.png)

<a id="d24e15811"></a>
有些人将继承视为定义新类型的一种方式。他们最喜欢的设计图显示了类层次结构。他们以维多利亚时代的绅士科学家看待自然的方式看待问题，将其分解为不同的类别。

<a id="d24e15823"></a>
![A data tree structure is shown.](https://panzhongxian.cn/images/the-pragmatic-programmer/class_diagram_complex.png)

<a id="d24e15824"></a>
不幸的是，这些图表很快就变成了覆盖墙壁的怪物，一层又一层地添加，以表达类别之间差异的最小细微差别。这种增加的复杂性可能会使应用程序更加脆弱，因为更改可能会在许多层上上下波动。

<a id="d24e15826"></a>
但更糟糕的是多重继承问题。汽车可能是车辆的一种，但也可以是资产、保险项目、贷款抵押品等的一种。正确建模需要多重继承。

<a id="d24e15847"></a>
由于一些可疑的消歧语义，C++ 在 20 世纪 90 年代给多重继承带来了坏名声。因此，许多当前的面向对象语言不提供它。因此，即使您对复杂类型树感到满意，您也无法准确地对您的域进行建模。

**提示 51：不要缴纳遗产税**

### 替代方案更好

<a id="d24e15862"></a>
让我们建议三种技术，这意味着您永远不需要再次使用继承：

- 接口和协议
- 代表团
- Mixin 和特征

#### 接口和协议

<a id="d24e15902"></a>
大多数面向对象语言允许您指定一个类实现一组或多组行为。例如，您可以说 Car 类实现了 Drivable 行为和 Locatable 行为。用于执行此操作的语法有所不同：在 Java 中，它可能如下所示：

```
public class Car implements Drivable, Locatable {

  // Code for class Car. This code must include
  // the functionality of both Drivable
  // and Locatable

}
```

<a id="d24e15955"></a>
Driveable 和 Locatable 是 Java 所说的接口；其他语言将它们称为协议，有些语言将它们称为特征（尽管这不是我们稍后所说的特征）。

<a id="d24e15972"></a>
接口定义如下：

```
public interface Drivable {
  double getSpeed();
  void   stop();
}

public interface Locatable() {
  Coordinate getLocation();
  boolean    locationIsValid();
}
```

<a id="d24e16027"></a>
这些声明不创建任何代码：它们只是说任何实现 Drivable 的类都必须实现 getSpeed 和 stop 这两个方法，而 Locatable 的类必须实现 getLocation 和 locationIsValid。这意味着我们之前的 Car 类定义只有在包含所有这四种方法时才有效。

<a id="d24e16051"></a>
接口和协议之所以如此强大，是因为我们可以将它们用作类型，并且任何实现适当接口的类都将与该类型兼容。如果汽车和电话都实现了 Locatable，我们可以将两者存储在可定位项目列表中：

```
List items = new ArrayList
```

<a id="d24e16098"></a>
然后我们可以安全地处理该列表，因为我们知道每个项目都有 getLocation 和 locationIsValid：

```
void printLocation(Locatable item) {
  if (item.locationIsValid() {
    print(item.getLocation().asString());
}

// ...

items.forEach(printLocation);
```

**技巧 52：优先使用接口来表达多态性**

<a id="d24e16149"></a>
接口和协议为我们提供了无需继承的多态性。

#### 代表团

<a id="d24e16156"></a>
继承鼓励开发人员创建其对象具有大量方法的类。如果父类有 20 个方法，而子类只想使用其中两个，则其对象仍将保留另外 18 个方法并可调用。该类失去了对其接口的控制。这是一个常见问题 — 许多持久性和 UI 框架坚持要求应用程序组件对某些提供的基类进行子类化：

```
class Account
```

<a id="d24e16181"></a>
Account 类现在携带所有持久性类的 API。相反，想象一下使用委托的替代方案，如下例所示：

```
class Account
  def initialize(. . .)
    @repo = Persister.for(self)
  end

  def save
    @repo.save()
  end
end
```

<a id="d24e16236"></a>
现在，我们不再向我们的 Account 类的客户端公开任何框架 API：这种耦合现在已经被打破了。但还有更多。现在我们不再受到我们正在使用的框架的 API 的限制，我们可以自由地创建我们需要的 API 。是的，我们以前可以这样做，但是我们总是冒着我们编写的接口可以被绕过的风险，并且使用持久性 API 来代替。现在我们控制一切。

**提示 53：服务委托：Has-A 胜过 Is-A**

<a id="d24e16253"></a>
事实上，我们可以更进一步。为什么帐户必须知道如何保存自己？它的工作不是了解并执行账户业务规则吗？

```
class Account
  # nothing but account stuff
end

class AccountRecord
  # wraps an account with the ability
  # to be fetched and stored
end
```

<a id="d24e16288"></a>
现在我们确实脱钩了，但这是有代价的。我们必须编写更多代码，通常其中一些代码是样板文件：例如，我们所有的记录类可能都需要一个 find 方法。

<a id="d24e16293"></a>
幸运的是，这就是 mixins 和 Traits 为我们所做的事情。

#### Mixins、特征、类别、协议扩展……

<a id="d24e16298"></a>
作为一个行业，我们喜欢给事物命名。我们常常会给同一个东西起很多名字。越多越好，对吗？

<a id="d24e16317"></a>
这就是我们在查看 mixin 时要处理的问题。基本思想很简单：我们希望能够在不使用继承的情况下扩展具有新功能的类和对象。因此，我们创建一组这些函数，给该组命名，然后以某种方式用它们扩展一个类或对象。此时，您已经创建了一个新的类或对象，它结合了原始类或对象及其所有 mixins 的功能。在大多数情况下，即使您无权访问要扩展的类的源代码，您也能够进行此扩展。

<a id="d24e16319"></a>
现在，此功能的实现和名称因语言而异。我们在这里倾向于将它们称为 mixins，但我们真的希望您将其视为与语言无关的功能。重要的是所有这些实现都具有的功能：合并现有事物和新事物之间的功能。

<a id="d24e16330"></a>
作为示例，让我们回到我们的 AccountRecord 示例。当我们离开时，AccountRecord 需要了解两个帐户以及我们的持久性框架。它还需要委托持久层中想要向外界公开的所有方法。

<a id="d24e16338"></a>
Mixins 为我们提供了另一种选择。首先，我们可以编写一个 mixin 来实现（例如）三个标准查找器方法中的两个。然后我们可以将它们作为 mixin 添加到 AccountRecord 中。而且，当我们为持久化的事物编写新类时，我们也可以向它们添加 mixin：

```
mixin CommonFinders {
  def find(id) { ... }
  def findAll() { ... }
end

class AccountRecord extends BasicRecord with CommonFinders
class OrderRecord   extends BasicRecord with CommonFinders
```

<a id="d24e16380"></a>
我们可以更进一步。例如，我们都知道我们的业务对象需要验证代码来防止不良数据渗透到我们的计算中。但验证到底是什么意思呢？

<a id="d24e16392"></a>
例如，如果我们考虑一下，可能可以应用许多不同的验证层：

- 验证哈希密码是否与用户输入的密码匹配
- 创建帐户时验证用户输入的表单数据
- 验证管理员输入的表单数据并更新用户详细信息
- 验证其他系统组件添加到帐户的数据
- 在持久化之前验证数据的一致性

<a id="d24e16411"></a>
一种常见的（我们认为不太理想）方法是将所有验证捆绑到一个类（业务对象/持久性对象）中，然后添加标志来控制在哪种情况下触发哪种情况。

<a id="d24e16413"></a>
我们认为更好的方法是使用 mixin 为适当的情况创建专门的类：

```
class AccountForCustomer extends Account
     with AccountValidations,AccountCustomerValidations

class AccountForAdmin extends Account
     with AccountValidations,AccountAdminValidations
```

<a id="d24e16442"></a>
这里，两个派生类都包括所有帐户对象通用的验证。客户变体还包括适合面向客户的 API 的验证，而管理变体则包含（可能限制较少的）管理验证。

<a id="d24e16444"></a>
现在，通过来回传递 AccountForCustomer 或 AccountForAdmin 的实例，我们的代码会自动确保应用正确的验证。

**技巧 54：使用 Mixins 共享功能**

### 继承很少是答案

<a id="d24e16464"></a>
我们快速浏览了传统类继承的三种替代方案：

- 接口和协议
- 代表团
- Mixin 和特征

<a id="d24e16476"></a>
在不同的情况下，这些方法可能更适合您，具体取决于您的目标是共享类型信息、添加功能还是共享方法。与编程中的任何事情一样，旨在使用最能表达您意图的技术。

<a id="d24e16478"></a>
尽量不要拖累整个丛林。

### 相关部分包括

- 主题 8，<a href="../02%20Pragmatic%20Approach/08%20The%20Essence%20of%20Good%20Design%20-%20essence_of_design#essence_of_design">优秀设计的本质</a>
- 主题 10，<a href="../02%20Pragmatic%20Approach/10%20Orthogonality%20-%20orthogonality#orthogonality">正交性</a>
- 主题 28，<a href="28%20Decoupling%20-%20coupling#coupling">解耦</a>

### 挑战

- 下次当您发现自己进行子类化时，请花一点时间检查这些选项。你能通过接口、委托和/或混合来实现你想要的吗？这样做可以减少耦合吗？
