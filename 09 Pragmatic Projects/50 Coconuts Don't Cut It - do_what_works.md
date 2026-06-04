Source: https://panzhongxian.cn/en/the-pragmatic-programmer/9_pragmatic_projects.html#do_what_works

<a id="do_what_works"></a>
## Topic 50. Coconuts Don't Cut It

<a id="d24e26447"></a>
The native islanders had never seen an airplane before, or met people
such as these strangers. In return for use of their land, the strangers
provided mechanical birds that flew in and out all day long on a
“runway,” bringing incredible material wealth to their island home. The
strangers mentioned something about war and fighting. One day it was
over and they all left, taking their strange riches with them.

<a id="d24e26461"></a>
The islanders were desperate to restore their good fortunes, and
re-built a facsimile of the airport, control tower, and equipment using
local materials: vines, coconut shells, palm fronds, and such. But for
some reason, even though they had everything in place, the
planes didn't come. They had imitated the form, but not the content. Anthropologists call this a cargo cult.

<a id="d24e26466"></a>
All too often, we are the islanders.

<a id="d24e26471"></a>
<a id="FNPTR-79"></a>
It's easy and tempting to fall into the cargo cult trap: by investing in and building up the easily-visible artifacts, you hope to attract the underlying, working magic. But as with the original cargo cults of Melanesia,[[79]](<../10 Postface/README.md#FOOTNOTE-79>) a fake airport made out of coconut shells is no substitute for the real thing.

<a id="d24e26480"></a>
For example, we have personally seen teams that claim to be using Scrum.
But, upon closer examination, it turned out they were doing a daily
stand up meeting once a week, with four-week iterations that often
turned into six- or eight-week iterations. They felt that this was okay
because they were using a popular “agile” scheduling tool. They were
only investing in the superficial artifacts—and even then, often in name
only, as if “stand up” or “iteration” were some sort of incantation for
the superstitious. Unsurprisingly, they, too, failed to attract the real
magic.

### Context Matters

<a id="d24e26492"></a>
Have you or your team fallen in this trap? Ask yourself, why are you
even using that particular development method? Or that framework? Or
that testing technique? Is it actually well-suited for the job at hand?
Does it work well for you? Or was it adopted just because it was being
used by the latest internet-fueled success story?

<a id="d24e26498"></a>
There's a current trend to adopt the policies and processes of
successful companies such as Spotify, Netflix, Stripe, GitLab, and
others. Each have their own unique take on software development and
management. But consider the context: are you in the same market, with
the same constraints and opportunities, similar expertise and
organization size, similar management, and similar culture? Similar user
base and requirements?

<a id="d24e26500"></a>
Don't fall for it. Particular artifacts, superficial structures, policies, processes, and methods are not enough.

**Tip 87: Do What Works, Not What's Fashionable**

<a id="d24e26512"></a>
How do you know “what works”? You rely on that most fundamental of Pragmatic techniques:

<a id="d24e26514"></a>
Try it.

<a id="d24e26516"></a>
Pilot the idea with a small team or set of teams. Keep the good bits that seem to work well, and discard anything else as waste or overhead. No one will downgrade your organization because it operates differently from Spotify or Netflix, because even they didn't follow their current processes while they were growing. And years from now, as those companies mature and pivot and continue to thrive, they'll be doing something different yet again.

<a id="d24e26522"></a>
That's the actual secret to their success.

### One Size Fits No One Well

<a id="d24e26529"></a>
The purpose of a software development methodology is to help people work together. As we discuss in Topic 48, [*The Essence of Agility*](<../08 Before the Project/48 The Essence of Agility - essence_of_agility.md#essence_of_agility>), there is no single plan you can follow when you develop software, especially not a plan that someone else came up with at another company.

<a id="d24e26536"></a>
Many certification programs are actually even worse than that: they are predicated on the student being able to memorize and follow the rules. But that's not what you want. You need the ability to see beyond the existing rules and exploit possibilities for advantage. That's a very different mindset from “but Scrum/Lean/Kanban/XP/agile does it this way…” and so on.

<a id="d24e26540"></a>
Instead, you want to take the best pieces from any particular methodology and adapt them for use. No one size fits all, and current methods are far from complete, so you'll need to look at more than just one popular method.

<a id="d24e26542"></a>
For example, Scrum defines some project management practices, but Scrum by itself doesn't provide enough guidance at the technical level for teams or at the portfolio/governance level for leadership. So where do you start?

<a id="d24e26547"></a>
<a id="d24e26552"></a>
Be Like Them!

We frequently hear software development leaders tell their staff, “We should operate like Netflix” (or one of these other leading companies). Of course you could do that.

First, get yourself a few hundred thousand servers and tens of millions of users...

### The Real Goal

<a id="d24e26557"></a>
The goal of course isn't to “do Scrum,” “do agile,” “do Lean,” or what-have-you. The goal is to be in a position to deliver working software that gives the users some new capability at a moment's notice. Not weeks, months, or years from now, but now. For many teams and organizations, continuous delivery feels like a lofty, unattainable goal, especially if you're saddled with a process that restricts delivery to months, or even weeks. But as with any goal, the key is to keep aiming in the right direction.

<a id="d24e26574"></a>
<a id="adelivery_times"></a>
![A graph depicts the delivery time for three entities.](https://panzhongxian.cn/images/the-pragmatic-programmer/delivery_times.png)

A graph depicts the period-wise delivery time information. The horizontal axis shows the entities: multi-month or year iterations (waterfall), fixed short iterations (scrum), and continuous delivery. The vertical axis shows the entities: hours, weeks, and years. Nine blocks are shown in the graph. The first three horizontal blocks represent the entities for the delivery time (years). The fourth to sixth horizontal blocks represent the entities for the delivery time (weeks). The seventh to ninth horizontal blocks represent the entities for the delivery time (hours). A decreasing curve is drawn in the graph passing the blocks: First, fourth, and ninth.

<a id="d24e26575"></a>
If you're delivering in years, try and shorten the cycle to months. From months, cut it down to weeks. From a four-week sprint, try two. From a two week sprint, try one. Then daily. Then, finally, on demand. Note that being able to deliver on demand does not mean you are forced to deliver every minute of every day. You deliver when the users need it, when it makes business sense to do so.

**Tip 88: Deliver When Users Need It**

<a id="d24e26583"></a>
In order to move to this style of continuous development, you need a rock-solid infrastructure, which we discuss in the next topic, Topic 51, [*Pragmatic Starter Kit*](<51 Pragmatic Starter Kit - starter_kit.md#starter_kit>). You do development in the main trunk of your version control system, not in branches, and use techniques such as feature switches to roll out test features to users selectively.

<a id="d24e26592"></a>
Once your infrastructure is in order, you need to decide how to organize the work. Beginners might want to start with Scrum for project management, plus the technical practices from eXtreme Programming (XP). More disciplined and experienced teams might look to Kanban and Lean techniques, both for the team and perhaps for larger governance issues.

<a id="d24e26608"></a>
But don't take our word for it, investigate and try these approaches for yourself. Be careful, though, in overdoing it. Overly investing in any particular methodology can leave you blind to alternatives. You get used to it. Soon it becomes hard to see any other way. You've become calcified, and now you can't adapt quickly anymore.

<a id="d24e26610"></a>
Might as well be using coconuts.

### Related Sections Include

- Topic 12, [*Tracer Bullets*](<../02 Pragmatic Approach/12 Tracer Bullets - tracer_bullets.md#tracer_bullets>)
- Topic 27, [*Don't Outrun Your Headlights*](<../04 Pragmatic Paranoia/27 Don't Outrun Your Headlights - headlights.md#headlights>)
- Topic 48, [*The Essence of Agility*](<../08 Before the Project/48 The Essence of Agility - essence_of_agility.md#essence_of_agility>)
- Topic 49, [*Pragmatic Teams*](<49 Pragmatic Teams - teams.md#teams>)
- Topic 51, [*Pragmatic Starter Kit*](<51 Pragmatic Starter Kit - starter_kit.md#starter_kit>)
