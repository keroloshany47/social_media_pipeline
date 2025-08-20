import pandas as pd

def get_top5_overall(df: pd.DataFrame) -> pd.DataFrame:
   
    top5_overall = df.sort_values(by="engagement_score", ascending=False).head(5)
    return pd.DataFrame(top5_overall)


def get_top3_per_platform(df: pd.DataFrame) -> pd.DataFrame:
   
    top3_per_platform = (
        df.groupby("platform")
          .apply(lambda x: x.sort_values(by="engagement_score", ascending=False).head(3))
          .reset_index(drop=True)
    )
    return pd.DataFrame(top3_per_platform)


def get_daily_engagement(df: pd.DataFrame) -> pd.DataFrame:
   
    daily_engagement = (
        df.groupby(["platform", df["post_date"].dt.date])["engagement_score"]
          .sum()
          .reset_index()
          .rename(columns={"post_date": "date"})
    )
    return daily_engagement
