---
sidebar_label: 6. Concurrency
---

## Topics

- [Topic 33. Breaking Temporal Coupling](<33 Breaking Temporal Coupling - temporal_coupling.md>)
- [Topic 34. Shared State Is Incorrect State](<34 Shared State Is Incorrect State - shared_state.md>)
- [Topic 35. Actors and Processes](<35 Actors and Processes - actor_model.md>)
- [Topic 36. Blackboards](<36 Blackboards - blackboards.md>)

# Chapter 6 - Concurrency

<a id="d24e16817"></a>
Just so we're all on the same page, let's start with some definitions:

<a id="d24e16819"></a>
Concurrency is when the execution of two or more pieces of code act
as if they run at the same time. Parallelism is when they do
run at the same time.

<a id="d24e16838"></a>
To have concurrency, you need to run code in an environment that can
switch execution between different parts of your code when it is
running. This is often implemented using things such as fibers, threads,
and processes.

<a id="d24e16840"></a>
To have parallelism, you need hardware that can do two things at once.
This might be multiple cores in a CPU, multiple CPUs in a computer, or
multiple computers connected together.
