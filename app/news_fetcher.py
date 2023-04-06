# app/news_fetcher.py
import os
import requests
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Set up the API key for the News API
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_news(query):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": NEWS_API_KEY,
        "q": query,
        "sortBy": "publishedAt",
        "language": "en",
    }

    response = requests.get(url, params=params)
    return response.json()
