<a id="safety"></a>
## 主题 43. 在外务必注意安全

> 好的栅栏造就好邻居。
>
> 罗伯特·弗罗斯特《修补墙》

<a id="d24e23083"></a>
在第一版关于代码耦合的讨论中，我们做了一个大胆而天真的声明：“我们不需要像间谍或持不同政见者那样偏执。”我们错了。事实上，你确实需要每天都那么偏执。

<a id="d24e23097"></a>
当我们撰写本文时，每日新闻充斥着毁灭性数据泄露、系统被劫持和网络欺诈的故事。数亿条记录同时被盗，造成数十亿美元的损失和补救，而且这些数字每年都在快速增长。在绝大多数情况下，这并不是因为攻击者非常聪明，甚至不是因为攻击者能力模糊。

<a id="d24e23099"></a>
就是因为开发商不小心。

### 其余90%

<a id="d24e23104"></a>
<a id="FNPTR-62"></a>
编码时，您可能会经历几个“它有效！”的循环。以及“为什么这不起作用？”偶尔会说“这不可能发生……”[62] 在爬上几座山丘和颠簸之后，很容易对自己说，“唷，这一切都成功了！”并宣布代码完成。当然，这还没有完成。您已经完成了 90%，但现在您还需要考虑其他 90%。

<a id="d24e23115"></a>
您要做的下一件事是分析代码，找出可能出错的方式，并将其添加到您的测试套件中。您将考虑诸如传递错误参数、泄漏或不可用资源等问题；之类的事情。

<a id="d24e23117"></a>
在过去的美好时光，这种对内部错误的评估可能就足够了。但今天这只是一个开始，因为除了内部原因造成的错误之外，您还需要考虑外部参与者如何故意搞砸系统。但也许你会抗议，“哦，没有人会关心这段代码，它不重要，甚至没有人知道这个服务器……”外面的世界很大，而且大部分都是相连的。无论是地球另一端的无聊孩子、国家支持的恐怖主义、犯罪团伙、企业间谍，甚至是复仇心重的前任，他们都在那里瞄准你。开放网络上未打补丁的过时系统的生存时间以分钟为单位，甚至更短。

<a id="d24e23123"></a>
通过默默无闻来保证安全是行不通的。

### 安全基本原则

<a id="d24e23128"></a>
务实的程序员有一定程度的偏执。我们知道我们有缺陷和局限性，外部攻击者会抓住我们留下的任何漏洞来破坏我们的系统。您的特定开发和部署环境将有其自己的以安全为中心的需求，但您应该始终牢记一些基本原则：

1. 最小化攻击面
2. 最小特权原则
3. 安全默认值
4. 加密敏感数据
5. 维护安全更新

<a id="d24e23206"></a>
让我们逐一看一下。

#### 最小化攻击面

<a id="d24e23211"></a>
系统的攻击面是攻击者可以输入数据、提取数据或调用服务执行的所有访问点的总和。以下是一些示例：

<a id="d24e23229"></a>
代码复杂性导致攻击向量：代码复杂性使攻击面更大，产生意外副作用的机会更多。将复杂的代码视为使表面区域变得更加多孔并且容易受到感染。再说一遍，简单、较小的代码更好。更少的代码意味着更少的错误，更少的严重安全漏洞的机会。更简单、更紧凑、不太复杂的代码更容易推理，更容易发现潜在的弱点。

<a id="d24e23242"></a>
<a id="FNPTR-63"></a>
<a id="d24e23305"></a>
<a id="d24e23315"></a>
<a id="d24e23353"></a>
<a id="d24e23371"></a>
<a id="d24e23390"></a>
输入数据是一种攻击媒介：永远不要信任来自外部实体的数据，始终在将其传递到数据库、视图渲染或其他处理之前对其进行清理。[63] 某些语言可以帮助解决此问题。例如，在 Ruby 中，保存外部输入的变量受到污染，这限制了可以对它们执行的操作。例如，此代码显然使用 wc 实用程序来报告其名称在运行时提供的文件中的字符数： : [安全/taint.rb](http://media.pragprog.com/titles/tpp20/code/safety/taint.rb)

    ```
    puts "Enter a file name to count: "
    name = gets
    system("wc -c #{name}")
    ```
: 恶意用户可能会造成如下损害： : ``` 输入要计数的文件名：test.dat; rm -rf /
    ```
:   However, setting the SAFE level to 1 will taint external data, which
    means it can't be used in dangerous contexts:
:   ```
    $SAFE = 1

    puts "Enter a file name to count: "
    name = gets
    system("wc -c #{name}")
    ```
: 现在，当我们运行它时，我们会被当场抓获: : ``` $ ruby taint.rb Enter a file name to count: test.dat; rm -rf / code/safety/taint.rb:5:in `system': Insecure opera - system (SecurityError) from code/safety/taint.rb:5:in `main
    ```

Unauthenticated services are an attack vector
:   By their very nature, any user anywhere in the world can call unauthenticated services, so barring any other handling or limiting you've immediately created an opportunity for a denial-of-service attack at the very least. Quite a few of highly public data breaches recently were caused by developers accidentally putting data in unauthenticated, publicly readable data stores in the cloud.

Authenticated services are an attack vector
:   Keep the number of authorized users at an absolute minimum. Cull unused, old, or outdated users and services. Many net-enabled devices have been found to contain simple default passwords or unused, unprotected administrative accounts. If an account with deployment credentials is compromised, your entire product is compromised.

Output data is an attack vector
:   There's a (possibly apocryphal) story about a system that dutifully reported the error message Password is used by another user. Don't give away information. Make sure that the data you report is appropriate for the authorization of that user. Truncate or obfuscate potentially risky information such as Social Security or other government ID numbers.

<a id="d24e23414"></a>
<a id="FNPTR-64"></a>
Debugging info is an attack vector
:   There's nothing as heartwarming as seeing a full stack trace with data on your local ATM machine, an airport kiosk, or crashing web page. Information designed to make debugging easier can make breaking in easier as well. Make sure any “test window” (discussed here) and runtime exception reporting is protected from spying eyes.[64]

**Tip 72: Keep It Simple and Minimize Attack Surfaces**

#### Principle of Least Privilege

<a id="d24e23460"></a>
Another key principle is to use the least amount of privilege for the shortest time you can get away with. In other words, don't automatically grab the highest permission level, such as root or Administrator. If that high level is needed, take it, do the minimum amount of work, and relinquish your permission quickly to reduce the risk. This principle dates back to the early 1970s:

<a id="d24e23498"></a>
> Every program and every privileged user of the system should operate using the least amount of privilege necessary to complete the job.— Jerome Saltzer, Communications of the ACM, 1974.

<a id="d24e23500"></a>
Take the login program on Unix-derived systems. It initially executes with root privileges. As soon as it finishes authenticating the correct user, though, it drops the high level privilege to that of the user.

<a id="d24e23505"></a>
This doesn't just apply to operating system privilege levels. Does
your application implement different levels of access? Is it a blunt
tool, such as “administrator” vs. “user?” If so, consider something more
finely grained, where your sensitive resources are partitioned into
different categories, and individual users have permissions for only
certain of those categories.

<a id="d24e23507"></a>
This technique follows the same sort of idea as minimizing surface area—reducing the scope of attack vectors, both by time and by privilege level. In this case, less is indeed more.

#### Secure Defaults

<a id="d24e23512"></a>
The default settings on your app, or for your users on your site, should
be the most secure values. These might not be the most user-friendly
or convenient values, but it's better to let each individual decide for
themselves the trade-offs between security and convenience.

<a id="d24e23526"></a>
For example, the default for password entry might be to hide the
password as entered, replacing each character with an asterisk. If
you're entering a password in a crowded public place, or projected
before a large audience, that's a sensible default. But some users might
want to see the password spelled out, perhaps for accessibility. If
there's little risk someone is looking over their shoulder, that's a
reasonable choice for them.

#### Encrypt Sensitive Data

<a id="d24e23540"></a>
Don't leave personally identifiable information, financial data, passwords, or other credentials in plain text, whether in a database or some other external file. If the data gets exposed, encryption offers an additional level of safety.

<a id="d24e23566"></a>
In Topic 19, Version Control we strongly recommend putting everything needed for the project under version control. Well, almost everything. Here's one major exception to that rule:

<a id="d24e23587"></a>
Don't check in secrets, API keys, SSH keys, encryption passwords or
other credentials alongside your source code in version control.

<a id="d24e23589"></a>
Keys and secrets need to be managed separately, generally via config files or environment variables as part of build and deployment.

<a id="passwords"></a>
<a id="d24e23598"></a>
<a id="d24e23620"></a>
<a id="FNPTR-65"></a>
<a id="d24e23638"></a>
<a id="d24e23641"></a>
<a id="d24e23644"></a>
<a id="d24e23659"></a>
<a id="d24e23667"></a>
<a id="d24e23679"></a>
<a id="d24e23682"></a>
<a id="d24e23684"></a>
Password Antipatterns

One of the fundamental problems with security is that oftentimes good security runs counter to common sense or common practice. For example, you might think that strict password requirements would increase security for your application or site. You'd be wrong.

Strict password policies will actually lower your security. Here's a short list of very bad ideas, along with some recommendations from the NIST:[65]

- Do not restrict password length to less than 64 characters. NIST recommends 256 as a good maximum length.
- Do not truncate the user's chosen password.
- Do not restrict special characters such as ``[]();&%$#`` or `/`. See the note about Bobby Tables earlier in this section. If special characters in your password will compromise your system, you have bigger problems. The NIST says to accept all printing ASCII characters, space, and Unicode.
- Do not provide password hints to unauthenticated users, or prompt for specific types of information (e.g., “what was the name of your first pet?”).
- Do not disable the paste function in the browser. Crippling the functionality of the browser and password managers does not make your system more secure, in fact it drives users to create simpler, shorter passwords that are much easier to compromise. Both the NIST in the US and the National Cyber Security Centre in the UK specifically require verifiers to allow paste functionality for this reason.
- Do not impose other composition rules. For example, do not mandate any particular mix of upper and lower case, numerics, or special characters, or prohibit repeating characters, and so on.
- Do not arbitrarily require users to change their passwords after some length of time. Only do this for a valid reason (e.g., if there has been a breach).

You want to encourage long, random passwords with a high degree of entropy. Putting artificial constraints limits entropy and encourages bad password habits, leaving your user's accounts vulnerable to takeover.

#### Maintain Security Updates

<a id="d24e23689"></a>
Updating computer systems can be a huge pain. You need that security patch, but as a side effect it breaks some portion of your application. You could decide to wait, and defer the update until later. That's a terrible idea, because now your system is vulnerable to a known exploit.

**Tip 73: Apply Security Patches Quickly**

<a id="d24e23701"></a>
This tip affects every net-connected device, including phones, cars, appliances, personal laptops, developer machines, build machines, production servers, and cloud images. Everything. And if you think that this doesn't really matter, just remember that the largest data breaches in history (so far) were caused by systems that were behind on their updates.

<a id="d24e23703"></a>
Don't let it happen to you.

### Common Sense vs. Crypto

<a id="d24e23710"></a>
<a id="FNPTR-66"></a>
It's important to keep in mind that common sense may fail you when it
comes to matters of cryptography. The first and most important rule when
it comes to crypto is never do it yourself.[66] Even for
something as simple as passwords, common practices are wrongheaded (see
the sidebar <a href="#passwords">Password Antipatterns</a>). Once you get into the world of
crypto, even the tiniest, most insignificant-looking error can
compromise everything: your clever new, home-made encryption algorithm
can probably be broken by an expert in minutes. You don't want to do
encryption yourself.

<a id="d24e23727"></a>
As we've said elsewhere, rely only on reliable things: well-vetted, thoroughly examined, well-maintained, frequently updated, preferably open source libraries and frameworks.

<a id="d24e23729"></a>
Beyond simple encryption tasks, take a hard look at other security-related features of your site or application. Take authentication, for instance.

<a id="d24e23743"></a>
In order to implement your own login with password or biometric
authentication, you need to understand how hashes and salts work, how
crackers use things like Rainbow tables, why you shouldn't use MD5 or
SHA1, and a host of other concerns. And even if you get all that right,
at the end of the day you're still responsible for holding onto the data
and keeping it secure, subject to whatever new legislation and legal
obligations come up.

<a id="d24e23745"></a>
Or, you could take the Pragmatic approach and let someone else
worry about it and use a third-party authentication provider. This may be an off-the-shelf service
you run in-house, or it could be a third party in the cloud.
Authentication services are often available from email, phone, or social
media providers, which may or may not be appropriate for your
application. In any case, these folks spend all their days keeping their
systems secure, and they're better at it than you are.

<a id="d24e23747"></a>
Stay safe out there.

### Related Sections Include

- Topic 23, Design by Contract
- Topic 24, Dead Programs Tell No Lies
- Topic 25, Assertive Programming
- Topic 38, Programming by Coincidence
- Topic 45, The Requirements Pit
