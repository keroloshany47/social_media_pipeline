import requests

def fetch_twitter_posts(query="news", max_results=50):
    
    bearer_token = "AAAAAAAAAAAAAAAAAAAAABOb3gEAAAAAEGvc7HkMvXa0DcqFZFWxNF26U9c%3DGCS5mRKwX7erq3mR4c1mAgqdtR0vZo7uyIj0NTxG4BjDYolg03"
    headers = {"Authorization": f"Bearer {bearer_token}"}

    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&tweet.fields=public_metrics,created_at,author_id&max_results={max_results}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        twitter_data = response.json()
    except Exception as e:
        print(f"Error fetching Twitter data: {e}")
        return []

    twitter_posts = []
    for tweet in twitter_data.get("data", []):
        metrics = tweet.get("public_metrics", {})
        twitter_posts.append({
            "content": tweet.get("text"),
            "likes": metrics.get("like_count", 0),
            "comments": metrics.get("reply_count", 0),
            "shares": metrics.get("retweet_count", 0),
            "post_date": tweet.get("created_at"),
            "platform": "Twitter",
            "author_id": tweet.get("author_id")
        })

    return twitter_posts