import cv2,os,urllib.request
import numpy as np
from django.conf import settings


class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the video stream.
		
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
  
		return jpeg.tobytes()



    
def getDistance(x1, y1, x2, y2):
	x = x2 - x1
	y = y2 - y1
	return np.sqrt(x * x + y * y)
 	