from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your API key
API_KEY = "api key"
PLAYLIST_ID = "playlist ket
y"

def get_video_ids(api_key, playlist_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_ids = []
    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlist_id,
        maxResults=50
    )
    while request:
        response = request.execute()
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])
        request = youtube.playlistItems().list_next(request, response)
    return video_ids

def get_transcripts(video_ids):
    transcripts = {}
    for video_id in video_ids:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcripts[video_id] = transcript
        except Exception as e:
            transcripts[video_id] = f"Error: {str(e)}"
    return transcripts

def main():
    video_ids = get_video_ids(API_KEY, PLAYLIST_ID)
    transcripts = get_transcripts(video_ids)
    for video_id, transcript in transcripts.items():
        print(f"Video ID: {video_id}\nTranscript: {transcript}\n")

if __name__ == "__main__":
    main()
