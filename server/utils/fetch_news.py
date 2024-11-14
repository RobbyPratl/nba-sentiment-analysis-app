# fetch_news.py

import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('NEWS_API_KEY')

def fetch_news(team_name, max_results=10):
    """Fetch news articles related to the team name."""
    url = f'https://newsapi.org/v2/everything?q={team_name}&language=en&pageSize={max_results}&apiKey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return [article['title'] + ' ' + article.get('description', '') for article in articles]
    else:
        print(f"Error fetching news: {response.status_code}")
        return []

if __name__ == "__main__":
    # Test the function with a sample team name
    print(fetch_news("Chicago Bulls"))
