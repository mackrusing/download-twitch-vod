# Download Twitch VOD

This is a small python script that downloads a Twitch VOD along with its metadata and thumbnail.

- [Installation](#installation)
- [Dependencies](#dependencies)
  - [Twitch CLI](#twitch-cli)
  - [cURL](#curl)
  - [youtube-dl](#youtube-dl)
- [Usage](#usage)
- [Options](#options)
- [Issues](#issues)
- [License](#license)


## Installation

First, be sure all the dependencies are installed and configured. Information on that is down bellow in the [dependencies](#dependencies) section.

Add how to install instructions!


## Dependencies

The script relies on the [Twitch CLI](https://github.com/twitchdev/twitch-cli) to retrieve the metadata, [cURL](https://github.com/curl/curl) to download the thumbnail, and [youtube-dl](https://github.com/ytdl-org/youtube-dl) to download the video.

### Twitch CLI

1. Download the Twitch CLI by following [these instructions](https://github.com/twitchdev/twitch-cli#download).

2. If you don't already have one, [create a Twitch account](https://dev.twitch.tv/login). Make sure to enable two-factor authentication for your account, as it is required for set-up.

2. Register an application and get an access token by following [these instructions](https://dev.twitch.tv/docs/api) in the docs.

### cURL

Many operating systems come with cURL already installed. To check if your machine already has cURL, try the following command in your terminal / command line environment.

```
command -v curl
```

If it is installed, the command will return the command's path like so: `usr/bin/curl`.

If it returns nothing, then follow [these instructions](https://curl.se/docs/install.html) to install cURL.

### youtube-dl

Install youtube-dl [here](https://github.com/ytdl-org/youtube-dl#installation).


## Usage

Description goes here

```
./dl-vod [OPTIONS] ID
```

### Output

- The metadata is appended to a file called `metadata.json` in the current directory.
- The thumbnail is added to a `thumbnails` folder in the current directory.
- The video is added to a `videos` folder in the current directory.

The file structure looks like this:

```
working-directory
├── thumbnails
│   └── 1153531342.jpg
├── videos
│   └── 1153531342.mp4
└── metadata.json
```

The metadata file looks like this:

```JSON
{
  "1197183589": {
    "created_at": "2021-11-05T23:33:15Z",
    "description": "",
    "duration": "5h42m6s",
    "id": "1197183589",
    "language": "en",
    "muted_segments": null,
    "published_at": "2021-11-05T23:33:15Z",
    "stream_id": "40183873723",
    "thumbnail_url": "https://static-cdn.jtvnw.net/cf_vods/d2nvs31859zcd8/86a7c358a7af41766ac0_tubbo_40183873723_1636155188//thumb/thumb0-%{width}x%{height}.jpg",
    "title": "Hi",
    "type": "archive",
    "url": "https://www.twitch.tv/videos/1197183589",
    "user_id": "223191589",
    "user_login": "tubbo",
    "user_name": "Tubbo",
    "view_count": 525420,
    "viewable": "public"
  },
  "1237772702": {
    "created_at": "2021-12-19T14:30:12Z",
    "description": "",
    "duration": "1h50m2s",
    "id": "1237772702",
    "language": "en",
    "muted_segments": null,
    "published_at": "2021-12-19T14:30:12Z",
    "stream_id": "44114517644",
    "thumbnail_url": "https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/283065165a7906da8355_tubbolive_44114517644_1639924203//thumb/thumb0-%{width}x%{height}.jpg",
    "title": "secret v2",
    "type": "archive",
    "url": "https://www.twitch.tv/videos/1237772702",
    "user_id": "478701870",
    "user_login": "tubbolive",
    "user_name": "TubboLIVE",
    "view_count": 113215,
    "viewable": "public"
  }
}
```


## Options

```
-h, --help                    show this help message and exit
-v, --video-path PATH         specify a different directory for video to be 
                              downoaded
-t, --thumb-path PATH         specify a different directory for thumbnail to be 
                              downoaded
-m, --meta-file FILE          specify a different file for metadata to be read 
                              & saved
--no-vid                      don't download video
--no-meta                     don't download metadata
--no-thumb                    don't download thumbnail
```


## Issues
## License
