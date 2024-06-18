#!/bin/bash

# remove the old video
rm ./videos/$2

ffmpeg -i ./videos/$1 -filter:v \
"drawtext=text='$3':x=24:y=540:fontsize=35:fontcolor=black:enable='between(t,0,10)'" \
-c:a copy -c:v libx264 -preset slow -crf 18 ./videos/$2