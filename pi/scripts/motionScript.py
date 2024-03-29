# import libraries, scripts and specify mode
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import os
from threading import Timer
import threading
from datetime import datetime

motionSensor = 36
motionCounter = 0
saverIsActive = False

#bashCommandScreenOff = "#!/bin/bash \n xset dpms force off"
bashCommandScreenOff = "#!/bin/bash \n feh -F -Y /home/pi/Pictures/Hintergrund.jpg"
bashCommandDeleteAll = "#!/bin/bash \n rm -r /home/pi/webcam \n cd /home/pi \n mkdir webcam"
bashCommandLeaveGallery = "#!/bin/bash \n pkill -f feh"
# bashCommandKillFeh = "#!/bin/bash \n feh -kill"

GPIO.setup(motionSensor, GPIO.IN)

# threading timer that can be restart, cancelled or whatever from any outside event
# and does not block the other code from running
class TimerThread(threading.Thread):
    def __init__(self, timeout=10, sleep_chunk=0.25, callback=None, *args):
        threading.Thread.__init__(self)

        self.timeout = timeout
        self.sleep_chunk = sleep_chunk
        if callback == None:
            self.callback = None
        else:
            self.callback = callback
        self.callback_args = args

        self.terminate_event = threading.Event()
        self.start_event = threading.Event()
        self.reset_event = threading.Event()
        self.count = self.timeout/self.sleep_chunk

    def run(self):
        while not self.terminate_event.is_set():
            while self.count > 0 and self.start_event.is_set():
                # print self.count
                # time.sleep(self.sleep_chunk)
                # if self.reset_event.is_set():
                if self.reset_event.wait(self.sleep_chunk):  # wait for a small chunk of timeout
                    self.reset_event.clear()
                    self.count = self.timeout/self.sleep_chunk  # reset
                self.count -= 1
            if self.count <= 0:
                self.start_event.clear()
                #print 'timeout. calling function...'
                self.callback(*self.callback_args)
                self.count = self.timeout/self.sleep_chunk  #reset

    def start_timer(self):
        self.start_event.set()

    def stop_timer(self):
        self.start_event.clear()
        self.count = self.timeout / self.sleep_chunk  # reset

    def restart_timer(self):
        # reset only if timer is running. otherwise start timer afresh
        if self.start_event.is_set():
            self.reset_event.set()
        else:
            self.start_event.set()

    def terminate(self):
        self.terminate_event.set()

#=================================================================
def my_callback_function():
    #delete images, leave gallery and activate screensaver
    os.system(bashCommandDeleteAll)
    os.system(bashCommandLeaveGallery)
    activateScreensaver()

timeout = 30  # sec
sleep_chunk = .25  # sec

tmr = TimerThread(timeout, sleep_chunk, my_callback_function)
tmr.start()

                    
def disableScreensaver():
    global saverIsActive
    saverIsActive = False
    print("screensaver disabled!")
    print(saverIsActive)
    #os.system(bashCommandScreenOn)
    os.system(bashCommandLeaveGallery)
    os.system(bashCommandLeaveGallery)
    #os.system(bashCommandLeaveGallery)
    
def activateScreensaver():
    global saverIsActive
    saverIsActive = True
    global motionCounter
    print("screensaver activated!")
    print(saverIsActive)
    motionCounter = 0
    os.system(bashCommandScreenOff)

def MOTION(motionSensor):
    global saverIsActive     
    global motionCounter
    
    motionCounter +=1
    if motionCounter > 3:
        motionCounter = 0
    print("Motion Detected!", motionCounter, saverIsActive)
    tmr.restart_timer()
    
    if ((motionCounter == 3) and (saverIsActive == True)):
        disableScreensaver()
        motionCounter = 0
        

print("PIR Module Test (CTRL+C to exit)")
#sleep(1)
#os.system(bashCommandLeaveGallery)
#activateScreensaver()
print("Ready")

try:
    GPIO.add_event_detect(motionSensor, GPIO.RISING, callback=MOTION)
    while 1:
        sleep(.1)
except KeyboardInterrupt:
               print("Quit")
               GPIO.cleanup()
               
        
