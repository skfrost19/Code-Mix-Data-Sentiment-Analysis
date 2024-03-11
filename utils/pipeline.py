from utils.get_model import download_model
from core.logger import Logger
from utils.predictor import Predictor

logger = Logger(__name__)


class Pipeline:
    def __init__(self) -> None:
        logger.info("Initializing Pipeline")
        logger.info("Phase 1:- Downloading model")
        download_model()
        logger.info("Phase 1 complete")
        logger.info("Phase 2:- Initializing Predictor")
        self.predictor = Predictor()
        logger.info("Phase 2 complete")

    def get_sentiment(self, tweet: str) -> str:
        return self.predictor.get_sentiment(tweet)
