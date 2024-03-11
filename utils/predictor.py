from core.logger import Logger
from config.init_config import load_model_paths
from config.model_config import load_model_config
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate

logger = Logger(__name__)
TOML_PATH = "config/paths.toml"


class Predictor:
    def __init__(self) -> None:
        self.model_paths = load_model_paths(TOML_PATH)
        self.model_config = load_model_config()
        self.sos = "<s>"
        self.eos = "<|end_of_turn|>"
        self.template = (
            self.sos
            + "Give sentiment analysis as Positive or Negative (nothing else) of the sentence :- {tweet}"
            + self.eos
        )
        self.prompt = PromptTemplate(input_variables=["tweet"], template=self.template)
        self.llm = self.__load_model()

    def get_model_attributes(self) -> None:
        return self.model_paths, self.model_config

    def __load_model(self) -> LlamaCpp:
        llm = LlamaCpp(
            model_path=self.model_config.model_path,
            n_gpu_layers=self.model_config.n_gpu_layers,
            n_batch=self.model_config.n_batch,
            max_new_tokens=self.model_config.max_new_tokens,
            verbose=self.model_config.verbose,
            callback_manager=self.model_config.callback_manager,
        )
        return llm

    async def get_sentiment(self, tweet: str) -> str:
        response = await self.llm(self.prompt.format(tweet=tweet))
        return "Positive" if "positive" in response.lower() else "Negative"
