from picamera import PiCamera
from time import sleep
import datetime
import os
import progjpg

def capture():
	work_dir = os.getcwd()
	camera = PiCamera()

	camera.resolution = (320,240)

	camera.start_preview(alpha=200)
	a=datetime.datetime.now()
	a=a.strftime('%Y-%m-%d_%H:%M:%S')

	#camera.capture(work_dir + '/data/%s.jpg' % a)
	camera.capture('%s.jpg' % a)
	camera.stop_preview()

	progjpg.convert_jpg(work_dir + '/%s.jpg' % a, 100, 50)

	return a + '.jpg'

