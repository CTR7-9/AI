# ZhipuAI — SDK usage examples (excerpt)

Example: constructing a chat prompt with system + user messages.

```
messages = [
  {"role":"system","content":"You are a helpful assistant."},
  {"role":"user","content":"Summarize the following text..."}
]
response = zhipuai.model_api.invoke(model="chatglm_6b", prompt=messages)
```

(Excerpted from zhipuai/sdk/examples)