#!usr/bin/python3
#Led.py
import time
from gpiozero import LED 


class Led: 
	def __init__(self, gpio_num: int):
		self.pin = LED(gpio_num) 

	def On(self) -> None:
		try: 
			self.pin.on()
		except KeyboardInterrupt:
			print("ending the program") # always have except interrupts because gpiozero cleans up on exceptions 
	def Off(self) ->None:
		try: 
			self.pin.off()
		except KeyboardInterrupt:
			print("ending the program")# gpiozero cleans up gpio ports on exceptions 

