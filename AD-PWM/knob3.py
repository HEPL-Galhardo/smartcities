# File : knob3.py
# Simple program to control a led with a rotary sensor button
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import ADC,Pin
from utime import sleep

# Led and rotary sensor pin configuration
led=Pin(16, Pin.OUT)
rotary=ADC(0)

#While statement
while True:
    print("Rotary: ",rotary.read_u16())
    #If statement to turn th led on at a certain value
    if 20000<rotary.read_u16() and rotary.read_u16()<40000:
        led.value(1)
        sleep(1)
    else:
        led.value(0)
        sleep(1)