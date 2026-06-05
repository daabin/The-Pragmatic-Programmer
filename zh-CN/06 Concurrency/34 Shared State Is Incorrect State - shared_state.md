<a id="shared_state"></a>
## 主题 34. 共享状态就是错误状态

<a id="d24e17333"></a>
你在你最喜欢的餐馆里。你吃完主菜，然后询问服务员是否还有苹果派。他回头一看，看到陈列柜里有一件作品，然后说是的。你点了它，心满意足地叹了口气。

<a id="d24e17344"></a>
与此同时，在餐厅的另一边，另一位顾客向服务员提出了同样的问题。她还查看并确认有一件，并且客户订购了。

<a id="d24e17346"></a>
其中一位顾客将会感到失望。

<a id="d24e17348"></a>
将展示柜换成联合银行账户，并将服务员变成销售点设备。您和您的伴侣同时决定购买一部新手机，但帐户中的余额只够一部手机使用。有人——银行、商店或者你——将会非常不高兴。

**提示 57：共享状态是不正确的状态**

<a id="d24e17356"></a>
问题在于共享状态。餐厅里的每个服务员都看着陈列柜，不顾对方。每个销售点设备都会查看帐户余额，而不考虑其他设备。

### 非原子更新

<a id="d24e17361"></a>
让我们看看我们的晚餐示例，就好像它是代码一样：

<a id="d24e17367"></a>
<a id="apie_case"></a>
![A figure shows a class diagram.](https://panzhongxian.cn/images/the-pragmatic-programmer/pie_case.png)

显示了 UML 类图。类名是具有属性“pie\_count: 1”的显示案例。该类与服务员 1 和服务员 2 相关联。服务员 1 显示条件，如果 display\_case.pie\_count > 0 Promise\_pie\_to\_customer() display\_case.take\_pie() Give\_pie\_to\_customer() 结束。服务员2显示条件，如果display\_case.pie\_count > 0，则promise\_pie\_to\_customer() display\_case.take\_pie()给出\_pie\_to\_customer()结束。

<a id="d24e17368"></a>
两个服务员同时操作（并且在现实生活中是并行的）。我们来看看他们的代码：

```
if display_case.pie_count > 0
  promise_pie_to_customer()
  display_case.take_pie()
  give_pie_to_customer()
end
```

<a id="d24e17391"></a>
服务员 1 获取当前饼数，发现是 1。他向顾客承诺馅饼。但就在这时，服务员 2 跑了。她还认为馅饼数是一，并向她的顾客做出了同样的承诺。然后，两个服务员中的一个拿起最后一块馅饼，另一个服务员进入某种错误状态（这可能涉及很多卑躬屈膝）。

<a id="d24e17393"></a>
这里的问题不在于两个进程可以写入同一内​​存。问题在于，两个进程都不能保证其对该内存的看法是一致的。实际上，当服务员执行 display\_case.pie\_count() 时，他们会将显示柜中的值复制到自己的内存中。如果展示柜中的值发生变化，他们的记忆（他们用来做出决定的）现在就已经过时了。

<a id="d24e17402"></a>
这都是因为获取然后更新饼图计数不是原子操作：底层值可能会在中间发生变化。

<a id="d24e17404"></a>
那么我们如何才能使其原子化呢？

#### 信号量和其他形式的互斥

<a id="d24e17409"></a>
信号量只是一种一次只有一个人可以拥有的东西。您可以创建一个信号量，然后使用它来控制对某些其他资源的访问。在我们的示例中，我们可以创建一个信号量来控制对饼图例的访问，并采用这样的约定：任何想要更新饼图例内容的人只有在持有该信号量时才能执行此操作。

<a id="d24e17434"></a>
假设用餐者决定使用物理信号量来解决馅饼问题。他们在馅饼盒上放了一个塑料妖精。在任何服务员出售馅饼之前，他们必须手里拿着妖精。一旦他们的订单完成（这意味着将馅饼送到桌子上），他们就可以将妖精放回原来看守馅饼宝藏的位置，准备调解下一个订单。

<a id="d24e17436"></a>
<a id="FNPTR-47"></a>
让我们用代码来看一下。传统上，获取信号量的操作称为 P，释放信号量的操作称为 V。<a href="36%20Blackboards%20-%20blackboards#FOOTNOTE-47">[47]</a> 今天我们使用诸如锁定/解锁、声明/释放等术语。

```
case_semaphore.lock()

if display_case.pie_count > 0
  promise_pie_to_customer()
  display_case.take_pie()
  give_pie_to_customer()
end

case_semaphore.unlock()
```

<a id="d24e17515"></a>
此代码假设已经创建了一个信号量并将其存储在变量 case\_semaphore 中。

<a id="d24e17520"></a>
我们假设两个服务员同时执行代码。他们都尝试锁定信号量，但只有一个成功。获得信号量的那个继续正常运行。没有获得信号量的将被挂起，直到信号量变得可用（服务员等待......）。当第一个服务员完成订单时，他们会解锁信号量，第二个服务员继续运行。他们现在发现箱子里没有馅饼，并向顾客道歉。

<a id="d24e17522"></a>
这种方法存在一些问题。也许最重要的是，它之所以有效，是因为访问饼图的每个人都同意使用信号量的约定。如果有人忘记了（也就是说，一些开发人员编写了不遵循约定的代码），那么我们就会陷入混乱。

#### 使资源具有事务性

<a id="d24e17528"></a>
当前的设计很糟糕，因为它将保护对馅饼盒的访问的责任委托给了使用它的人。让我们对其进行更改以集中控制。为此，我们必须更改 API 以便服务员可以检查计数并在一次调用中分得一杯羹：

```
slice = display_case.get_pie_if_available()
if slice
  give_pie_to_customer()
end
```

<a id="d24e17563"></a>
为了实现这一点，我们需要编写一个作为展示柜本身的一部分运行的方法：

```
def get_pie_if_available()     ####
  if @slices.size > 0             #
    update_sales_data(:pie)       #
    return @slices.shift          #
  else                            #  incorrect code!
    false                         #
  end                             #
end                            ####
```

<a id="d24e17630"></a>
这段代码说明了一个常见的误解。我们已将资源访问移至中心位置，但我们的方法仍然可以从多个并发线程调用，因此我们仍然需要使用信号量来保护它：

```
def get_pie_if_available()
  @case_semaphore.lock()

  if @slices.size > 0
    update_sales_data(:pie)
    return @slices.shift
  else
    false
  end

  @case_semaphore.unlock()
end
```

<a id="d24e17689"></a>
即使这段代码也可能不正确。如果 update\_sales\_data 引发异常，信号量将永远不会被解锁，并且所有将来对饼图的访问都将无限期挂起。我们需要处理这个：

```
def get_pie_if_available()
  @case_semaphore.lock()

  try {
    if @slices.size > 0
      update_sales_data(:pie)
      return @slices.shift
    else
      false
    end
  }
  ensure {
    @case_semaphore.unlock()
  }
end
```

<a id="d24e17772"></a>
因为这是一个常见的错误，所以许多语言都提供了可以为您处理此问题的库：

```
def get_pie_if_available()
  @case_semaphore.protect() {
    if @slices.size > 0
      update_sales_data(:pie)
      return @slices.shift
    else
      false
    end
  }
end
```

### 多资源交易

<a id="d24e17835"></a>
我们的餐厅刚刚安装了冰淇淋冰箱。如果顾客点了馅饼，服务员需要检查馅饼和冰淇淋是否都有。

<a id="d24e17844"></a>
我们可以将服务员代码更改为：

```
slice = display_case.get_pie_if_available()
scoop = freezer.get_ice_cream_if_available()

if slice  scoop
  give_order_to_customer()
end
```

<a id="d24e17868"></a>
但这是行不通的。如果我们要了一块馅饼，但当我们试图拿一勺冰淇淋时却发现没有，会发生什么？我们现在手里拿着一些我们无能为力的馅饼（因为我们的顾客必须有冰淇淋）。事实上，我们拿着馅饼意味着它不在盒子里，因此其他一些（作为纯粹主义者）不想要冰淇淋的顾客无法使用它。

<a id="d24e17873"></a>
我们可以通过向案例添加一个方法来解决这个问题，让我们返回一块馅饼。我们需要添加异常处理，以确保在出现故障时不会保留资源：

```
slice = display_case.get_pie_if_available()

if slice
  try {
      scoop = freezer.get_ice_cream_if_available()
      if scoop
      try {
        give_order_to_customer()
      }
      rescue {
        freezer.give_back(scoop)
      }
      end
  }
  rescue {
    display_case.give_back(slice)
  }
end
```

<a id="d24e17943"></a>
同样，这并不理想。现在的代码真的很难看：弄清楚它实际上做了什么很困难：业务逻辑被隐藏在所有的内务处理中。

<a id="d24e17946"></a>
之前，我们通过将资源处理代码移至资源本身来修复此问题。不过，在这里我们有两种资源。我们应该将代码放在展示柜还是冰箱中？

<a id="d24e17948"></a>
我们认为这两种选择的答案都是“否”。务实的做法是说“苹果派à la mode”是它自己的资源。我们会将此代码移动到一个新模块中，然后客户端只需说“给我加冰淇淋的苹果派”，它要么成功，要么失败。

<a id="d24e17950"></a>
当然，在现实世界中可能有很多像这样的复合菜品，您不会想为每个菜品编写新的模块。相反，您可能需要某种包含对其组件的引用的菜单项，然后有一个通用的 get\_menu\_item 方法来使资源与每个菜单项一起跳舞。

### 非事务性更新

<a id="d24e17958"></a>
人们对共享内存作为并发问题的根源给予了很多关注，但实际上，应用程序代码共享可变资源的任何地方都可能出现问题：文件、数据库、外部服务等。每当您的代码的两个或多个实例可以同时访问某些资源时，您就会遇到潜在的问题。

<a id="d24e17972"></a>
有时，资源并不那么明显。在编写本书的这个版本时，我们更新了工具链，以使用线程并行完成更多工作。这导致构建失败，但以奇怪的方式和随机的地方失败。所有错误的一个共同点是无法找到文件或目录，即使它们确实位于正确的位置。

<a id="d24e17974"></a>
我们追踪到代码中临时更改当前目录的几个位置。在非并行版本中，该代码将目录恢复回来就足够了。但在并行版本中，一个线程将更改目录，然后在该目录中，另一个线程将开始运行。该线程期望位于原始目录中，但由于当前目录在线程之间共享，因此情况并非如此。

<a id="d24e17976"></a>
这个问题的本质提示了另一个提示：

**提示 58：随机失败通常是并发问题**

### 其他类型的独家访问

<a id="d24e17999"></a>
大多数语言都有库支持对共享资源的某种独占访问。他们可能将其称为互斥体（用于互斥）、监视器或信号量。这些都是作为库实现的。

<a id="d24e18028"></a>
但是，某些语言本身内置了并发支持。例如，Rust 强化了数据所有权的概念；一次只有一个变量或参数可以保存对任何特定可变数据块的引用。

<a id="d24e18039"></a>
您还可以争辩说，函数式语言倾向于使所有数据不可变，从而使并发性变得更简单。然而，他们仍然面临着同样的挑战，因为在某些时候他们被迫踏入真实的、变化无常的世界。

### 医生，好痛……

<a id="d24e18054"></a>
如果您从本节中没有学到任何其他内容，请记住：共享资源环境中的并发性很困难，并且您自己管理它充满了挑战。

<a id="d24e18056"></a>
这就是为什么我们推荐这个老笑话的妙语：

<a id="d24e18059"></a>
> 医生，我这样做的时候会很痛。

<a id="d24e18062"></a>
> 那么就不要那么做。

<a id="d24e18064"></a>
接下来的几节提出了一些替代方法，可以轻松获得并发的好处。

### 相关部分包括

- 主题 10，<a href="../02%20Pragmatic%20Approach/10%20Orthogonality%20-%20orthogonality#orthogonality">正交性</a>
- 主题 28，<a href="../05%20Bend%20or%20Break/28%20Decoupling%20-%20coupling#coupling">解耦</a>
- 主题 38，<a href="../07%20While%20Coding/38%20Programming%20by%20Coincidence%20-%20coincidence#coincidence">巧合编程</a>
