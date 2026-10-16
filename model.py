
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression


# Locate the project dataset
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Job Market Analysis.csv"


def load_job_data():
    """Load job postings and prepare publication dates."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    data = pd.read_csv(DATA_PATH)

    data["published_date"] = pd.to_datetime(
        data["published_date"],
        errors="coerce",
        utc=True
    )

    data = data.dropna(
        subset=["published_date"]
    ).copy()

    return data


def forecast_monthly_job_postings():
    """
    Train Linear Regression on monthly posting counts
    and forecast the next month.
    """
    data = load_job_data()

    data["Month"] = (
        data["published_date"]
        .dt.tz_convert(None)
        .dt.to_period("M")
        .astype(str)
    )

    monthly_jobs = (
        data.groupby("Month")
        .size()
        .reset_index(name="Job Postings")
        .sort_values("Month")
        .reset_index(drop=True)
    )

    if len(monthly_jobs) < 2:
        raise ValueError(
            "At least two months of data are needed."
        )

    # Create sequential month index
    monthly_jobs["Month_Index"] = range(
        len(monthly_jobs)
    )

    X = monthly_jobs[["Month_Index"]]
    y = monthly_jobs["Job Postings"]

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    # Predict the month after the last recorded month
    next_index = len(monthly_jobs)

    prediction = model.predict(
        pd.DataFrame({
            "Month_Index": [next_index]
        })
    )[0]

    last_month = pd.Period(
        monthly_jobs["Month"].iloc[-1],
        freq="M"
    )

    forecast_month = str(last_month + 1)

    return {
        "last_recorded_month": str(last_month),
        "forecast_month": forecast_month,
        "estimated_job_postings": max(
            0, round(float(prediction))
        ),
        "historical_monthly_data": (
            monthly_jobs[
                ["Month", "Job Postings"]
            ].to_dict(orient="records")
        )
    }


if __name__ == "__main__":
    result = forecast_monthly_job_postings()

    print("Monthly Job Market Forecast")
    print("---------------------------")
    print("Last recorded month:",
          result["last_recorded_month"])
    print("Forecast month:",
          result["forecast_month"])
    print("Estimated job postings:",
          result["estimated_job_postings"])
