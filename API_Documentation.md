\# Job Market Analysis API Documentation



\## Overview

This API provides job search, job recommendations, and job posting forecasts.



\## Base URL

`http://127.0.0.1:5000`



\## API Endpoints



\### 1. Home

\*\*Endpoint:\*\* `/`



\*\*Method:\*\* GET



Shows the API welcome message and available endpoints.



\### 2. Search Jobs

\*\*Endpoint:\*\* `/api/jobs?keyword=designer`



\*\*Method:\*\* GET



Searches job postings using a keyword.



\### 3. Job Recommendations

\*\*Endpoint:\*\* `/api/recommendations?keyword=developer`



\*\*Method:\*\* GET



Returns job recommendations based on matching keywords in job titles.



\### 4. Job Forecast

\*\*Endpoint:\*\* `/api/forecast`



\*\*Method:\*\* GET



Returns historical monthly job counts and the forecast for the next month.



\## How to Run

1\. Open Anaconda Prompt.

2\. Navigate to the project folder.

3\. Run `python app.py`.

4\. Open the base URL in a browser.



\## Limitations

\- Recommendations use job-title keyword matching.

\- Forecasts are affected by uneven historical data coverage.

\- The API uses the available dataset and does not fetch live job postings automatically.

