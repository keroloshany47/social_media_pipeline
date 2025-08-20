import pandas as pd
import os

def save_to_csv(data, filename="output/social_media_posts.csv"):
   
    if data is None or len(data) == 0:
        print("No data to save.")
        return

    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)

    
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    data.to_csv(filename, index=False, encoding="utf-8")
    print(f"Data saved to {filename}")