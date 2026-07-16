# ZhipuAI — model_api_example.py (excerpt)

import zhipuai

# your api key
zhipuai.api_key = ""


def invoke_example():
    response = zhipuai.model_api.invoke(
        model="chatglm_6b",
        prompt=[{"role": "user", "content": "人工智能"}],
        top_p=0.7,
        temperature=0.9,
    )
    print(response)

(Excerpted from zhipuai/zhipuai-sdk-python/examples/model_api_example.py)
