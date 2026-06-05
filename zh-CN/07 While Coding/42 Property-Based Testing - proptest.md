<a id="proptest"></a>
## 主题 42. 基于性质的测试

> Доверяй, но проверяй（信任，但验证）
>
> 俄罗斯谚语

<a id="d24e22067"></a>
我们建议为您的函数编写单元测试。为此，您可以根据您对所测试事物的了解，思考可能存在问题的典型事物。

<a id="d24e22076"></a>
不过，该段落中潜伏着一个小但可能很重要的问题。如果您编写原始代码并编写测试，是否有可能在两者中都表达错误的假设？该代码通过了测试，因为它根据您的理解完成了预期的工作。

<a id="d24e22087"></a>
解决这个问题的一种方法是让不同的人编写测试和被测代码，但我们不喜欢这样：正如我们在主题 41 测试代码 中所说，考虑测试的最大好处之一是它告诉您编写的代码的方式。当测试工作与编码工作分开时，你就会失去这一点。

<a id="d24e22110"></a>
相反，我们赞成另一种选择，即计算机不会与您有先入之见，而是为您进行一些测试。

### 契约、不变量和属性

<a id="d24e22115"></a>
在主题 23 按合同设计 中，我们讨论了代码具有其满足的契约的想法：当您向其提供输入时满足条件，并且它将对其产生的输出做出某些保证。

<a id="d24e22136"></a>
还有一些代码不变量，即某些状态在通过函数传递时仍然保持不变。例如，如果对列表进行排序，结果将具有与原始元素相同的元素数量 - 长度不变。

<a id="d24e22141"></a>
一旦我们制定出契约和不变量（我们将把它们放在一起并称为属性），我们就可以使用它们来自动化我们的测试。我们最终所做的称为基于属性的测试。

**提示 71：使用基于属性的测试来验证您的假设**

<a id="d24e22159"></a>
作为一个人工示例，我们可以为排序列表构建一些测试。我们已经建立了一个属性：排序后的列表与原始列表的大小相同。我们还可以声明，结果中的任何元素都不能大于其后面的元素。

<a id="d24e22165"></a>
我们现在可以用代码来表达这一点。大多数语言都有某种基于属性的测试框架。这个示例是用 Python 编写的，并使用假设工具和 pytest，但原理非常通用。

<a id="d24e22174"></a>
这是测试的完整来源：

[proptest/sort.py](http://media.pragprog.com/titles/tpp20/code/proptest/sort.py)

```
from   hypothesis import given
import hypothesis.strategies as some

@given(some.lists(some.integers()))
def test_list_size_is_invariant_across_sorting(a_list):
    original_length = len(a_list)
    a_list.sort()
    assert len(a_list) == original_length

@given(some.lists(some.text()))
def test_sorted_result_is_ordered(a_list):
    a_list.sort()
    for i in range(len(a_list) - 1):
        assert a_list[i]
```

<a id="d24e22249"></a>
当我们运行它时会发生以下情况：

```
$ pytest sort.py
======================= test session starts ========================
...
plugins: hypothesis-4.14.0

sort.py ..                                                    [100%]

===================== 2 passed in 0.95 seconds =====================
```

<a id="d24e22276"></a>
那里没有太多戏剧性。但是，在幕后，Hypothesis 运行了我们的两个测试一百次，每次都传递不同的列表。这些列表的长度不同，内容也不同。就好像我们用 200 个随机列表准备了 200 个单独的测试。

### 测试数据生成

<a id="d24e22281"></a>
与大多数基于属性的测试库一样，Hypothesis 为您提供了一种迷你语言来描述它应该生成的数据。该语言基于对 Hypothesis.strategies 模块中函数的调用，我们将其别名为 some，只是因为它读起来更好。

<a id="d24e22298"></a>
如果我们写：

```
@given(some.integers())
```

<a id="d24e22306"></a>
我们的测试函数将运行多次。每次，都会传递一个不同的整数。如果我们编写以下内容：

```
@given(some.integers(min_value=5, max_value=10).map(lambda x: x * 2))
```

<a id="d24e22317"></a>
然后我们会得到 10 到 20 之间的偶数。

<a id="d24e22319"></a>
您还可以组合类型，以便

```
@given(some.lists(some.integers(min_value=1), max_size=100))
```

<a id="d24e22328"></a>
将是最多 100 个元素长的自然数列表。

<a id="d24e22330"></a>
这不应该是关于任何特定框架的教程，因此我们将跳过一些很酷的细节，而是看一个现实世界的示例。

### 寻找错误的假设

<a id="d24e22335"></a>
我们正在编写一个简单的订单处理和库存控制系统（因为总有空间容纳更多系统）。它使用 Warehouse 对象对库存水平进行建模。我们可以查询仓库以查看是否有库存、从库存中删除商品并获取当前库存水平。

<a id="d24e22340"></a>
这是代码：

[proptest/stock.py](http://media.pragprog.com/titles/tpp20/code/proptest/stock.py)

```
class Warehouse:
    def __init__(self, stock):
        self.stock = stock

    def in_stock(self, item_name):
        return (item_name in self.stock) and (self.stock[item_name] > 0)

    def take_from_stock(self, item_name, quantity):
        if quantity
```

<a id="d24e22422"></a>
我们编写了一个基本的单元测试，该测试通过了：

[proptest/stock.py](http://media.pragprog.com/titles/tpp20/code/proptest/stock.py)

```
def test_warehouse():
    wh = Warehouse({"shoes": 10, "hats": 2, "umbrellas": 0})
    assert wh.in_stock("shoes")
    assert wh.in_stock("hats")
    assert not wh.in_stock("umbrellas")

    wh.take_from_stock("shoes", 2)
    assert wh.in_stock("shoes")

    wh.take_from_stock("hats", 2)
    assert not wh.in_stock("hats")
```

<a id="d24e22502"></a>
然后我们编写了一个函数来处理从仓库订购商品的请求。它返回一个元组，其中第一个元素是“ok”或“not available”，后跟项目和请求的数量。我们还编写了一些测试，它们通过了：

[proptest/stock.py](http://media.pragprog.com/titles/tpp20/code/proptest/stock.py)

```
def order(warehouse, item, quantity):
    if warehouse.in_stock(item):
        warehouse.take_from_stock(item, quantity)
        return ( "ok", item, quantity )
    else:
        return ( "not available", item, quantity )
```

[proptest/stock.py](http://media.pragprog.com/titles/tpp20/code/proptest/stock.py)

```
def test_order_in_stock():
    wh = Warehouse({"shoes": 10, "hats": 2, "umbrellas": 0})
    status, item, quantity = order(wh, "hats", 1)
    assert status   == "ok"
    assert item     == "hats"
    assert quantity == 1
    assert wh.stock_count("hats") == 1

def test_order_not_in_stock():
    wh = Warehouse({"shoes": 10, "hats": 2, "umbrellas": 0})
    status, item, quantity = order(wh, "umbrellas", 1)
    assert status   == "not available"
    assert item     == "umbrellas"
    assert quantity == 1
    assert wh.stock_count("umbrellas") == 0

def test_order_unknown_item():
    wh = Warehouse({"shoes": 10, "hats": 2, "umbrellas": 0})
    status, item, quantity = order(wh, "bagel", 1)
    assert status   == "not available"
    assert item     == "bagel"
    assert quantity == 1
```

<a id="d24e22695"></a>
表面上，一切看起来都很好。但在我们发布代码之前，让我们添加一些属性测试。

<a id="d24e22697"></a>
我们知道的一件事是，股票在我们的交易中不会出现和消失。这意味着，如果我们从仓库中取出一些物品，我们取出的数量加上仓库中当前的数量应该与仓库中原来的数量相同。在下面的测试中，我们使用从“帽子”或“鞋子”中随机选择的项目参数以及从 1 到 4 中选择的数量来运行测试：

[proptest/stock.py](http://media.pragprog.com/titles/tpp20/code/proptest/stock.py)

```
@given(item     = some.sampled_from(["shoes", "hats"]),
       quantity = some.integers(min_value=1, max_value=4))

def test_stock_level_plus_quantity_equals_original_stock_level(item, quantity):
    wh = Warehouse({"shoes": 10, "hats": 2, "umbrellas": 0})
    initial_stock_level = wh.stock_count(item)
    (status, item, quantity) = order(wh, item, quantity)
    if status == "ok":
        assert wh.stock_count(item) + quantity == initial_stock_level
```

<a id="d24e22756"></a>
让我们运行一下：

```
$ pytest stock.py
. . .
stock.py:72:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
stock.py:76: in test_stock_level_plus_quantity_equals_original_stock_level
    (status, item, quantity) = order(wh, item, quantity)
stock.py:40: in order
    warehouse.take_from_stock(item, quantity)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = at 0x10cf97cf8>, item_name = 'hats'
quantity = 3

    def take_from_stock(self, item_name, quantity):
      if quantity
```

<a id="d24e22829"></a>
它在仓库中爆炸了。take\_from\_stock：我们试图从仓库中取出三顶帽子，但库存中只有两顶。

<a id="d24e22835"></a>
我们的属性测试发现了一个错误的假设：我们的 in\_stock 函数仅检查是否至少有一种给定的商品有库存。相反，我们需要确保我们有足够的资金来填写订单：

[proptest/stock1.py](http://media.pragprog.com/titles/tpp20/code/proptest/stock1.py)

```
def in_stock(self, item_name, quantity):
    return (item_name in self.stock) and (self.stock[item_name] >= quantity)
```

<a id="d24e22861"></a>
我们也改变了 order 函数：

[proptest/stock1.py](http://media.pragprog.com/titles/tpp20/code/proptest/stock1.py)

```
def order(warehouse, item, quantity):
    if warehouse.in_stock(item, quantity):
        warehouse.take_from_stock(item, quantity)
        return ( "ok", item, quantity )
    else:
        return ( "not available", item, quantity )
```

<a id="d24e22903"></a>
现在我们的财产测试通过了。

### 基于属性的测试常常会让您感到惊讶

<a id="d24e22909"></a>
在前面的示例中，我们使用基于属性的测试来检查库存水平是否已正确调整。测试发现了一个错误，但这与库存水平调整无关。相反，它在我们的 in\_stock 函数中发现了一个错误。

<a id="d24e22918"></a>
这既是基于属性的测试的优势，也是其缺点。它很强大，因为您设置了一些用于生成输入的规则，设置了一些用于验证输出的断言，然后就让它撕裂了。你永远不知道会发生什么。测试可能会通过。断言可能会失败。或者代码可能会完全失败，因为它无法处理给定的输入。

<a id="d24e22920"></a>
令人沮丧的是，确定失败的原因可能很棘手。

<a id="d24e22922"></a>
我们的建议是，当基于属性的测试失败时，找出它传递给测试函数的参数，然后使用这些值创建单独的常规单元测试。该单元测试为您做了两件事。首先，它可以让您专注于问题，而无需基于属性的测试框架对代码进行所有其他调用。其次，该单元测试充当回归测试。由于基于属性的测试会生成传递给测试的随机值，因此无法保证下次运行测试时将使用相同的值。通过强制使用这些值的单元测试可以确保这个错误不会被漏掉。

### 基于属性的测试也有助于您的设计

<a id="d24e22949"></a>
当我们谈论单元测试时，我们说过主要好处之一是它让您思考代码的方式：单元测试是您的 API 的第一个客户端。

<a id="d24e22980"></a>
基于属性的测试也是如此，但方式略有不同。它们让你从不变量和契约的角度思考你的代码；你思考什么是不能改变的，什么是必须真实的。这种额外的洞察力会对您的代码产生神奇的影响，消除边缘情况并突出显示使数据处于不一致状态的函数。

<a id="d24e22982"></a>
我们相信基于属性的测试是单元测试的补充：它们解决不同的问题，并且各自带来自己的好处。如果您目前没有使用它们，请尝试一下。

### 相关部分包括

- 主题 23，按合同设计
- 主题 25，断言编程
- 主题 45，需求坑

### 练习

<a id="exercise-31"></a>
**练习 31** (可能的答案)

<a id="d24e23014"></a>
回顾一下仓库的例子。还有其他可以测试的属性吗？

<a id="exercise-32"></a>
**练习 32** (可能的答案)

<a id="d24e23038"></a>
贵公司运送机械。每台机器都装在一个板条箱中，每个板条箱都是矩形的。板条箱的大小各不相同。您的工作是编写一些代码，将尽可能多的板条箱包装在适合送货卡车的单层中。代码的输出是所有板条箱的列表。对于每个板条箱，该列表给出了卡车中的位置以及宽度和高度。可以测试输出的哪些属性？

### 挑战

<a id="d24e23043"></a>
考虑一下您当前正在处理的代码。有哪些属性：契约和不变量？您可以使用基于属性的测试框架来自动验证这些吗？
