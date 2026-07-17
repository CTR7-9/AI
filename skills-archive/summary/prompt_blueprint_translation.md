# Prompt blueprint: translation-friendly template

Use a language-agnostic template and supply localized examples:

System: "You are a helpful assistant. Follow the schema and language instructions exactly."

Template:
```
Task: {task_description}
Language: {language}
Examples: {localized_examples}
Schema: {json_schema}
```

(Practical template for internationalized prompts)