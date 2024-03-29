# import libraries, scripts and specify mode
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import os
import subprocess
import sys

#TODO: weiterer button -> startDefaultConfig

#set bash command -- unschoene vorruebergehende lsg statt script lesen
bashCommandStartMirrorBackground = "#!/bin/bash \n cd /home/pi \n cp /home/pi/mmbackgroundconfig/config.js /home/pi/MagicMirror/config/config.js \n cd /home/pi/MagicMirror \n npm start \n cd /home/pi"
bashCommandStartMirrorDefault = "#!/bin/bash \n cd /home/pi \n cp /home/pi/mmdefaultconfig/config.js /home/pi/MagicMirror/config/config.js \n cd /home/pi/MagicMirror \n npm start \n cd /home/pi"
bashMotion ="#!/bin/bash \n python /home/pi/scripts/motionScript.py &"
#todo add pkill mirror vor start

# set pin modes
startMirror = 10 #background
startMirror2 = 32 #default
GPIO.setup(startMirror,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(startMirror2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# activate them as pullup resistor - does not require physical ones
pull_up_down = GPIO.PUD_UP


while(1):
    
    if GPIO.input(startMirror) == 0:
        sleep(.1)
        print ("start smart")
        #os.system("/home/pi/scripts/motionScript.py 1")
        #os.system("pkill -f /home/pi/MagicMirror")
        os.system(bashCommandStartMirrorBackground)
    if GPIO.input(startMirror2) == 0:
        sleep(.1)
        print ("start smart2")
        #os.system("pkill -f /home/pi/MagicMirror")
        os.system(bashMotion)#todo in stopp adden
        os.system(bashCommandStartMirrorDefault)