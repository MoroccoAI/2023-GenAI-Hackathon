from llama_cpp import Llama


class LLLM:
    """A model class to load the Local LLM"""

    def __init__(self, model_path) -> None:
        self.model_path = model_path
        self.llm = Llama(self.model_path, chat_format="llama-2",
            n_ctx=8192,
            n_threads=8)
    
    def generate(self, question: str):
        output = self.llm.create_chat_completion(
                        messages = [
                            {"role": "system", "content": "You are an expert in environmental sciences."},
                            {"role": "user", "content": question}
                        ],
                        max_tokens = 256
                )
        return output