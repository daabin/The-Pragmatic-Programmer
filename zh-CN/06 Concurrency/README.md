---
sidebar_label: "6. 并发"
---


## 主题

- <a href="33%20Breaking%20Temporal%20Coupling%20-%20temporal_coupling">主题 33. 打破时间耦合</a>
- <a href="34%20Shared%20State%20Is%20Incorrect%20State%20-%20shared_state">主题 34. 共享状态就是错误状态</a>
- <a href="35%20Actors%20and%20Processes%20-%20actor_model">主题 35. Actor 与进程</a>
- <a href="36%20Blackboards%20-%20blackboards">主题 36. 黑板系统</a>

# 第 6 章 - 并发

<a id="d24e16817"></a>
为了让我们都在同一页面上，让我们从一些定义开始：

<a id="d24e16819"></a>
并发是指两段或多段代码的执行就像同时运行一样。并行是指它们同时运行。

<a id="d24e16838"></a>
为了实现并发，您需要在一个可以在代码运行时在不同部分之间切换执行的环境中运行代码。这通常是使用纤程、线程和进程等来实现的。

<a id="d24e16840"></a>
为了实现并行性，您需要能够同时执行两件事的硬件。这可能是一个 CPU 中的多个核心、一台计算机中的多个 CPU 或连接在一起的多台计算机。
