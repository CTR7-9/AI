# Prompt schema examples (excerpt)

When asking for structured JSON output, include an explicit schema and example.

Example:
```
Schema:
{
  "name": "string",
  "age": "integer",
  "emails": ["string"]
}

Example Output:
{
  "name": "Alice",
  "age": 30,
  "emails": ["alice@example.com"]
}
```

(Collected from multiple prompt-engineering guides)