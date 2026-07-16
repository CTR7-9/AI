# Roadtrip Planner Skill (excerpt)

Both return JSON. A 403 here is a key problem, not a cookbook problem.

## 2. Provision

```bash
npm install
npm run setup
```

Creates the environment (networking limited to `developer.nps.gov` and `api.windy.com`), the reviewer agent (Opus, review-only prompt), the planner agent (bash on, `web_search`/`web_fetch` off, a `multiagent` coordinator roster naming the reviewer), the vault, and two `environment_variable` credentials with the `injection_location` each vendor documents hardcoded (NPS: header, Windy: body). Writes six `ROADTRIP_PLANNER_*` ids into `.env.local`. Re-running is a no-op while the agent exists (it does demand `--force` if the stored planner predates the reviewer roster), and `--force` provisions a fresh copy.

## 3. Run

```bash
npm run dev
```

Open <http://localhost:3000>. The page creates one session per browser on load (cookie `roadtrip_planner_session_id`), so the sandbox is warm before the first question. Then do the four beats in [README.md](./README.md#four-things-to-do-with-it), in order. Beat 2 is the vault story and it only lands after a real conversation exists. Beat 3 is the `agent_with_overrides` model picker. Beat 4 is the multi-agent review: it needs a full itinerary ask, not a one-fact question.

(Excerpted from anthropics/claude-cookbooks/managed_agents/roadtrip_planner/skill.md)
