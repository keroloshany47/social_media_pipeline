from googleapiclient.discovery import build

def fetch_youtube_videos(query="music", max_results=50):
    
    api_key = "AIzaSyBa-fzA-iQd0XwfNg9_Zi8mnczaY_w4qWY"
    youtube = build("youtube", "v3", developerKey=api_key)

    try:
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            maxResults=max_results
        )
        response = request.execute()
    except Exception as e:
        print(f"Error fetching YouTube search results: {e}")
        return []

    youtube_posts = []
    for item in response.get("items", []):
        video_id = item["id"]["videoId"]

        try:
            video_details = youtube.videos().list(
                part="snippet,statistics",
                id=video_id
            ).execute()["items"][0]

            youtube_posts.append({
                "content": video_details["snippet"]["title"],
                "likes": int(video_details["statistics"].get("likeCount", 0)),
                "comments": int(video_details["statistics"].get("commentCount", 0)),
                "shares": 0,  # YouTube API does not provide shares
                "post_date": video_details["snippet"]["publishedAt"],
                "platform": "YouTube",
                "author_id": video_details["snippet"]["channelId"]
            })
        except Exception as e:
            print(f"Error fetching video details for {video_id}: {e}")
            continue

    return youtube_posts
