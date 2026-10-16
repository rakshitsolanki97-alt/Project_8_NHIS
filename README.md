
# Project_8_NHIS

## Job Market Analysis and Recommendation System

This project analyzes job market data to identify popular job titles, salary patterns, country-wise job opportunities, and monthly job posting trends.

It also provides job search, keyword-based recommendations, and job posting forecasts through a Flask web application.

## Dataset Information

- Total Job Postings: 244,828
- Columns: 8
- Time Period: November 2023 to March 2024

## Data Analysis

The following analysis was performed:

- Job Type Distribution
- Top 10 Job Titles
- Country-wise Job Postings
- Hourly Rate Analysis
- Correlation Heatmap
- Outlier Detection
- Monthly Job Posting Trends

## Feature Engineering

- Extracted year and month from posting dates
- Created month names
- Extracted day and weekday
- Used date features for trend analysis and forecasting

## Machine Learning Model

- Linear Regression
- Monthly Job Posting Forecast

## Web Application

The Flask web application provides:

- Job Search
- Keyword-based Job Recommendations
- Monthly Job Posting Forecast

## API Endpoints

- `/` – Home Page
- `/api/jobs?keyword=designer` – Search Jobs
- `/api/recommendations?keyword=developer` – Job Recommendations
- `/api/forecast` – Monthly Forecast

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Plotly
- Flask
- HTML
- CSS
- JavaScript
- GitHub

## Project Structure

Project-8/

- Job Market Analysis.csv
- Job Market Analysis.ipynb
- app.py
- model.py
- API_Documentation.md
- README.md
- templates/
  - index.html

## Conclusion

This project uses data analysis, visualization, and Linear Regression to explore job market trends. The Flask web application provides keyword-based job search, recommendations, and monthly job posting forecasts.
