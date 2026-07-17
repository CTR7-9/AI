# Multi-agent retry strategy (excerpt)

- On transient failures, retry subagents with exponential backoff and jitter.
- Ensure idempotency by including request IDs and sequence numbers in subagent payloads.

(Excerpted from multi-agent resilience guides)