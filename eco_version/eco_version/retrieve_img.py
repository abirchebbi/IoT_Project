#!/usr/bin/env python3


import picamera

    
# Take pictures every 2 seconds

def take_picture(filename):

	camera = picamera.PiCamera()
	camera.resolution = (800, 600)
	camera.start_preview()

	picName = filename + '.jpg'

	# Take a picture

	camera.capture(picName, resize=(360, 192))
	camera.stop_preview()
	camera.close()

