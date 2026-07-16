# Off Topic Prompts (Excerpt)

Ensures content stays within defined business scope using LLM analysis. Flags content that goes off-topic or outside your scope to help maintain focus and prevent scope creep.

## Configuration

```json
{
    "name": "Off Topic Prompts",
    "config": {
        "model": "gpt-5",
        "confidence_threshold": 0.7,
        "system_prompt_details": "Customer support for our e-commerce platform. Topics include order status, returns, shipping, and product questions.",
        "max_turns": 10
    }
}
```

(Excerpted from openai/openai-guardrails-python/docs/ref/checks/off_topic_prompts.md)
