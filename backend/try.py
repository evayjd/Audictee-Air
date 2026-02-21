from app.youtube_transcript import extract_video_id, fetch_transcript

url = "https://www.youtube.com/watch?v=sGMb2L58Et0"

video_id = extract_video_id(url)
data = fetch_transcript(video_id)

print(data["sentences"][:3])