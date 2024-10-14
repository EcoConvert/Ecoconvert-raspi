import os 
import time 
import logging
from modules.Led import Led
from gpiozero import LED 

led = LED(21)
def blink() -> None: 
	
	#led.On()
	led.on()
	logging.info("LED on")
	time.sleep(8)

	#led.Off()
	led.off()
	logging.info("LED off")
	time.sleep(.5)


if __name__ == "__main__": 
	blink()
