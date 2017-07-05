import sys
import RPi.GPIO as GPIO
import time
import camera
import vision


print("sys.version : ")
print(sys.version + "\n")

print("GPIO.VERSION : " + GPIO.VERSION)
print("GPIO.RPI_INFO['P1_REVISION'] = " + str(GPIO.RPI_INFO['P1_REVISION']))

io20 = 20
io21 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(io20,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(io21,GPIO.OUT)

print("Press button to capture PIC");
try:
	while(True):
		if(GPIO.input(io20)):
			GPIO.output(io21,GPIO.LOW)
		else:
			GPIO.output(io21,GPIO.HIGH)
			pic_name=camera.capture()
			print(pic_name + '\n')
			vision_analysis(pic_name)

except KeyboardInterrupt:
	print("\n")
	print("Exit by KeyboardInterrupt\n")

except:
	print("\n")
	print("Exit by Other case!\n")

finally:
	GPIO.cleanup(io20)
	GPIO.cleanup(io21)
	print("Clean up GPIO\n")


