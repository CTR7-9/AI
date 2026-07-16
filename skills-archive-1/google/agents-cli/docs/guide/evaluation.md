## The Eval-Fix Loop (agents-cli evaluation)

Evaluation is iterative. Expect 5-10+ cycles before your agent consistently passes.

1. Write 1-2 core eval cases covering the most important behavior.
2. Run: `agents-cli eval generate` followed by `agents-cli eval grade`
3. Read the results — which cases failed and why.
4. Fix — adjust the agent's instruction, tools, or logic.
5. Re-run: `agents-cli eval generate` and `agents-cli eval grade`
6. Expand — once core cases pass, add edge cases and new scenarios.

(Excerpted from google/agents-cli/docs/src/guide/evaluation.md)
