import cv2
import numpy as np

def create_video(image_list, filename):
	frameSize = (360, 192)
	frame_per_second = 1

	PATH_video = '../videos/'

	video = PATH_video + filename +'.mp4'
	out = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*'mp4v'), frame_per_second, frameSize)

	for file in image_list[:-1]:
	    print("using", file, " as image");
	    img = cv2.imread(file)
	    out.write(img)

	out.release()
