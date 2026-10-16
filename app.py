from flask import Flask, request, jsonify, render_template
import pandas as pd

from model import forecast_monthly_job_postings, load_job_data

app = Flask(__name__)

df = load_job_data()
df.columns = df.columns.str.strip().str.lower()


def clean_value(value):
    if pd.isna(value):
        return None
    if hasattr(value, "item"):
        return value.item()
    return value


def job_to_dict(row):
    fields = ["title", "country", "is_hourly", "hourly_low", "hourly_high", "budget", "published_date", "link"]

    return {field: clean_value(row.get(field))
        for field in fields
        if field in df.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/jobs")
def search_jobs():
    keyword = request.args.get("keyword", "").strip()

    if not keyword:
        return jsonify({"error": "Please provide a keyword."}), 400

    matches = df[df["title"].astype(str).str.contains(keyword, case=False, regex=False, na=False)].head(50)

    return jsonify({"keyword": keyword, "results_count": len(matches), "jobs": [job_to_dict(row) for _, row in matches.iterrows()]})


@app.route("/api/recommendations")
def recommend_jobs():
    keyword = request.args.get("keyword", "").strip()

    if not keyword:
        return jsonify({"error": "Please provide a keyword."}), 400

    matches = df[df["title"].astype(str).str.contains(keyword, case=False, regex=False, na=False)].head(10)

    return jsonify({"keyword": keyword, "recommendations_count": len(matches), "recommendations": [job_to_dict(row) for _, row in matches.iterrows()]})


@app.route("/api/forecast")
def forecast():
    try:
        return jsonify(forecast_monthly_job_postings())
    except (ValueError, FileNotFoundError) as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)