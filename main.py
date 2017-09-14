import RPi.GPIO as GPIO
import time
import camera
import request

print("Deeping Sauce with Server v.1.0")
print("sys.version : overleap")
#print(sys.version + "\n")

print("GPIO.VERSION : " + GPIO.VERSION)
print("GPIO.RPI_INFO['P1_REVISION'] = " + str(GPIO.RPI_INFO['P1_REVISION']))

io20 = 20
io21 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(io20,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(io21,GPIO.IN, pull_up_down=GPIO.PUD_UP)

rot=True

print("Press button to capture PIC");
try:
	while(rot):
		if(not GPIO.input(io20)):	# Labeling(20)
			print("=> Img Labelling")
			pic_name = camera.capture()
			print(pic_name + " Ready\n")
			request.send_image_json(pic_name,20)
			rot = False
			
		elif(not GPIO.input(io21)):	# OCR(21)
			print("=> OCR")
			pic_name = camera.capture()
			print(pic_name + " Ready\n")
			request.send_image_json(pic_name,21)
			rot = False

except KeyboardInterrupt:
	print("\n")
	print("Exit by KeyboardInterrupt\n")

except Exception as e:
	print("\n")
	if hasattr(e,'message'):
		print(e.message)
	else:
		print(e)
	print(e)
	print("ERROR")
	print("Exit by Other case!\n")

finally:
	GPIO.cleanup(io20)
	GPIO.cleanup(io21)
	print("Clean up GPIO\n")


