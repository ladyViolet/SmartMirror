#!/bin/bash

vax=$(date +%s)
val = 2000000000 - $vax

fswebcam -r 1280x720 --no-banner /home/pi/webcam/$vax.jpg

fbi -a /home/pi/webcam/*.jpg