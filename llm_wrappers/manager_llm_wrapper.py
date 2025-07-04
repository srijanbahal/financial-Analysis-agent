from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage
from utils.token_utils import count_tokens, trim_text_to_token_limit
from typing import Any

class ManagerLLMWrapper(BaseChatModel):
    base_llm: Any
    max_tokens: int = 80000
    model_name: str = "generic"

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        # Flatten all messages into one string
        prompt = "\n".join([msg.content for msg in messages if hasattr(msg, 'content')])
        token_count = count_tokens(prompt, model=self.model_name)

        print(f"[ManagerLLMWrapper] Token count: {token_count}")

        # Trim if needed
        if token_count > self.max_tokens:
            print(f"[ManagerLLMWrapper] Trimming input from {token_count} to {self.max_tokens} tokens")
            trimmed_prompt = trim_text_to_token_limit(prompt, max_tokens=self.max_tokens, model=self.model_name)
            messages = [HumanMessage(content=trimmed_prompt)]

        # Forward to base LLM
        return self.base_llm._generate(messages, stop=stop, run_manager=run_manager, **kwargs)

    @property
    def _llm_type(self):
        return "manager-wrapper"
