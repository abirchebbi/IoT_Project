import datetime
from time import sleep
import picamera
import glob
import os
    
# Take pictures every 2 seconds

PATH = '../images/'

camera = picamera.PiCamera()
camera.rotation = 90
camera.resolution = (800, 600)
camera.start_preview()
while True:

    # prepare the camera
    
    sleep(0.5)   
    Format = "%Y.%m.%d-%H:%M:%S"

    
    # Grab the current time
    currentTime = datetime.datetime.now()

    # Create name for the picture
    picTime = currentTime.strftime(Format)
    picName = picTime + '.jpg'
    path= PATH + picName
    # Take a picture

    camera.capture(path, resize=(360, 192))

