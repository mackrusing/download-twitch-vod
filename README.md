# download-twitch-vod

This is a small python script that easily downloads a twitch vod along with it's metadata and thumbnail 

## Usage

Run the script like so, substituting in the vod's id:

`python3 save-vod.py ID`

### Output

- The metadata is appended to ./metadata.json
- The thumbnail is added to ./thumbnails/ID.EXT 
- The video is added to ./videos/ID.EXT 

The structure looks like this:

```
working-directory
|-- thumbnails
|   `-- 1153531342.jpg
`-- videos
|   `-- 1153531342.mp4
`-- metadata.json
```

## Dependencies

The script relies on [twicli](https://snapcraft.io/twcli) (a snap of the twitch cli) as well as [youtube-dl](https://youtube-dl.org).
