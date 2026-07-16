# prompts_zh.py (excerpt)

   - 如果文献中有对应记录，则为不同队列、性别、研究对象国家定义新分组。

# 输出格式
- 严格输出 JSON 格式, JSON中不得包含任何解释或附加说明；
- 所有结果采用确切的值回答，无法确定采用空字符串 `""` 替代。  
- JSON中禁止任何解释说明。
- 结构应完全符合下列示例：

```json
{
  "Group 1": {
    "CohortID": "Cohort 1",
    "Sex": "female",
    "CancerOutcome": "Lung Cancer",
    "ExposedGroup": {
      "Exp_Definition": "C1/2, HP感染，未治愈",
      "Exp_Cases": "120",
      "Exp_NonCases": "880"
    }
  }
}
```

(Excerpted from bytedance/CanRisk-AI/scripts/prompts_zh.py)
