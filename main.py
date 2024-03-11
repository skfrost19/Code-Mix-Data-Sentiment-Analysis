from utils.predictor import Predictor

predictor = Predictor()
tweet = "I love this product"
sentiment = predictor.get_sentiment(tweet)
print(sentiment)
