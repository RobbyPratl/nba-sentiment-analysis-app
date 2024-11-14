import requests
import json
import datetime
from transformers import pipeline
from dateutil.parser import parse
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm


NEWS_API_KEY = "redacted"

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

NBA_TEAMS = [
    "Boston Celtics", "Brooklyn Nets", "New York Knicks", "Philadelphia 76ers", "Toronto Raptors",
    "Chicago Bulls", "Cleveland Cavaliers", "Detroit Pistons", "Indiana Pacers", "Milwaukee Bucks",
    "Atlanta Hawks", "Charlotte Hornets", "Miami Heat", "Orlando Magic", "Washington Wizards",
    "Dallas Mavericks", "Houston Rockets", "Memphis Grizzlies", "New Orleans Pelicans", "San Antonio Spurs",
    "Denver Nuggets", "Minnesota Timberwolves", "Oklahoma City Thunder", "Portland Trail Blazers",
    "Utah Jazz", "Golden State Warriors", "Los Angeles Clippers", "Los Angeles Lakers", "Phoenix Suns", "Sacramento Kings"
]

def fetch_recent_news(team_name, max_results=20):
    """Fetch news articles related to the team name from the past week."""
    end_date = datetime.datetime.now(datetime.timezone.utc)  # Set to UTC for timezone consistency
    start_date = end_date - datetime.timedelta(days=7)
    url = (f'https://newsapi.org/v2/everything?q={team_name}&language=en&from={start_date.date()}'
           f'&to={end_date.date()}&pageSize={max_results}&apiKey={NEWS_API_KEY}')

    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return [
            {
                "text": article['title'] + ' ' + article.get('description', ''),
                "published_at": article.get('publishedAt')
            }
            for article in articles
        ]
    else:
        print(f"Error fetching news for {team_name}: {response.status_code}")
        return []

# Function to calculate weighted sentiment score
def weighted_sentiment_analysis(articles):
    """Analyze and calculate a weighted sentiment score for a list of articles."""
    sentiments = []
    weights = []
    now = datetime.datetime.now(datetime.timezone.utc)  # Use timezone-aware datetime for consistency

    # Scale days to weight, with more recent articles having higher weights
    scaler = MinMaxScaler(feature_range=(1, 2))

    days_ago = [(now - parse(article["published_at"]).astimezone(datetime.timezone.utc)).days for article in articles]
    weights_scaled = scaler.fit_transform([[day] for day in days_ago]).flatten()

    for i, article in enumerate(articles):
        # Perform sentiment analysis
        sentiment_result = sentiment_pipeline(article["text"])[0]
        sentiment_score = sentiment_result['score'] if sentiment_result['label'] == "POSITIVE" else -sentiment_result['score']

        weight = weights_scaled[i]
        weighted_sentiment = sentiment_score * weight
        sentiments.append(weighted_sentiment)
        weights.append(weight)

    # weighted average sentiment
    weighted_avg_sentiment = sum(sentiments) / sum(weights) if weights else 0
    return weighted_avg_sentiment

def analyze_all_teams():
    team_sentiment_data = {}

    with tqdm(total=len(NBA_TEAMS), desc="Processing Teams") as pbar:
        for team in NBA_TEAMS:
            pbar.set_postfix_str(f"Fetching data for {team}")
            articles = fetch_recent_news(team)
            if articles:
                pbar.set_postfix_str(f"Analyzing sentiment for {team}")
                weighted_avg_sentiment = weighted_sentiment_analysis(articles)
                team_sentiment_data[team] = weighted_avg_sentiment
                print(f"Weighted average sentiment for {team}: {weighted_avg_sentiment:.2f}")
            else:
                print(f"No recent articles found for {team}.")
                team_sentiment_data[team] = None  # If no data is found, set sentiment to None

            pbar.update(1)

    with open("all_teams_sentiment_data.json", "w") as f:
        json.dump(team_sentiment_data, f, indent=4)
    print("All team sentiment data saved to all_teams_sentiment_data.json")

if __name__ == "__main__":
    analyze_all_teams()
