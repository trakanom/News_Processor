# app/news_fetcher.py
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org"


def get_news(
    query,
    advanced=False,
    sources="",
    languages=None,
    categories=None,
    countries=None,
    popular_sources=None,
):
    if not advanced:
        url = f"{BASE_URL}/v2/top-headlines"
    else:
        url = f"{BASE_URL}/v2/everything"

    params = {
        "apiKey": API_KEY,
        "q": query,
        "pageSize": 100,
    }

    # Merge manually entered sources and selected popular sources
    if popular_sources:
        if sources and sources.strip():
            sources = ",".join(set(sources.strip().split(",") + popular_sources))
        else:
            sources = ",".join(popular_sources)
        params["sources"] = sources

    response = requests.get(url, params=params)
    return json.loads(response.text)
