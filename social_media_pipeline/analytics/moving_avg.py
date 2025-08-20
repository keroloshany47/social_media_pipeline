import pandas as pd

def get_avg_last7days(df: pd.DataFrame) -> pd.DataFrame:
   
    engagement_trends = df.sort_values(by=["platform", "date"])

    last_7days = (
        engagement_trends.groupby("platform")
        .tail(7)
    )

    avg_last7days = (
        last_7days.groupby("platform")["engagement_score"]
        .mean()
        .reset_index()
        .rename(columns={"engagement_score": "avg_engagement_last7days"})
    )
    return avg_last7days
