# Research Memory — Emerging Things

_Last updated: Wed 2026-11-04 (evening run)._

## Narrative Tracker

### Theme 1: The agent governance stack is forming
- **Thesis:** Control over what IT agents may do is being split across ITSM (policy), observability (tracing) and silicon/runtime (enforcement). Whoever owns the policy layer owns the agent.
- **Status:** 📈 Substack-ready (8 data points)
- **Data points:**
  - 2026-10-21: ServiceNow AI Passport with NVIDIA, policy from AI Control Tower enforced at runtime. https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-delivers-industry-first-personal-enterprise-agent-and-policy-enforcement-with-NVIDIA-extending-AI-governance-across-software-and-silicon/default.aspx
  - 2026-10-28: Digitate ignio Hummingbird, built-in MCP and A2A servers for IT ops agents. https://www.tmcnet.com/usubmit/2026/10/28/10471511.htm
  - 2026-10-30: Dynatrace unifies AI observability ingest for coding agents, Claude Managed Agents, OpenInference; drops OpenLLMetry. https://dynatrace.com/news/blog/dynatrace-unifies-ai-observability-ingest-across-coding-agents-oneagent-and-openinference
  - 2026-10-22: Agentic AI Foundation takes Anthropic Agent Skills, OpenAI Open Responses, OpenEnv, OpenSandbox; joins MCP, A2A, AGENTS.md under vendor-neutral governance. https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox
  - 2026-10-28: OutSystems survey: gap between confidence in governing agents and operational readiness (via SecurityBrief). https://securitybrief.asia/story/outsystems-survey-finds-ai-governance-gap-in-firms
  - 2026-11-03: CrowdStrike to acquire Fiddler AI (agent observability: tracing reasoning/tool calls, drift) and Dreadnode; WSJ-reported ~$495M combined, terms not disclosed by CrowdStrike. https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-fiddler-to-deliver-agent-observability/ ; https://techcrunch.com/2026/11/03/crowdstrike-to-shell-out-nearly-500m-for-2-ai-security-startups-as-the-market-for-securing-agents-takes-off
  - 2026-11 (CrowdStrike Fal.Con Europe): AI Kill Switch to terminate rogue agents and cut network access. https://cryptobriefing.com/crowdstrike-unveils-ai-kill-switch-to-rein-in-rogue-agents (aggregator-grade, unverified date)
  - Context (2026-05-05): Microsoft Agent 365 GA (May 1) and Google AI control center; analysts say single-vendor consoles won't cover multi-cloud agents. https://www.computerworld.com/article/4167054/microsoft-google-push-ai-agent-governance-into-enterprise-it-mainstream.html
  - Supporting stat (date ~2026-10-27): Splunk State of Observability 2026, 83% concerned about unintended consequences of AI agents. https://tahawultech.com/industry/technology/splunk-state-of-observability-2026-report-avoiding-the-hidden-costs-of-ai-agents

### Theme 2: In AIOps, the model is a commodity and telemetry is the moat
- **Thesis:** Observability vendors are shipping small in-house models; advantage comes from proprietary telemetry, not model quality.
- **Status:** building (2 data points)
- **Data points:**
  - 2026-11-04: Dynatrace Q2 FY27 call: 1,100+ customers in agents public preview (up from 800), monetizing agents from Q3 (per Benzinga transcript; page not fetchable, snippet only). https://www.benzinga.com/news/26/11/62820620/dynatrace-q2-2027-earnings-call-transcript
  - ~2026-10-29: Datadog Scout specialist SRE model, closed preview; vendor claims parity with a larger Claude model at 1/4 cost (Datadog's own benchmark). https://infoq.com/news/2026/10/datadog-scout-sre-model

### Theme 3: Observability is moving into the coding agent
- **Thesis:** Change risk is now assessed inside the coding agent before deploy, which collides with ITSM change management.
- **Status:** building (1 data point)
- **Data points:**
  - 2026-10-30: New Relic Change Tracking for GitHub Copilot (public preview); Autopilot for GitHub MCP Server GA. https://itwire.com/business-it-news/business-intelligence/new-relic-change-tracking-brings-headless-intelligent-observability-directly-into-github-copilot-empowering-developers-to-ship-code-with-confidence

## Content Backlog
- 2026-11-01: LinkedIn — "The AIOps moat is telemetry, not the model" (Theme 2, Galloway-style contrarian). Status: suggested.
- 2026-11-01: Substack — "The Agent Control Plane" (Theme 1). Status: drafted (chief-of-staff/drafts/2026-11-substack-the-agent-control-plane.md), not yet published.
- 2026-11-01: LinkedIn — "Who approves your AI agent?" (Theme 1) with dynamic diagram chief-of-staff/visuals/2026-11-01-agent-control-plane.mp4. Status: drafted (chief-of-staff/drafts/2026-11-02-linkedin-who-approves-your-ai-agent.md), not yet published.
- 2026-11-01: One-page — "Agent Control Plane Scorecard" grid (vendors x layers). Status: suggested.
- 2026-11-01: Visual — one-page map of where observability vendors plug into the AI agent lifecycle (Bhatia-style). Status: suggested.

- 2026-11-04: LinkedIn — "Security vendors are buying the agent trace" (Theme 1, Galloway-style contrarian) with diagram chief-of-staff/visuals/2026-11-04-who-owns-the-trace.mp4. Status: suggested.
- 2026-11-04: One-page — "Who owns each layer of the agent control loop" grid. Status: suggested.

## Content Log
- (nothing recorded yet — tell me what you publish)

## Stories Covered
- 2026-11-01: Dynatrace AI observability ingest; Datadog Scout; New Relic + Copilot change tracking; AI-training opt-out token (unverified, aggregator); ServiceNow AI Passport; Digitate ignio Hummingbird.
- 2026-11-01 (run 2): Agentic AI Foundation new projects (Oct 22); OutSystems governance-gap survey (Oct 28); Microsoft/Google agent governance (context, May).

- 2026-11-04: CrowdStrike–Fiddler/Dreadnode (Nov 3); Dynatrace Q2 FY27 call (Nov 4); Dynatrace agents integrations (TechTarget, earlier, context).

## Patterns
- 2026-11-01: Weekend runs have little fresh news; Sunday is best used to deepen a theme rather than scan.
- 2026-11-01: Frontier-AI news searches return many aggregator/newsletter pages with conflicting dates. Prefer company blogs and named trade press.
- 2026-11-04: Web search returns mostly stale results; adding explicit date strings (e.g. "November 3, 2026") surfaced fresh stories. WebFetch hosts (techcrunch, benzinga, techtarget) are blocked in this environment: snippets only. Substack 'Agent Control Plane' and LinkedIn drafts still unpublished 3 days on (pattern: drafts pile up, nothing logged as published).
