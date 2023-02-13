# File : while_blink.py
# Simple program to blink a led
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import Pin
from utime import sleep

#Led pin configuration
led = Pin(16, Pin.OUT)

#While statement togles of the led
while True:
    led.value(1)	#Led on
    sleep(1)	#Wait for 1 second
    led.value(0)	#Led off
    sleep(1)