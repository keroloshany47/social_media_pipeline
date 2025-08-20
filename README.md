# Social Media ETL Pipeline

## Overview
The **Social Media ETL** project collects and analyzes social media content (Twitter + YouTube) through an ETL process:

1. **Extract**: fetch posts from Twitter and YouTube  
2. **Transform**: clean, normalize, and calculate `engagement_score`  
3. **Load**: save the data into CSV files  
4. **Analytics**: analyze top posts, daily engagement, and 7-day moving averages  

## Project Structure

social_media_pipeline/
│
├─ extract/
│ ├─ twitter_api.py # fetch Twitter posts
│ └─ youtube_api.py # fetch YouTube videos
│
├─ transform/
│ ├─ clean_normalize.py # merge, clean, and normalize data
│ └─ enrich.py # add engagement_score
│
├─ load/
│ └─ save_csv.py # save data to CSV
│
├─ analytics/
│ ├─ metrics.py # calculate top posts & daily engagement
│ └─ moving_avg.py # 7-day moving average
│
├─ dags/
│ └─ social_media_etl.py # Airflow DAG
│
└─ main.py # run full ETL pipeline


## Extract

### Twitter
**File:** `extract/twitter_api.py`  
- Main function: `fetch_twitter_posts(query, max_results)`  
- Uses Twitter API v2 to fetch recent tweets with stats: likes, comments, shares  

### YouTube
**File:** `extract/youtube_api.py`  
- Main function: `fetch_youtube_videos(query, max_results)`  
- Uses YouTube Data API to fetch recent videos with stats: likes, comments, shares  

## Transform

### Merge & Clean
**File:** `transform/clean_normalize.py`  
- `merge_posts(twitter_posts, youtube_posts)` merges lists  
- `clean_and_normalize(df)` converts types, handles missing values, and normalizes dates  

### Enrich Data
**File:** `transform/enrich.py`  
- `add_engagement_score(df)` calculates `engagement_score = likes + comments + shares`  

## Load
**File:** `load/save_csv.py`  
- `save_to_csv(data, filename)` saves results to CSV  
- Ensures folders exist and creates them if missing  

## Analytics

### Metrics
**File:** `analytics/metrics.py`  
- `get_top5_overall(df)` → top 5 posts overall  
- `get_top3_per_platform(df)` → top 3 posts per platform  
- `get_daily_engagement(df)` → daily engagement per platform  

### Moving Average
**File:** `analytics/moving_avg.py`  
- `get_avg_last7days(df)` → 7-day moving average engagement per platform  

## DAG (Airflow)
**File:** `dags/social_media_etl.py`  
- Defines DAG to run the ETL daily with Airflow  
- Passes `query` (e.g., "AI") to `etl_pipeline`  

## Main Pipeline
**File:** `main.py`  
- Main function: `etl_pipeline(query, twitter_results, youtube_results)`  
- Steps: **Extract → Transform → Enrich → Load → Analytics**  
- Prints results to terminal  

## Requirements
- Python 3.9+  
- Libraries:
pip install pandas requests google-api-python-client python-dateutil apache-airflow

## Run

Run pipeline directly:
```bash

python main.py

Trigger DAG via Airflow

airflow dags trigger social_media_etl


## Output
- CSV: `output/social_media_posts.csv`  
- Terminal stats:
  - Top 5 posts overall  
  - Top 3 per platform  
  - Daily engagement  
  - 7-day average engagement

