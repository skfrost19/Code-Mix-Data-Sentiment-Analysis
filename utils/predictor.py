from core.logger import Logger
from config.init_config import load_model_paths
from config.model_config import load_model_config
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate

logger = Logger(__name__)
TOML_PATH = "config/paths.toml"


class Predictor:
    def __init__(self) -> None:
        logger.info("Initializing Predictor")
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
        logger.info("Predictor initialized")

    def get_model_attributes(self) -> None:
        return self.model_paths, self.model_config

    def __load_model(self) -> LlamaCpp:
        logger.info(f"Loading LLM {self.model_paths.name} model")
        try:
            llm = LlamaCpp(
                model_path=self.model_config.model_path,
                n_gpu_layers=self.model_config.n_gpu_layers,
                n_batch=self.model_config.n_batch,
                max_new_tokens=self.model_config.max_new_tokens,
                verbose=self.model_config.verbose,
                callback_manager=self.model_config.callback_manager,
            )
            return llm
        except Exception as e:
            logger.error(f"Error loading LLM model: {e}")
            raise e

    def get_sentiment(self, tweet: str) -> str:
        """
        Get sentiment of a tweet

        Args:
            tweet (str): Tweet to get sentiment of

        Returns:
            str: Sentiment of the tweet
        """

        logger.info(f"Getting sentiment for tweet: {tweet}")
        try:
            response = self.llm(self.prompt.format(tweet=tweet))
            return "Positive" if "positive" in response.lower() else "Negative"

        except Exception as e:
            logger.error(f"Error getting sentiment: {e}")
            raise e
