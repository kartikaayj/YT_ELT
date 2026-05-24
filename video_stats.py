import requests
import json

API_KEY = "AIzaSyDg1O8uqYzprj96J9ohuulsONORFgTAhek"
CHANNEL_HANDLE = "MrBeast"

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername={CHANNEL_HANDLE}&key={API_KEY}"

response = requests.get(url)

print(response)

data = response.json()

print(json.dumps(data,indent=4))