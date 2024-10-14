from gpiozero import Servo
from time import sleep

#Instances
leftServo = Servo(18)
rightServo = Servo(26)

def set_servo_angle(angle):
	servo_value = (angle - 90) / 90
	servo.value = servo_value
	print (f"Servo moved to {angle} degrees")
	sleep(1)
	
        
#-------------------------RUN
try:
	while True:
		# servo1
		set_servo_angle(leftServo, 0)
		sleep(2)
		
		# servo2
		set_servo_angle(rightServo, 0)
		sleep(2)
		
except KeyboardInterrupt:
	print("Program stopped")

if __name__ == "__main__":
    test_capture()
