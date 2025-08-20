import pandas as pd
from dateutil import parser

def merge_posts(twitter_posts, youtube_posts):
   
    all_posts = twitter_posts + youtube_posts   
    df = pd.DataFrame(all_posts)               
    return df



def clean_and_normalize(df: pd.DataFrame) -> pd.DataFrame:


    df["likes"] = pd.to_numeric(df["likes"], errors="coerce").fillna(0).astype("int64")
    df["comments"] = pd.to_numeric(df["comments"], errors="coerce").fillna(0).astype("int64")
    df["shares"] = pd.to_numeric(df["shares"], errors="coerce").fillna(0).astype("int64")

    df.loc[df["platform"] == "YouTube", "post_date"] = df.loc[df["platform"] == "YouTube", "post_date"].apply(
        lambda x: parser.parse(x) if pd.notnull(x) else None
    )
    df["post_date"] = pd.to_datetime(df["post_date"], errors="coerce", utc=True)

    df["content"] = df["content"].fillna("Unknown content")
    
   # Inconsistent field names already unified in extract step

    return df