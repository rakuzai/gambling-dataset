import csv
from youtube_comment_downloader import YoutubeCommentDownloader

# Initialize the downloader
downloader = YoutubeCommentDownloader()

# Dictionary of topics and their YouTube video URLs
video_links = {
    'politics': 'https://www.youtube.com/watch?v=qtz3gHi-XQM',
    'technology': 'https://www.youtube.com/watch?v=VXqMJqP7mvk',
    'sports': 'https://www.youtube.com/watch?v=H-9fQ7OkNrg',
    'entertainment': 'https://www.youtube.com/watch?v=nl9oP6GWLoc',
    'travel': 'https://www.youtube.com/watch?v=PgrGHs0U2Zs&t=67s',
    'daily_life': 'https://www.youtube.com/watch?v=67NYUTrcV9Y',
    'fashion': 'https://www.youtube.com/watch?v=YMv5a-WLm4A',
    'finance': 'https://www.youtube.com/watch?v=_-ofPdzjxAs',
    'hobbies': 'https://www.youtube.com/watch?v=7SZI9sa-vWU'
}

# Loop through each topic and download comments
for topic, url in video_links.items():
    print(f"Scraping comments for {topic}...")

    # Fetch comments
    comments = downloader.get_comments_from_url(url)

    # File name based on topic
    filename = f'youtube_comments_{topic}.csv'
    
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

    print(f"Saved comments to {filename}")

print("✅ All scraping complete!")
