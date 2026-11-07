# LinkedIn draft — Mon 2026-11-02
Attach: chief-of-staff/visuals/2026-11-01-agent-control-plane.mp4

---

Your AI agent just asked to restart a production database.

Who said yes?

In the last two weeks, the answer started to take shape. There are now six checkpoints, and a different company wants to own each one:

1 → The agent asks
2 → Identity: who is this agent? (ServiceNow AI Passport, Microsoft Agent 365)
3 → Policy: is it allowed?
4 → Enforcement: NVIDIA's runtime allows or blocks
5 → Tools: MCP, A2A, Agent Skills
6 → Production

Here's what most people missed.

On Oct 22, MCP, A2A and Agent Skills all ended up under one neutral body: the Agentic AI Foundation.

When the plumbing is neutral, the plumbing stops being the moat.

The moat moves to step 2.

Whoever issues the agent's identity decides what it can touch. Everyone else either enforces that decision or records it.

That's why ServiceNow's AI Passport matters. It ties each agent's credential to live configuration data and policy. A policy built on the CMDB knows the difference between "restart a test box" and "restart the payments database."

Observability vendors now have a choice: become air traffic control, or stay the flight recorder.

Whoever owns the agent's identity owns the agent.

Who issues identity to the AI agents in your environment today: IAM, ITSM, or nobody?

#AIAgents #ITSM #Observability

---

Sources (for you, not the post):
- ServiceNow AI Passport with NVIDIA, Oct 21: https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-delivers-industry-first-personal-enterprise-agent-and-policy-enforcement-with-NVIDIA-extending-AI-governance-across-software-and-silicon/default.aspx
- Agentic AI Foundation new projects, Oct 22: https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox
- Microsoft Agent 365 GA, May: https://www.computerworld.com/article/4167054/microsoft-google-push-ai-agent-governance-into-enterprise-it-mainstream.html
