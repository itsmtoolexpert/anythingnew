# The Agent Control Plane

### MCP made agents interoperable. Now the fight is over who gets to say yes.

*Emerging Things · Rahul Adokar*

---

Picture a Tuesday night incident. An AI operations agent spots a memory leak, decides the fix is to restart a production database, and calls the tool to do it.

Nobody in your org chart approved that restart. So who did?

A year ago the honest answer was "whoever wrote the agent's permissions file." In the last two weeks, a much more interesting answer has started to form. Five vendors and one standards body each staked a claim on a different part of that decision. Put their announcements side by side and you can see the shape of something new: a **control plane for AI agents**.

This piece maps it, argues which layer will matter most, and ends with five questions to ask before you buy any of it.

---

## 1. The six checkpoints

Every action an enterprise agent takes now passes, at least on paper, through six checkpoints:

1. **The request.** The agent decides to act.
2. **Identity.** Who is this agent, and on whose behalf is it acting?
3. **Policy.** Is this action allowed, given what's being touched and how risky it is?
4. **Enforcement.** Something at runtime actually allows or blocks the call.
5. **Tools.** The action travels over a protocol to the target system.
6. **Production.** Something changes in the real world.

Running alongside all six is **observability**: the record of what the agent actually did.

*[Embed: dynamic diagram — chief-of-staff/visuals/2026-11-01-agent-control-plane.mp4]*

None of these layers is new on its own. What's new is that, in late October, each one got a named owner.

---

## 2. The plumbing went neutral

Start with step 5, because it explains everything else.

On October 22, the Agentic AI Foundation [announced four new projects](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox): Anthropic's **Agent Skills**, OpenAI's **Open Responses**, Hugging Face's **OpenEnv** and Alibaba's **OpenSandbox**. They joined MCP, A2A and AGENTS.md, which the foundation already hosted. That's ten projects under one vendor-neutral roof.

Read that list again. The way agents call tools (MCP), talk to each other (A2A), package instructions (Agent Skills) and talk to models (Open Responses) now belongs to a foundation, not to a vendor.

There's a fair caveat: governance on paper isn't the same as neutrality in practice, and some observers have pointed out that the named maintainers still come mostly from the companies that donated the projects. But the direction is clear.

And here's the consequence that matters for buyers: **when the plumbing is neutral, the plumbing stops being the moat.** No vendor can lock you in through the protocol your agents use. So the competition moves up the stack, to the layers that decide *what agents are allowed to do*.

You can already see vendors adapting. Digitate's [ignio Hummingbird release](https://www.tmcnet.com/usubmit/2026/10/28/10471511.htm) (Oct 28) ships built-in MCP and A2A servers so other agents, including ones in Teams, Claude and Gemini, can call its IT operations capabilities. Speaking the open protocols is becoming table stakes, not a differentiator.

---

## 3. The identity land grab

Step 2 is where the real fight is.

**ServiceNow** made its move on October 21 with [AI Passport, built with NVIDIA](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-delivers-industry-first-personal-enterprise-agent-and-policy-enforcement-with-NVIDIA-extending-AI-governance-across-software-and-silicon/default.aspx). Each agent gets a credential that carries business rules from ServiceNow's AI Control Tower, such as risk tolerance and which external services it may use. ServiceNow also added shadow-AI detection and AI cost management to the same governance layer.

**Microsoft** got there first on availability: [Agent 365 went generally available on May 1](https://www.computerworld.com/article/4167054/microsoft-google-push-ai-agent-governance-into-enterprise-it-mainstream.html), giving IT one console to discover, secure and manage agents across Microsoft, third-party SaaS and hybrid clouds.

**Google** has taken a narrower path so far, with an AI control center in Workspace focused on how AI interacts with collaboration data. (Commentary after Cloud Next 2026 also described agent identity and registry features; I'd treat those as directional until Google's own documentation catches up.)

Analysts quoted by Computerworld framed the difference neatly: Microsoft treats agents as enterprise actors that need broad oversight; Google focuses on AI's interaction with its own data. Their shared conclusion was the important part: **no single vendor's native console is likely to cover every agent in a multi-cloud, multi-SaaS enterprise.**

That gap is exactly where ServiceNow is aiming. And it has an advantage the other two don't: **the CMDB.**

An identity system knows *who* an agent is. A configuration management database knows *what everything is*: which server runs payments, which database is customer-facing, which change window is frozen. A policy built on that context can tell the difference between "restart a test box" and "restart the payments database." A policy built only on identity can't.

That's my core argument: **whoever issues the agent's identity decides what it can touch, and the issuer with the best map of the estate writes the best rules.**

---

## 4. Enforcement moves into the runtime

A policy is only a suggestion until something enforces it.

In the ServiceNow announcement, that something is **NVIDIA**, which ServiceNow names as a design and launch partner: policy written in ServiceNow is carried by the AI Passport and enforced by NVIDIA's runtime layers, which approve or block the agent's actions. It extends work announced in May, when ServiceNow paired its Project Arc desktop agent with NVIDIA's runtime security.

This split matters architecturally. It separates the **decision** (policy, owned by whoever holds the identity) from the **execution** (enforcement, close to the compute). That's the same pattern we already trust for network security, where policy is defined centrally and enforced at the edge. Expect it to become the default design for agents too.

---

## 5. Flight recorder or air traffic control?

Which leaves observability, the layer that runs alongside all six checkpoints.

The observability vendors moved fast in late October:

- **Dynatrace** [unified its AI observability ingest](https://dynatrace.com/news/blog/dynatrace-unifies-ai-observability-ingest-across-coding-agents-oneagent-and-openinference) (Oct 30) across coding agents, Python LLM apps and OpenInference-instrumented frameworks, added tracing for Claude Managed Agents, and is ending support for OpenLLMetry.
- **New Relic** [brought change tracking into GitHub Copilot](https://itwire.com/business-it-news/business-intelligence/new-relic-change-tracking-brings-headless-intelligent-observability-directly-into-github-copilot-empowering-developers-to-ship-code-with-confidence) (public preview) and made its Autopilot for the GitHub MCP Server generally available.
- **Datadog** [built Scout](https://infoq.com/news/2026/10/datadog-scout-sre-model), a specialist model for SRE investigations, now in closed preview. Datadog says it matched a larger general model at a quarter of the cost, by Datadog's own benchmarks.

The demand is real. Splunk's [State of Observability 2026](https://tahawultech.com/industry/technology/splunk-state-of-observability-2026-report-avoiding-the-hidden-costs-of-ai-agents) found **83%** of respondents worried about unintended consequences from AI agents.

But look at where these products sit in the diagram. They record what the agent *did*. That's the flight recorder: essential after a crash, but it doesn't decide who takes off.

Observability vendors have a strategic choice to make. They can stay the flight recorder, or they can feed what they see back into policy, so an agent that behaved strangely yesterday gets a narrower passport today. That feedback loop is the orange arrow in the diagram, and right now nobody clearly owns it. **It's the most interesting open position in the whole stack.**

---

## 6. The strongest counterargument

Here's how my thesis could be wrong: **bundling.**

Microsoft folds Agent 365 into its E7 licensing tier. Most enterprises already run on Microsoft identity. A good-enough governance layer that's already paid for often beats a better architecture that needs a new purchase order.

If that happens, the identity layer goes to whoever already owns employee identity, and the CMDB advantage I described matters less than the procurement path. I still think the context argument wins for high-risk actions in production. But if you're betting on this market, bet with that risk in mind.

---

## 7. What to do in Q1: five questions to ask before buying

The data says most organizations aren't ready. An [OutSystems survey](https://securitybrief.asia/story/outsystems-survey-finds-ai-governance-gap-in-firms) (Oct 28) found a gap between how confident companies feel about governing agents and how ready they actually are, with many still relying on governance structures built before agents existed.

Before you pick a platform, get clear answers to these:

1. **Who issues identity to our agents today?** IAM, ITSM, the agent framework, or nobody? If the answer is "nobody," that's your first project.
2. **Can our policy see business context?** Does it know which systems are critical, or only who the agent is?
3. **Where is policy enforced?** In the runtime, close to the action, or only in a dashboard after the fact?
4. **Does observability feed back into policy?** Or does it only produce reports?
5. **What happens to agents outside our main vendor's ecosystem?** If your governance console only sees one cloud, the agents you can't see are the ones that will cause the incident.

---

## The bottom line

The protocols went neutral in October. That didn't end the platform war; it moved it.

The next fight is over the agent's passport: who issues it, what context it carries, and who gets to revoke it. **Whoever owns the agent's identity owns the agent.**

I'll keep tracking this layer by layer. If you run IT operations, ITSM or enterprise architecture, subscribe to get the next map when it changes.

*What did I miss? If your organization already issues identity to its agents, reply and tell me how. I read every response.*
