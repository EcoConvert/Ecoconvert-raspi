import RPi.GPIO as GPIO
from hx711 import HX711
from modules.Camera import Camera
from gpiozero import Servo
from time import sleep


#Instances
leftServo = Servo(18)
rightServo = Servo(26)
GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6, pd_sck_pin=5)


def set_servo_angle(angle):
	servo_value = (angle - 90) / 90
	servo.value = servo_value
	print (f"Servo moved to {angle} degrees")
	sleep(1)                                                                          


def test_capture():
    cam = Camera(0)
    cam.init_camera()
    
    labels = cam.load_labels()
    print(labels)   

    inference = cam.capture_and_infer()
    print(inference)
    
#-------------------------RUN
try:
	while True:
		reading = hx.get_raw_data_mean()
		print(reading)
		
		
		set_servo_angle(leftServo1, 0)
		sleep(2)
		
		set_servo_angle(leftServo1, 90)
		sleep(2)
		
		set_servo_angle(leftServo, 180)
		sleep(2)
		
		# servo2
		
		set_servo_angle(rightServo, 0)
		sleep(2)
		
		set_servo_angle(rightServo, 90)
		sleep(2)
		
		set_servo_angle(rightServo, 180)
		sleep(2)
		
except KeyboardInterrupt:
	print("Program stopped")

if __name__ == "__main__":
    test_capture()
