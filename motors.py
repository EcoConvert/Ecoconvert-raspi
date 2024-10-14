from gpiozero import PMWOutputDevice, DigitalOutputDevice
from time import sleep

motor_forward = DigitalOutputDevice(17) # IN1
motor_backward = DigitalOutput(27) # IN2
motor_speed = PMWOutputDevice(18) # ENA

def move_motor(direction, speed, duration)
	if direction == "forwar":
		motor_forward.on()
		motor_backward.off()
	elif direction == "backward":
		motor_forward.off()
		motor_backward.on()
		
	motor_speed.value = speed
	sleep(duration)
	
	
	motor_forward.off()
	motor_backward.off()
	motor_speed.off()
	
try:
	while True:
	
	print("Motor running forward at 100% speed")
	move_motor("forward", 1.0,3)
	
	print(Motor running backward at 50% speed")
	move_motor("backward", 0.5, 3)
	
	sleep(2)
	
	
except KeyboardInterrupt:
	print("Motor control stopped")
	motor_forward.off()
	motor_backward.off()
	motor_speed.off()
