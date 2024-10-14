import RPi.GPIO as GPIO
from modules.Camera import Camera
from gpiozero import Servo
from gpiozero import LED
from time import sleep

IN1 = LED(19)
IN2 = LED(18)

#Instances
leftServo = Servo(18)
rightServo = Servo(26)
GPIO.setmode(GPIO.BCM)


# dcMotor control, just need to test its rotation
def runMotor(stopTime):
    IN1.on()
    IN2.off()
    sleep(stopTime) #????????????

def set_servo_angle(Servo, angle):
	servo_value = (angle - 90) / 90
	Servo.value = servo_value
	print (f"Servo moved to {angle} degrees")
	sleep(1)                                                                       


def test_capture():
    cam = Camera(0)
    cam.init_camera()
    
    labels = cam.load_labels()
    print(labels)   

    inference = cam.capture_and_infer()
    print(inference)
    
    # Clean accepted bottle
    if inference == "Object: PET bottle 1.5L":
        set_servo_angle(rightServo, 180)
        sleep(5)
        set_servo_angle(rightServo, 0)
        sleep(2)

    # Left servo movements
    elif inference == "Object: plastic":
        set_servo_angle(leftServo, 180)
        sleep(5)
        set_servo_angle(leftServo, 0)
        sleep(2)
    elif inference == "Object: glass":
        set_servo_angle(leftServo, 180)
        sleep(5)
        set_servo_angle(leftServo, 0)
        sleep(2)
    elif inference == "Object: Crumpled":
        set_servo_angle(leftServo, 180)
        sleep(5)
        set_servo_angle(leftServo, 0)
        sleep(2)


    # Other prompts
    elif inference == "Object: Capped":
        print("Please uncap your bottle")
    elif inference == "Object: Unclean":
        print("Unclean Input")
    
    
    # Invalid Inputs
    elif inference == "Object: metal":
        print("Invalid Input")
    elif inference == "Object: cardboard_paper":
        print("Invalid Input")
    elif inference == "Object: rock":
        print("Invalid Input")
    elif inference == "Object: trash":
        print("Invalid Input")
    elif inference == "Object: Not 1.5L":
        print("Invalid Input")
    elif inference == "Object: leaf":
        print("Invalid Input")
        
		
    
#-------------------------RUN
try:
	while True:
		# set_servo_angle(leftServo, 0)
		# sleep(2)
		
		# set_servo_angle(leftServo, 90)
		# sleep(2)
		
		# set_servo_angle(leftServo, 180)
		# sleep(2)
		
		# # servo2
		
		# set_servo_angle(rightServo, 0)
		# sleep(2)
		
		# set_servo_angle(rightServo, 90)
		# sleep(2)
		
		# set_servo_angle(rightServo, 180)
		# sleep(2)
		
except KeyboardInterrupt:
	print("Program stopped")

if __name__ == "__main__":
    test_capture()
