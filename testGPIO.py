import RPi.GPIO as GPIO
import time
import camera
import vision


print("sys.version : overleap")
#print(sys.version + "\n")

print("GPIO.VERSION : " + GPIO.VERSION)
print("GPIO.RPI_INFO['P1_REVISION'] = " + str(GPIO.RPI_INFO['P1_REVISION']))

io20 = 20
io21 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(io20,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(io21,GPIO.OUT)

rot=True

print("Press button to capture PIC");
try:
	while(rot):
		if(GPIO.input(io20)):
			GPIO.output(io21,GPIO.LOW)
		else:
			GPIO.output(io21,GPIO.HIGH)
			#print(pic_name + ".jpg Ready\n")
			pic_name=camera.capture()
			#print(pic_name + ".jpg Captured\n")
			vision.vision_analysis()
			rot=False

except KeyboardInterrupt:
	print("\n")
	print("Exit by KeyboardInterrupt\n")

except Exception as e:
	print("\n")
	if hasattr(e,'message'):
		print(e.message)
	else:
		print(e)
	print("Exit by Other case!\n")

finally:
	GPIO.cleanup(io20)
	GPIO.cleanup(io21)
	print("Clean up GPIO\n")


