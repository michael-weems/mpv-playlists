# Video Playlist CLI

A simple CLI tool to generate playlists from directories and save off configuration options for playing videos via `mpv`. Written in `python` specifically so my buddy can understand it. But also some `bash` because why not.

There are a few components to this: downloading and playlist management. `dl` is a convenience bash-script for downloading videos. `play.py` is a convenience python script for running `mpv` with your own configuration options. `to720p` take a directory of mp4 videos (videos), and outputs a directory of those videos converted to 720p (videos-720p).

## Installation

For downloading, make sure you install: 
- [yt-dlp](https://github.com/yt-dlp/yt-dlp).

For playlist management, please make sure to install:
- [python v3.13+](https://www.python.org/downloads/)
- [mpv](https://mpv.io/installation/)

For converting resolution, make sure you install: 
- [ffmpeg](https://ffmpeg.org/download.html)

## Usage

### Playlist management

When videos are playing, you can end the program by:
- `Ctrl+c`
- manually closing the video window
- `pkill mpv`

```bash
# generate playlist from directory
# NOTE: if you'd like to re-order the playlist, open the file in a text editor and re-order the entries
python play.py --from-directory a/path/to/videos # outputs "videos.m3u" playlist file

# configure how mpv plays the videos
python play.py --shuffle --fullscreen videos.m3u

# save off configuration for later use
python play.py --shuffle --fullscreen videos.m3u -o config.json

# re-use configuration
python play.py -c config.json videos.m3u

# run the program in verbose mode (usually for debugging)
python play.py --verbose -c config.json videos.m3u
```

### Video downloads

Create an "inbox" file with the below format

Format:
```bash
output-path,url
output-path,url
output-path,url
output-path,url
```

Example:
```bash
karaoke/song1,http://the-url
game1/ost-1,http://the-url-2
```

> If downloading from a playlist, make sure to remove the `&list` query-parameter.

Run the `dl` script like below:

```bash
./dl <your-inbox-file-path>
```

Read the script output to check for failures / successes.

### Resolution conversion

Create a directory containing all the mp4 files you wish to downscale to 720p. It can contain as many nested folders as you wish, the conversion script will respect this.

```bash
./to720p path/to/your/videos/dir 
# outputs videos to 'path/to/your/videos/dir-720p'
```
> If a file cannot be converted, it will instead just copy the original.

Read the script output to check for failures / successes.

## Trim Videos

```bash
# in 'output.mp4', get the first minute and 15 seconds of input.mp4 and trim the rest
ffmpeg --ss 00:00:00 -t 00:01:15 -i input.mp4 output.mp4
```
