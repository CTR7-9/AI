# snippet: bytedance/CanRisk-AI/scripts/prompts_zh.py (excerpt)

```python
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
      },
      "NonExposedGroup": {
        "NEP_Definition": "当地一般人群",
        "NEP_Cases": "80.5",
        "NEP_NonCases": "919.5"
      },
      "RiskEstimates": {
        "Value 1": {
          "Type": "RR",
          "PointEstimate": "1.27",
          "95% CI": "1.10-1.51",
          "Variables": "age, gender, BMI"
        },...
      },
      "Note": ""
    },
  }
  ```

# 注意事项
- 严格按照以上指令执行，不得增添、遗漏或修改任何信息，需特殊说明的信息在"Note"中简述。
- 分析过程与最终输出必须严格分离，分别写在 `<think>` 与 `<answer>` 标签内。

请根据以上指令，从待分析的学术文献中提取关键信息，确保输出内容完全符合要求，以供癌症发病风险因素的Meta分析使用。''')
cancer_adj = Template('''# 输入:
<input>
{{content}}
</input>''')

prompts = {
    'grade_evaluator_sys': sys_prompt_grade_evaluator,
    'grade_evaluator': grade_evaluator,
    'theme_class_sys': sys_prompt_theme_class,
    'theme_class': theme_class,
    'table_prompts': table_prompts,
    'figure_prompts': figure_prompts,
    'common_input': common_input,
    'sys_prompt_outcomes': sys_prompt_outcomes,
    'sys_prompt_cancers': sys_prompt_cancers,
    'sys_prompt_risk_factor': sys_prompt_risk_factor,
    'sys_prompt_risk_factor_check': sys_prompt_risk_factor_check,
    'sys_prompt_effect_size': sys_prompt_effect_size,
    'risk_factors_check_input': risk_factors_check_input,
    'sys_prompt_cancer_adj': sys_prompt_cancer_adj,
    'sys_prompt_risk_factor_adj': sys_prompt_risk_factor_adj,
    'risk_factor_adj': risk_factor_adj,
    'sys_prompt_groupA': sys_prompt_groupA,
    'sys_prompt_groupB': sys_prompt_groupB,
    'group_info': group_info,

    'cancer_adj': cancer_adj,
}
```
```
