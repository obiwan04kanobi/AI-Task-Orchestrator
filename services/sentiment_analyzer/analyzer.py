from textblob import TextBlob
import sys

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive Sentiment"
    elif sentiment < 0:
        return "Negative Sentiment"
    else:
        return "Neutral Sentiment"

if __name__ == "__main__":
    input_text = sys.stdin.read()
    print(analyze_sentiment(input_text))
