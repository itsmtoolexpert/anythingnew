# Research Memory — Emerging Things

_Last updated: Tue 2026-11-10 (evening run, MT)._

## Narrative Tracker

### Theme 1: The agent governance stack is forming
- **Thesis:** Control over what IT agents may do is being split across ITSM (policy), observability (tracing) and silicon/runtime (enforcement). Whoever owns the policy layer owns the agent.
- **Status:** 📈 Substack-ready (17 data points; Theme 4 challenges the single-owner framing)
- **Data points:**
  - 2026-10-21: ServiceNow AI Passport with NVIDIA, policy from AI Control Tower enforced at runtime. https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-delivers-industry-first-personal-enterprise-agent-and-policy-enforcement-with-NVIDIA-extending-AI-governance-across-software-and-silicon/default.aspx
  - 2026-10-28: Digitate ignio Hummingbird, built-in MCP and A2A servers for IT ops agents. https://www.tmcnet.com/usubmit/2026/10/28/10471511.htm
  - 2026-10-30: Dynatrace unifies AI observability ingest for coding agents, Claude Managed Agents, OpenInference; drops OpenLLMetry. https://dynatrace.com/news/blog/dynatrace-unifies-ai-observability-ingest-across-coding-agents-oneagent-and-openinference
  - 2026-10-22: Agentic AI Foundation takes Anthropic Agent Skills, OpenAI Open Responses, OpenEnv, OpenSandbox; joins MCP, A2A, AGENTS.md under vendor-neutral governance. https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox
  - 2026-10-28: OutSystems survey: gap between confidence in governing agents and operational readiness (via SecurityBrief). https://securitybrief.asia/story/outsystems-survey-finds-ai-governance-gap-in-firms
  - 2026-11-03: CrowdStrike to acquire Fiddler AI (agent observability: tracing reasoning/tool calls, drift) and Dreadnode; WSJ-reported ~$495M combined, terms not disclosed by CrowdStrike. https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-fiddler-to-deliver-agent-observability/ ; https://techcrunch.com/2026/11/03/crowdstrike-to-shell-out-nearly-500m-for-2-ai-security-startups-as-the-market-for-securing-agents-takes-off
  - 2026-11 (CrowdStrike Fal.Con Europe): AI Kill Switch to terminate rogue agents and cut network access. https://cryptobriefing.com/crowdstrike-unveils-ai-kill-switch-to-rein-in-rogue-agents (aggregator-grade, unverified date)
  - 2026-11 (NIST blog, ~Nov 4 per aggregator ID Tech Digest, date unverified): NIST proposes 10 design tenets for AI agent identity management (agents as distinct identity principals). https://nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems
  - 2026-11-04: CrowdStrike AI Kill Switch in Falcon Guardian (second source via aggregator search; still not primary-confirmed).
  - 2026-10-01 (closed; announced Aug): Dynatrace completes $915M Arize acquisition (tracing + evals for AI agents, Phoenix stays open source). https://thenewstack.io/dynatrace-arize-agents-observability/
  - 2026-11-03: Traversal (AI SRE, autonomous incident remediation) raises $120M Series B at $1B valuation (Kleiner Perkins, Redpoint, Khosla); Resolve AI had $1B mark in Feb. https://www.goodwinlaw.com/en/news-and-events/news/2026/11/announcements-technology-goodwin-advises-traversal-120-million-series-b (law-firm release; aggregator-covered)
  - 2026-04 (context): Cisco announces intent to acquire Galileo (AI agent observability); Futurum frames it as pressure on Datadog/Dynatrace. https://futurumgroup.com/insights/cisco-to-acquire-galileo-ai-agent-observability-cant-run-at-human-speed/
  - 2026-09-15 (context): Cisco Splunk Agent Observability + Tokenomics (token spend per agent/coding agent). https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m09/cisco-delivers-trusted-ai-at-scale-through-new-splunk-advancements.html
  - 2025-11 (context, date approximate): Palo Alto Networks to acquire Chronosphere, $3.35B. https://msp-channel.com/news/71188/palo-alto-networks-acquires-chronosphere-to-boost-ai-observability-and-security
  - 2026-10-20 (context): Grafana Agent Observability (OTel) GA + Assistant Watchers. https://grafana.com/press/2026/10/20/observabilitycon-2026-ai-updates/
  - Context (2026-05-05): Microsoft Agent 365 GA (May 1) and Google AI control center; analysts say single-vendor consoles won't cover multi-cloud agents. https://www.computerworld.com/article/4167054/microsoft-google-push-ai-agent-governance-into-enterprise-it-mainstream.html
  - 2026-11-03: Snowflake Expedition 2026: Cortex AI Gateway, agent tool calls authenticated with end-user identity and checked against policy before they run; agent abuse detection on full trajectories. https://www.snowflake.com/en/news/press-releases/expedition-2026-business-ontology-ai-gateway/ (page not fetchable; search snippets + blog https://snowflake.com/en/blog/ai-agents-governance-ai-security-cost-control)
  - 2026-11-09/10 (KubeCon NA, Salt Lake City): Mirantis Agent Platform GA (spend caps; one-click cut network access for all agents); Teleport Beams GA (zero standing privileges, human or LLM judge reviews access); Solo.io enterprise Agent Substrate + kagent GA. Source: Cloud Native Now KubeCon coverage (snippets only; not primary-confirmed). https://cloudnativenow.com/kubecon-cloudnativecon-north-america-2026/mirantis-launches-agent-platform-for-governed-ai-agents-on-kubernetes/
  - 2026-11-10: IBM + Microsoft Imagine Enterprise: platform to build, run and govern industry-specific agents on Foundry/Copilot Studio with Entra, Purview, Defender. https://news.microsoft.com/source/2026/11/10/ibm-and-microsoft-announce-a-new-ai-agent-platform-designed-for-industry-specific-transformation/
  - Supporting stat (date ~2026-10-27): Splunk State of Observability 2026, 83% concerned about unintended consequences of AI agents. https://tahawultech.com/industry/technology/splunk-state-of-observability-2026-report-avoiding-the-hidden-costs-of-ai-agents

### Theme 2: In AIOps, the model is a commodity and telemetry is the moat
- **Thesis:** Observability vendors are shipping small in-house models; advantage comes from proprietary telemetry, not model quality.
- **Status:** 📈 Substack-ready (5 data points; New Relic Autopilot K8s agent added 2026-11-10)
- **Data points:**
  - 2026-11-04: Dynatrace Q2 FY27 call: 1,100+ customers in agents public preview (up from 800), monetizing agents from Q3 (per Benzinga transcript; page not fetchable, snippet only). https://www.benzinga.com/news/26/11/62820620/dynatrace-q2-2027-earnings-call-transcript
  - 2026-11-04: Datadog Q3: revenue $1.20B, +35% YoY; Q4 guide $1.19-1.20B; Q2 10-Q flagged lower usage from largest customer from Q3. Scout 1.0 / Bits Investigation claim NOT confirmed. https://www.sec.gov/Archives/edgar/data/0001561550/000162828026069792/ex-991x20260930x8k.htm
  - 2026-11-10: New Relic Autopilot Kubernetes Agent (public preview, KubeCon), built on its Ground Truth context engine over correlated OTel data; pinpoints root cause, generates fix code for engineers to review. https://www.financialcontent.com/article/bizwire-2026-11-10-new-relic-launches-new-relic-autopilot-kubernetes-agent-to-close-the-expertise-gap-and-protect-business-uptime ; https://cloudnativenow.com/kubecon-cloudnativecon-north-america-2026/new-relic-launches-autopilot-kubernetes-agent-for-ai-driven-cluster-troubleshooting/
  - ~2026-10-29: Datadog Scout specialist SRE model, closed preview; vendor claims parity with a larger Claude model at 1/4 cost (Datadog's own benchmark). https://infoq.com/news/2026/10/datadog-scout-sre-model

### Theme 3: Observability is moving into the coding agent
- **Thesis:** Change risk is now assessed inside the coding agent before deploy, which collides with ITSM change management.
- **Status:** building (1 data point)
- **Data points:**
  - 2026-10-30: New Relic Change Tracking for GitHub Copilot (public preview); Autopilot for GitHub MCP Server GA. https://itwire.com/business-it-news/business-intelligence/new-relic-change-tracking-brings-headless-intelligent-observability-directly-into-github-copilot-empowering-developers-to-ship-code-with-confidence

### Theme 4: Every layer ships its own agent controls (no single control plane)
- **Thesis:** Agent controls are fragmenting by layer (app/identity, data, runtime, observability). No one owns the whole loop, so the scarce asset is a cross-layer agent system of record; ITSM/CMDB is the natural home if it moves fast. Counter: Microsoft-style consolidation may make one stack's console the de facto record.
- **Status:** building (4 data points, all 2026-11-03 to 11-10; see Theme 1 entries for Snowflake, KubeCon runtime vendors, IBM+Microsoft, plus New Relic in Theme 2)
- **Data points:** Snowflake Cortex AI Gateway (11-03); Mirantis/Teleport/Solo.io at KubeCon (11-09/10, trade-press only); IBM+Microsoft Imagine Enterprise (11-10); New Relic Autopilot K8s agent (11-10). Context: CrowdStrike kill switch (11-04), ServiceNow AI Control Tower.

## Content Backlog
- 2026-11-01: LinkedIn — "The AIOps moat is telemetry, not the model" (Theme 2, Galloway-style contrarian). Status: suggested.
- 2026-11-01: Substack — "The Agent Control Plane" (Theme 1). Status: drafted (chief-of-staff/drafts/2026-11-substack-the-agent-control-plane.md), not yet published.
- 2026-11-01: LinkedIn — "Who approves your AI agent?" (Theme 1) with dynamic diagram chief-of-staff/visuals/2026-11-01-agent-control-plane.mp4. Status: drafted (chief-of-staff/drafts/2026-11-02-linkedin-who-approves-your-ai-agent.md), not yet published.
- 2026-11-01: One-page — "Agent Control Plane Scorecard" grid (vendors x layers: identity, policy, trace, enforcement/kill, standards). Status: suggested. (Merged with the 2026-11-04 "Who owns each layer of the agent control loop" grid, same idea.)
- 2026-11-01: Visual — one-page map of where observability vendors plug into the AI agent lifecycle (Bhatia-style). Status: suggested.


- 2026-11-05: LinkedIn — "Four layers, one loop: identity, policy, trace, kill" (Theme 1, Bhatia-style one-page visual) with diagram chief-of-staff/visuals/2026-11-05-identity-policy-trace-kill.mp4. Status: suggested.

- 2026-11-04 (merged 11-06): LinkedIn — "Security vendors are buying the agent trace" / "Three buyers, one asset" (Theme 1, Galloway-style contrarian, timeline) with diagram chief-of-staff/visuals/2026-11-06-agent-trace-buyers.mp4. Status: suggested.

- 2026-11-10: LinkedIn — "Every layer now ships its own agent controls. Who keeps the record?" (Theme 4, Bhatia-style stack visual + Galloway-style closing take) with diagram chief-of-staff/visuals/2026-11-10-every-layer-agent-controls.mp4. Status: suggested.
- 2026-11-10: Substack — "The Agent System of Record" (Theme 4 + Theme 1; why ITSM/CMDB, not another console, should hold agent decisions). Status: suggested; needs 2 more data points (an ITSM vendor ingesting agent actions from other layers; a buyer survey on agent inventory).

## Visuals
- 2026-11-01 · agent-control-plane · Theme 1 · 6-step flow: request, identity, policy, enforcement, tools, production + observability feedback loop · updated 2026-11-01 · used by: LinkedIn "Who approves your AI agent?" (drafted), Substack "The Agent Control Plane" (drafted).
- 2026-11-05 · identity-policy-trace-kill · Theme 1 · 4-step loop: identity, policy, trace, kill · updated 2026-11-05 · used by: LinkedIn "Four layers, one loop". Supersedes 2026-11-04 who-owns-the-trace (same loop, fewer layers; deleted 2026-11-06 during dedup).
- 2026-11-06 · agent-trace-buyers · Theme 1 · acquisition timeline (4 rows): Palo Alto–Chronosphere, Cisco–Galileo, Dynatrace–Arize, CrowdStrike–Fiddler · updated 2026-11-09 · used by: LinkedIn "Security vendors are buying the agent trace".
- 2026-11-10 · every-layer-agent-controls · Theme 4 · 4-layer stack (app+identity, data, runtime, observability) each with its own control toggle, feeding an empty "agent system of record" column · updated 2026-11-10 · used by: LinkedIn "Every layer now ships its own agent controls".
- Note: files dated 2026-11-04/05/06 were named with the UTC date; the runs happened on 11-03/04/05 Mountain Time. New files use the Mountain Time date.

## Content Log
- (nothing recorded yet — tell me what you publish)

## Stories Covered
- 2026-11-01: Dynatrace AI observability ingest; Datadog Scout; New Relic + Copilot change tracking; AI-training opt-out token (unverified, aggregator); ServiceNow AI Passport; Digitate ignio Hummingbird.
- 2026-11-01 (run 2): Agentic AI Foundation new projects (Oct 22); OutSystems governance-gap survey (Oct 28); Microsoft/Google agent governance (context, May).

- 2026-11-04: CrowdStrike–Fiddler/Dreadnode (Nov 3); Dynatrace Q2 FY27 call (Nov 4); Dynatrace agents integrations (TechTarget, earlier, context).

- 2026-11-05: NIST agent identity tenets; Datadog Q3 (Nov 4); CrowdStrike kill switch (repeat, new corroboration); Rapid7 Q3, Meta-Conductor (aggregator only, not featured).

- 2026-11-06: Thin day, no verified stories dated Nov 4-6 beyond already covered. Re-surfaced Cisco-Galileo, Grafana GA, Palo Alto-Chronosphere as context only.

- 2026-11-06 (run 2): Quiet day, no verified Tier 1/2 stories dated Nov 4-6 beyond those covered. Context only: Splunk State of Observability (Oct 20, Cisco newsroom https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m10/splunk-state-of-observability-2026-avoiding-the-hidden-costs-of-ai-agents.html), Ardoq MCP GA / SAP LeanIX MCP server (undated vendor pages). Frontier AI: nothing verified.

- 2026-11-09: Run covered Fri evening to Mon. Quiet again. Added to Signal Scan: Dynatrace–Arize (closed Oct 1), Traversal $120M (Nov 3), Copado–Valo.ai (Nov 4, minor, not featured). Frontier AI: nothing verified. Search tools returned undated/stale results; ITSM, EA, cloud/data searches found nothing new.

- 2026-11-10: KubeCon NA (Nov 9-12): Mirantis Agent Platform GA, Teleport Beams GA, Solo.io Agent Substrate/kagent GA, New Relic Autopilot K8s agent (Nov 10); IBM+Microsoft Imagine Enterprise (Nov 10); Snowflake Expedition Cortex AI Gateway (Nov 3, still-worth-tracking). Not featured: ServiceNow AIOps AI Specialist GA (store listing only, undated); Google Agentic Data Cloud update (Nov 4, CIO Dive); ControlTheory Dstl8 2.0.

## Patterns
- 2026-11-01: Weekend runs have little fresh news; Sunday is best used to deepen a theme rather than scan.
- 2026-11-01: Frontier-AI news searches return many aggregator/newsletter pages with conflicting dates. Prefer company blogs and named trade press.
- 2026-11-04: Web search returns mostly stale results; adding explicit date strings (e.g. "November 3, 2026") surfaced fresh stories. WebFetch hosts (techcrunch, benzinga, techtarget) are blocked in this environment: snippets only. Substack 'Agent Control Plane' and LinkedIn drafts still unpublished 3 days on (pattern: drafts pile up, nothing logged as published).
- 2026-11-05: Thin news day; vendor-specific searches returned nothing dated Nov 4-5 for ITSM/EA. WebFetch blocked for investors.datadoghq.com and aiagentsdirectory.com. Drafts still unpublished 4 days; Content Log empty.
- 2026-11-06 (dedup): Three quiet days in a row produced three near-identical Theme 1 diagrams (11-04 and 11-05 were the same loop). Rule added: update or reuse an existing diagram instead of drawing a new one for the same theme and structure.
- 2026-11-06: Quiet day again (3rd in a row). WebFetch blocked for itpro.com. Drafts unpublished 5 days; Content Log empty. LinkedIn gap flagged.
- 2026-11-06 (run 2): 4th quiet day in a row; date-string searches returned no Nov 5-6 items. Diagram reused (agent-trace-buyers), no new visual. Drafts unpublished 5 days; Content Log empty; LinkedIn gap persists. Theme 3 has had no new evidence since Oct 30 (fading flag at Nov 13).
- 2026-11-09: 5th quiet run; no Monday-dated verified stories found. Diagram updated in place (Arize row added). Drafts unpublished 8 days; Content Log empty; LinkedIn gap persists. Theme 3 still no new evidence since Oct 30 (fading flag Nov 13).
- 2026-11-10: First non-quiet run in a week, thanks to KubeCon NA. Conference weeks are the reliable source of fresh Tier 1 news; plan around KubeCon (Nov 9-12), Microsoft Ignite and AWS re:Invent. WebFetch blocked this run for snowflake.com, servicenow.com, cloudnativenow.com, techtimes.com: snippets only. Drafts unpublished 9 days; Content Log empty for 3rd week running (pattern now 3+ weeks: flagged once in Headline). Theme 3 still no evidence since Oct 30 (fading Nov 13).
