# import libraries, scripts and specify mode
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import os

#set bash command -- unschoene vorruebergehende lsg statt script lesen
bashCommandWebcam1 = "#!/bin/bash \n vax=$(date +%s) \n fswebcam -r 1920x1080 --rotate 270 --no-banner /home/pi/webcam/$vax.jpg \n fswebcam -d /dev/video0 --list-controls"
#bashCommandWebcam2 = "#!/bin/bash \n fbi -a /home/pi/webcam/*.jpg"
bashCommandDeleteAll = "#!/bin/bash \n rm -r /home/pi/webcam \n cd /home/pi \n mkdir webcam"
bashCommandShutDown = "#!/bin/bash \n pkill -f /home/pi/MagicMirror"
bashCommandIMGBack = "#!/bin/bash \n xdotool key Right"
bashCommandIMGForward = "#!/bin/bash \n xdotool key Left"

# set pin modes
takeImage = 16
deleteAllImages = 18
shutDown = 12
backButton = 22
forwardButton = 24
GPIO.setup(takeImage,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(deleteAllImages,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(shutDown,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(backButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(forwardButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# activate them as pullup resistor - does not require physical ones
pull_up_down = GPIO.PUD_UP


while(1):        
    if GPIO.input(takeImage) == 0:
        print("take image..")
        sleep(.1) # delay..
        os.system(bashCommandWebcam1)
        sleep(1)
        #os.system(bashCommandWebcam2)
        #fbi startet nicht
        #feh findet bild nicht; + export display?
        #os.system('pkill -f feh')
        os.system('feh --hide-pointer -x -q -B black -g 1080x1920 -S mtime /home/pi/webcam/*.jpg &')
    if GPIO.input(deleteAllImages) == 0:
        sleep(.1)
        print ("all images deleted")
        os.system('pkill -f feh')
        os.system(bashCommandDeleteAll)
        
    if GPIO.input(shutDown) == 0:
        sleep(.1)
        print ("program shut down")
        os.system(bashCommandShutDown)
        
    if GPIO.input(backButton) == 0:
        sleep(.1)
        print ("img back")
        os.system(bashCommandIMGBack)
        sleep(.4)
        
    if GPIO.input(forwardButton) == 0:
        sleep(.1)
        print ("img forward")
        os.system(bashCommandIMGForward)
        sleep(.4)
        