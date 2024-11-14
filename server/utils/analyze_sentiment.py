# analyze_sentiment.py

import sys
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fetch_news import fetch_news
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)
    sentiment_score = round((score['compound'] + 1) * 50)  # Normalize to 0-100
    return sentiment_score

if __name__ == "__main__":
    team_name = sys.argv[1]  # Team name input from command line argument
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    # Fetch news articles
    articles = fetch_news(team_name, max_results)

    # Calculate sentiment for each article
    scores = [analyze_sentiment(article) for article in articles]
    average_score = round(sum(scores) / len(scores)) if scores else 0

    # Output JSON with the team name and average sentiment score
    print(json.dumps({"team_name": team_name, "average_sentiment": average_score}))
