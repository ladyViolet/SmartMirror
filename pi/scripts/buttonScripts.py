# import libraries, scripts and specify mode
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import os

#set bash command -- unschoene vorruebergehende lsg statt script lesen
bashCommandStartMirror = "#!/bin/bash \n cd /home/pi \n cp /home/pi/mmbackgroundconfig/config.js /home/pi/MagicMirror/config/config.js \n cd /home/pi/MagicMirror \n npm start \n cd /home/pi"
bashCommandWebcam = "#!/bin/bash \n vax=$(date +%s) \n val = 2000000000 - $vax \n fswebcam -r 1280x720 --no-banner /home/pi/webcam/$vax.jpg \n fbi -a /home/pi/webcam/*.jpg"
bashCommandDeleteAll = "#!/bin/bash \n rm -r /home/pi/webcam \n cd /home/pi \n mkdir webcam"
bashCommandShutDown = "#!/bin/bash \n pkill -f /home/pi/MagicMirror"

# set pin modes
startMirror = 10
takeImage = 16
deleteAllImages = 18
shutDown = 12
GPIO.setup(startMirror,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(takeImage,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(deleteAllImages,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(shutDown,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# activate them as pullup resistor - does not require physical ones
pull_up_down = GPIO.PUD_UP


while(1):
    
    if GPIO.input(startMirror) == 0:
        sleep(.1)
        print ("start smart")
        os.system(bashCommandStartMirror)
        
    if GPIO.input(takeImage) == 0:
        print("take image..")
        sleep(.1) # delay..
        os.system(bashCommandWebcam)
        
    if GPIO.input(deleteAllImages) == 0:
        sleep(.1)
        print ("all images deleted")
        os.system(bashCommandDeleteAll)
        
    if GPIO.input(shutDown) == 0:
        sleep(.1)
        print ("program shut down")
        os.system(bashCommandShutDown)
        


        
