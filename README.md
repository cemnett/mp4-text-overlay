# mp4 Video Overlay

## Overview

This project takes in a video and adds text as an overlay on the video. 
It utilizes `ffmpeg` in order to do this. You can modify the video and/or play a video.


## Running the project

- Ensure ffmpeg is installed
- run `python3 ./video`
  - The python script video will call the bash scripts modifyVideo and playVideo
    if required.
- You can then choose to modify a video, play a video, both, or quit.
- If you are doing both or just modifying, then you can choose to enter your own text and file names.
- If only playing a video, you then specify the video name.

### Default Video and Text
Default values can be used rather than taking in input. 
The default input video is testVideo.mp4.
The default output video with the overlay is testVideoOverlay.mp4.
These default videos can be found in the video folder.
The default text is "This is a test."
