import os
import requests

script_dir = os.path.dirname(os.path.abspath(__file__)) 

video_file =  "yt_shorts_english.mp4"
video_path = os.path.join(script_dir, video_file)


url = "http://localhost:5678/webhook-test/upload_trigger"

payload = {
    "caption": "This is test video",
    "video_url": video_path
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)