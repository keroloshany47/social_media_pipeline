import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

def get_top5_overall(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by="engagement_score", ascending=False).head(5)

def get_top3_per_platform(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("platform")
          .apply(lambda x: x.sort_values(by="engagement_score", ascending=False).head(3))
          .reset_index(drop=True)
    )

def get_daily_engagement(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["platform", df["post_date"].dt.date])["engagement_score"]
          .sum()
          .reset_index()
          .rename(columns={"post_date": "date"})
    )


def plot_daily_engagement(daily_df: pd.DataFrame, output_path="output/daily_engagement.png"):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=daily_df, x="date", y="engagement_score", hue="platform", marker="o")
    plt.title("Daily Engagement by Platform")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Daily engagement plot saved to {output_path}")


def plot_engagement_distribution(df: pd.DataFrame, output_path="output/engagement_distribution.png"):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["engagement_score"], bins=20, kde=True)
    plt.title("Distribution of Engagement Score")
    plt.xlabel("Engagement Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Engagement distribution plot saved to {output_path}")


def get_top_words(df: pd.DataFrame, top_n=10):
    all_text = " ".join(df["content"].astype(str)).lower()
    words = re.findall(r"\b[a-zA-Z]{3,}\b", all_text)  
    common_words = Counter(words).most_common(top_n)
    return pd.DataFrame(common_words, columns=["word", "count"])
