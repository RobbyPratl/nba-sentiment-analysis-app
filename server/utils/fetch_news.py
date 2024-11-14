# fetch_news.py

import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pytz  # For timezone handling (optional but recommended)

load_dotenv()
API_KEY = os.getenv('NEWS_API_KEY')

def fetch_news(team_name, max_results=10):
    """Fetch news articles related to the team name from the past week."""
    
    utc_now = datetime.utcnow()
    one_week_ago = utc_now - timedelta(weeks=1)
    
    from_date = one_week_ago.strftime('%Y-%m-%d')
    
    to_date = utc_now.strftime('%Y-%m-%d')
    
    url = (
        f'https://newsapi.org/v2/everything?'
        f'q={requests.utils.quote(team_name)}&'
        f'language=en&'
        f'pageSize={max_results}&'
        f'from={from_date}&'
        f'to={to_date}&'
        f'apiKey={API_KEY}'
    )
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        articles = response.json().get('articles', [])
        return [f"{article['title']} {article.get('description', '')}" for article in articles]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

if __name__ == "__main__":
    team = "Chicago Bulls"
    print(fetch_news(team, max_results=5))
