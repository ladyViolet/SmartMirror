#!/bin/bash

export DISPLAY=:0

python /home/pi/scripts/buttonLong.py &
python /home/pi/scripts/buttonShort.py &
# python /home/pi/scripts/motionScript.py &
