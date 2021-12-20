# download-twitch-vod

This is a small python script that easily downloads a twitch vod along with it's metadata and thumbnail 

## Usage

Run the script like so, substituting in the vod's id:

`python3 save-vod.py vod_id`

### Output

- The metadata is appended to ./metadata/index.json
- The thumbnail is added to ./thumbnails with its name as the vod id
- The video is added to ./videos with its name as the vod id

The structure looks like this:

```
working-directory
|-- metadata
|   `-- index.json
|-- thumbnails
|   `-- 1153531342.jpg
`-- videos
    `-- 1153531342.mp4
```

## Dependencies

The script relies on [twicli](https://snapcraft.io/twcli) (a snap of the twitch cli) as well as [youtube-dl](https://youtube-dl.org).
