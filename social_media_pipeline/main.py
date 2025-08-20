import pandas as pd
from extract.twitter_api import fetch_twitter_posts
from extract.youtube_api import fetch_youtube_videos
from transform.clean_normalize import merge_posts, clean_and_normalize
from transform.enrich import add_engagement_score
from load.save_csv import save_to_csv
from analytics.metrics import (
    get_top5_overall,
    get_top3_per_platform,
    get_daily_engagement,
)
from analytics.moving_avg import get_avg_last7days


def etl_pipeline(query="sport", twitter_results=10, youtube_results=5):
    """
    ETL Pipeline:
    1. Extract (Twitter + YouTube)
    2. Transform (clean + normalize + enrich)
    3. Load (save to CSV)
    4. Analytics (Top posts, daily metrics, moving avg)
    """

    # Extract
    twitter_posts = fetch_twitter_posts(query=query, max_results=twitter_results)
    youtube_posts = fetch_youtube_videos(query=query, max_results=youtube_results)

    # Transform
    df = merge_posts(twitter_posts, youtube_posts)
    df = clean_and_normalize(df)
    df = add_engagement_score(df)

    # Load
    save_to_csv(df, "output/social_media_posts.csv")

    # Analytics
    top5 = get_top5_overall(df)
    top3 = get_top3_per_platform(df)
    daily = get_daily_engagement(df)
    avg7 = get_avg_last7days(daily)

    print("\nTop 5 Overall:\n", top5[["platform", "content", "engagement_score"]])
    print("\nTop 3 Per Platform:\n", top3[["platform", "content", "engagement_score"]])
    print("\nDaily Engagement:\n", daily.head())
    print("\nAverage Engagement Last 7 Days:\n", avg7)

    return df


if __name__ == "__main__":
    df_final = etl_pipeline("sport", twitter_results=10, youtube_results=5)
    print("\nPipeline finished successfully! Total posts:", df_final.shape[0])
