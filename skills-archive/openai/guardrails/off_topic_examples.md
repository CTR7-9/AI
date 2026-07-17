# Guardrails checks — off-topic examples (excerpt)

This file contains examples of off-topic checks used to detect when user requests fall outside a supported domain. Use confidence thresholds and fail-open policies carefully.

Example check:
- name: "off_topic_customer_support"
  description: "Flag inputs unrelated to customer support for the e-commerce product."
  rules:
    - pattern: "refund|order status|shipping|return"
      action: "allow"
    - otherwise:
      action: "flag"

(Excerpted from openai/openai-guardrails examples)