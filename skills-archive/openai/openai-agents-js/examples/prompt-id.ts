// Example: using a prompt ID stored in the OpenAI platform

const DEFAULT_PROMPT_ID =
  'pmpt_6965a984c7ac8194a8f4e79b00f838840118c1e58beb3332';

async function runDynamic(promptId: string) {
  const poemStyle = pickPoemStyle();
  const agent = new Agent({
    name: 'Assistant',
    prompt: {
      promptId,
      version: '1',
      variables: { poem_style: poemStyle },
    },
  });

  const result = await run(agent, 'Tell me about recursion in programming.');
  console.log(result.finalOutput);
}

(Excerpted from openai/openai-agents-js/examples/basic/prompt-id.ts)
