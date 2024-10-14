import RPi.GPIO as GPIO
from modules.Camera import Camera
from gpiozero import Servo
from time import sleep

# Instances
leftServo = Servo(18)
rightServo = Servo(26)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)  # Set GPIO 5 as input to detect the parameter

hx = HX711(dout_pin=6, pd_sck_pin=5)

def set_servo_angle(servo, angle):
    servo_value = (angle - 90) / 90
    servo.value = servo_value
    print(f"Servo moved to {angle} degrees")
    sleep(1)

def test_capture():
    cam = Camera(0)
    cam.init_camera()
    
    labels = cam.load_labels()
    print(labels)

    inference = cam.capture_and_infer()
    print(inference)

    if inference == "Object: plastic":
        set_servo_angle(leftServo, 0)
        sleep(2)
    elif inference == "Object: glass":
        set_servo_angle(leftServo, 90)
        sleep(2)
    elif inference == "Object: metal":
        set_servo_angle(leftServo, 180)
        sleep(2)
    # Add other inferences as needed
    elif inference == "Object: leaf":
        set_servo_angle(rightServo, 90)
        sleep(2)

#-------------------------RUN
try:
    while True:
        reading = hx.get_raw_data_mean()
        print(reading)

        # Check if the specific parameter is detected on GPIO 5
        if GPIO.input(5) == GPIO.HIGH:  # Parameter detected
            print("Parameter detected on GPIO 5")
            
            # Run the test_capture function to infer object and move the servo
            test_capture()
        else:
            print("No parameter detected on GPIO 5")
            sleep(1)

except KeyboardInterrupt:
    print("Program stopped")
finally:
    GPIO.cleanup()  # Clean up the GPIO pins when exiting
