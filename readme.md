# Download Twitch VOD

This is a small python script that downloads a Twitch VOD along with its metadata and thumbnail.

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Options](#options)
- [Issues](#issues)


## Installation

First, be sure all the dependencies are installed and configured. Information on that is down bellow in the [dependencies](#dependencies) section.

Run the following commands to install the script:

```
sudo curl -L https://github.com/mackrusing/download-twitch-vod/releases/download/v1.0.0/dl-vod -o /usr/local/bin/dl-vod
sudo chmod a+rx /usr/local/bin/dl-vod
```

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

dl-vod is a command-line script to download Twitch VODs along with their metadata and thumbnail. It requires a Python3+ interpreter, the Twitch CLI, cURL, and youtube-dl.

```
dl-vod [OPTIONS] ID
```

### Default output

The default output assumes a preexisting file structure (shown in the example). The output locations can be changed by using the `-m`, `-t`, and `-v` flags (see [options section](#options) below).

- The metadata is appended to a file called `metadata.json` in the current directory (make sure that this file has an empty object).
- The thumbnail is added to a `thumbnails` folder in the current directory.
- The video is added to a `videos` folder in the current directory.

Here is an example of the file structure and JSON file before and after running `dl-vod 1197183589`

Before:
```
working-directory
├── thumbnails
├── videos
└── metadata.json
```

```JSON
{

}
```

After:
```
working-directory
├── thumbnails
│   └── 1153531342.jpg
├── videos
│   └── 1153531342.mp4
└── metadata.json
```

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
  }
}
```

## Options

```
-h, --help                    show this help message and exit
--alt-cli COMMAND             specify a different command for calling the
                              twitch cli
```

### Output
```
-m, --meta-file FILE          specify a different file for metadata to be read
                              & saved
-t, --thumb-path PATH         specify a different directory for thumbnail to be
                              downoaded
-v, --video-path PATH         specify a different directory for video to be
                              downoaded
--no-meta                     don't download metadata
--no-thumb                    don't download thumbnail
--no-vid                      don't download video
```

## Issues

Bugs and suggestions can be reported on this project's [GitHub issues page](https://github.com/mackrusing/download-twitch-vod/issues). If possible, please do not send bug reports to my email.
