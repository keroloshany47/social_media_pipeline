import pandas as pd

def add_engagement_score(df: pd.DataFrame) -> pd.DataFrame:
    
    df["engagement_score"] = df["likes"] + df["comments"] + df["shares"]
    return df



