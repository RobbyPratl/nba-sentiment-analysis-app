# NBA Sentiment Analysis App

This application provides real-time sentiment analysis on NBA teams by fetching and analyzing recent news articles. It generates a sentiment score and displays it in a user-friendly front end. 

### Key Features

- **Data Fetching**: Utilizes the [News API](https://newsapi.org/) to pull the latest news about NBA teams.
- **Sentiment Analysis**: Leverages NLTK’s VADER sentiment analysis tool and a pre-trained DistilBERT model from the `transformers` library to conduct in-depth sentiment analysis. A custom weighting algorithm further refines sentiment scores for accuracy. [Check out the sentiment weighting script here.](https://github.com/RobbyPratl/nba-sentiment-analysis-app/blob/main/compiled_analysis/get_weighted_sentiment.py)
- **Frontend**: Built with React and styled using Material UI for a clean, responsive user experience.
- **Backend**: Designed in JavaScript, which interacts with Python scripts to gather and analyze data, bridging seamless communication between front and back ends.
- **Findings**: There is little correlation between sentiment scores and recent win data. Further analysis is required.
### Visuals

- ![Graph of Wins vs. Sentiment Analysis](static/recent_wins_vs_sentiment.png): A graphical representation of recent wins and sentiment trends.
- ![Website Home Screenshot](static/website_screenshot.png): A snapshot of the app’s main interface.

---

This project demonstrates the integration of machine learning with real-time data fetching and a polished user interface. It’s a showcase of technical versatility, spanning Python, JavaScript, React, and Material UI. 

> *Feel free to explore the code, contribute, or reach out with any feedback!*
