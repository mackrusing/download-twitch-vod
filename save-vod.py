import subprocess
import sys
import json

# get arguments
id = sys.argv[1]

# get current json index file
json_file = open('metadata/index.json')
json_data = json.load(json_file)
json_file.close()

# get vod metadata 
video_metadata = json.loads(subprocess.run(['twcli', 'api', 'get', 'videos', '-q', f'id={id}'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
json_data[id] = video_metadata['data'][0]

# write to index json file
with open('metadata/index.json', 'w', encoding='utf-8') as f:
  json.dump(json_data, f, ensure_ascii=False, indent=2)

# download thumbnail
thumbnail_url = json_data[id]['thumbnail_url'].replace('%{width}', '1280').replace('%{height}', '720')
file_type = thumbnail_url.split('.')[-1]
subprocess.run(['curl', thumbnail_url, '--output', f'thumbnails/{id}.{file_type}'])

# download video
subprocess.run(['youtube-dl', '-o', f'./videos/{id}.%(ext)s', f'https://www.twitch.tv/videos/{id}'])
