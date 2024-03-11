from pydantic import BaseModel
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import Any


class ModelConfig(BaseModel):
    n_gpu_layers: int = 14
    n_batch: int = 50
    model_path: str = "models/openchat-3.5-0106.Q8_0.gguf"
    max_new_tokens: int = 2
    verbose: bool = True
    callback_manager: Any = CallbackManager([StreamingStdOutCallbackHandler()])


def load_model_config() -> ModelConfig:
    return ModelConfig()
