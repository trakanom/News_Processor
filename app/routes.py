# app/routes.py
from flask import render_template, request
from app import app
from app.news_fetcher import get_news, get_everything


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        everything = request.form.get("everything")

        if everything:
            news_data = get_everything(query)
        else:
            news_data = get_news(query)

        print(news_data)
        articles = news_data.get("articles", [])
        return render_template("index.html", articles=articles)

    return render_template("index.html")
