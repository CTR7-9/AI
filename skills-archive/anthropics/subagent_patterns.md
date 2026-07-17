# Subagent communication patterns (excerpt)

- Use typed channels (researcher_output, verifier_output) with strict schemas.
- Prefer idempotent messages and include sequence numbers to tolerate retries.
- Record each subagent's runtime metadata (duration, model version, tool calls) for debugging.

(Excerpted from multi-agent architecture notes)