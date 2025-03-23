# loadllm.py
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class Loadllm:
    @staticmethod
    def load_llm():
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        llm = LlamaCpp(
            model_path="llama-2-7b-chat.Q4_K_M.gguf",  # Update path as needed
            temperature=0.7,
            max_tokens=2048,
            top_p=0.95,
            n_ctx=4096,  # Try increasing if supported
            n_batch=512,
            n_gpu_layers=40,  # Adjust per GPU
            f16_kv=True,
            callback_manager=callback_manager,
            verbose=True,
        )
        return llm
