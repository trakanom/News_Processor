# app/routes.py
from flask import render_template, request, Response, session, current_app as app

from app.news_fetcher import get_news
import json
import os


@app.route("/", methods=["GET", "POST"])
def index():
    with open(os.path.join(app.root_path, "static", "languages.json"), "r") as f:
        languages = json.load(f)

    with open(os.path.join(app.root_path, "static", "categories.json"), "r") as f:
        categories = json.load(f)

    with open(os.path.join(app.root_path, "static", "countries.json"), "r") as f:
        countries = json.load(f)
    with open(os.path.join(app.root_path, "static", "sources.json"), "r") as f:
        sources = json.load(f)
    with open(os.path.join(app.root_path, "static", "popular_sources.json"), "r") as f:
        popular_sources = json.load(f)

    news_data = []
    form_data = {}
    total_results = 0
    query = ""

    if request.method == "POST":
        query = request.form["query"]
        if query.strip():
            advanced = "advanced" in request.form
            sources = request.form.get("sources", "")
            form_data = request.form
            popular_sources = request.form.getlist("popular_sources")
            news_results = get_news(
                query,
                advanced=advanced,
                sources=sources,
                popular_sources=popular_sources,
            )
            total_results = news_results["totalResults"]
            news_data = news_results["articles"]

            # Store the search results in the session
            if "history" not in session:
                session["history"] = []
            session["history"].append(news_data)
            session.modified = True
    # context = {
    #     'popular_sources': popular_sources,
    #     # 'languages': ...,
    #     # 'categories': ...,
    #     # 'countries': ...,
    # }

    # return render_template('advanced_options.html', **context)

    return render_template(
        "index.html",
        query=query,
        form_data=form_data,
        news_data=news_data,
        languages=languages,
        categories=categories,
        countries=countries,
        sources=sources,
        popular_sources=popular_sources,
        total_results=total_results,
    )


@app.route("/download_results", methods=["POST"])
def download_results():
    news_data = json.loads(request.form["news_data"])
    file_content = json.dumps(news_data, indent=4)

    return Response(
        file_content,
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=results.json"},
    )
