# File : blink.py
# Simple program to blink a led 10 times
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import Pin
import utime

#Led pin configuration
led = Pin(16, Pin.OUT)

#For statement to 10 togles of the led
for i in range (10):
    led.value(1)	#Led on
    sleep(1)	#Wait for 1 second
    led.value(0)	#Led off
    sleep(1)