import csv
from youtube_comment_downloader import YoutubeCommentDownloader

# Initialize the downloader
downloader = YoutubeCommentDownloader()

# List of video URLs
video_urls = [
    'https://www.youtube.com/watch?v=FBQpsd8igZ8&t=1075s',
    'https://www.youtube.com/watch?v=nRyZpSiqr-U&t=10s',
    'https://www.youtube.com/watch?v=sVvqERTVoSE',
    'https://www.youtube.com/watch?v=vnSowo8me_o&t=4s',
    'https://www.youtube.com/watch?v=sVvqERTVoSE',
    'https://www.youtube.com/watch?v=3pXm_gvJcNA',
    'https://www.youtube.com/watch?v=bUbve2g0n4U',
    'https://www.youtube.com/watch?v=7BGa_JLBRpU',
    'https://www.youtube.com/watch?v=I9u59hPGl08',
]

# Topic name (used as prefix for file names)
topic = 'gambling'

# Loop through each video and scrape comments
for idx, video_url in enumerate(video_urls, start=1):
    print(f"Scraping comments for video {idx}...")

    try:
        comments = downloader.get_comments_from_url(video_url)

        # Clean filename from URL
        video_id = video_url.split('v=')[1].split('&')[0]
        filename = f'youtube_comments_{topic}_{idx}_{video_id}.csv'

        # Save to CSV
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Comment', 'Time'])  # Write header

            for comment in comments:
                writer.writerow([
                    comment.get('author', ''),
                    comment.get('text', ''),
                    comment.get('time', '')
                ])

        print(f"✅ Saved comments to {filename}")

    except Exception as e:
        print(f"❌ Failed to scrape video {video_url}: {e}")

print("🎉 All scraping complete!")
