import aiofiles
import aiohttp
import json
import os

with open("emotion_map.json") as json_file:
    emotion_map = json.load(json_file)

def extract_emotion(prob_list):
    max_score = 0
    emotion=""
    for i in prob_list:
        if i['score']>max_score:
            max_score=i['score']
            emotion=i['label']
    return emotion_map[emotion]

async def download_track(track_url, filepath):
    track_file_path = os.path.join(os.getcwd(),filepath)
    async with aiohttp.ClientSession() as session:
        async with session.get(track_url) as response:
            if response.status == 200:
                async with aiofiles.open(track_file_path, "wb+") as f:
                    await f.write(await response.read())