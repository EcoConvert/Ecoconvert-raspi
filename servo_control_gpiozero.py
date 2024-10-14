from gpiozero import Servo
from time import sleep

servo1 = Servo(18)
servo2 = Servo(26)

def set_servo_angle(angle):
	servo_value = (angle - 90) / 90
	servo.value = servo_value
	print (f"Servo moved to {angle} degrees")
	sleep(1)                                                                          



try:
	while True:
		set_servo_angle(servo1, 0)
		sleep(1)
		
		set_servo_angle(servo1, 90)
		sleep(1)
		
		set_servo_angle(servo1, 180)
		sleep(1)
		
		# servo2
		
		set_servo_angle(servo2, 0)
		sleep(1)
		
		set_servo_angle(servo2, 90)
		sleep(1)
		
		set_servo_angle(servo2, 180)
		sleep(1)
		
except KeyboardInterrupt:
	print("Program stopped")
