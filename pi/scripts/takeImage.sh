#!/bin/bash

vax=$(date +%s)
val = 2000000000 - $vax

fswebcam -r 1920x1080 --rotate 270 --no-banner /home/pi/webcam/$vax.jpg
fswebcam -d /dev/video0 --list-controls

#convert "$/home/pi/webcam/1592228936.jpg" -rotate 270 "$/home/pi/webcam/rotate/1592228936.jpg"

fbi -a /home/pi/webcam/*.jpg

$SHELL