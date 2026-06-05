---
sidebar_label: "5. 弯而不折"
---


## 主题

- <a href="28%20Decoupling%20-%20coupling">主题 28. 解耦</a>
- <a href="29%20Juggling%20the%20Real%20World%20-%20event">主题 29. 应对真实世界</a>
- <a href="30%20Transforming%20Programming%20-%20function_pipelines">主题 30. 变换式编程</a>
- <a href="31%20Inheritance%20Tax%20-%20inheritance_tax">主题 31. 继承税</a>
- <a href="32%20Configuration%20-%20configuration">主题 32. 配置</a>

# 第 5 章 - 弯而不折

<a id="d24e11772"></a>
生活并不是静止的。我们编写的代码也不能。为了跟上当今近乎疯狂的变化步伐，我们需要尽一切努力编写尽可能松散、尽可能灵活的代码。否则，我们可能会发现我们的代码很快就会过时，或者太脆弱而无法修复，并可能最终在奔向未来的疯狂冲刺中被抛在后面。

<a id="d24e11778"></a>
回到主题 11，<a href="../02%20Pragmatic%20Approach/11%20Reversibility%20-%20reversi#reversi">可逆性</a> 我们讨论了不可逆转决定的危险。在本章中，我们将告诉您如何做出可逆的决策，以便您的代码在面对不确定的世界时可以保持灵活性和适应性。

<a id="d24e11785"></a>
首先我们看看耦合——代码位之间的依赖关系。主题 28，<a href="28%20Decoupling%20-%20coupling#coupling">解耦</a> 展示了如何保持不同的概念分离，减少耦合。

<a id="d24e11806"></a>
接下来，我们将了解在主题 29，<a href="29%20Juggling%20the%20Real%20World%20-%20event#event">杂耍现实世界</a> 时可以使用的不同技术。我们将研究四种不同的策略来帮助管理和响应事件——这是现代软件应用程序的一个关键方面。

<a id="d24e11819"></a>
传统的过程代码和面向对象的代码对于您的目的来说可能过于紧密地耦合。在主题 30 <a href="30%20Transforming%20Programming%20-%20function_pipelines#function_pipelines">转变编程</a> 中，我们将利用函数管道提供的更灵活、更清晰的风格，即使您的语言不直接支持它们。

<a id="d24e11851"></a>
常见的面向对象风格可能会用另一个陷阱来诱惑您。不要上当，否则你最终将付出高昂的主题 31，<a href="31%20Inheritance%20Tax%20-%20inheritance_tax#inheritance_tax">遗产税</a> 的代价。我们将探索更好的替代方案，以保持您的代码灵活且更易于更改。

<a id="d24e11869"></a>
当然，保持灵活性的一个好方法是编写更少的代码。更改代码会让您有可能引入新的错误。主题 32，<a href="32%20Configuration%20-%20configuration#configuration">配置</a> 将解释如何将详细信息完全移出代码，以便可以更安全、更轻松地更改它们。

<a id="d24e11885"></a>
所有这些技术将帮助您编写可弯曲且不会破坏的代码。
