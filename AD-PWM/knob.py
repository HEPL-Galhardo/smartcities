# File : knob.py
# Simple program to control a led with a button
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import ADC, Pin
from utime import sleep

# Led and rotary sensor pin configuration
led=Pin(16, Pin.OUT)
rotary=ADC(0)

#While statement
while True:
    print("Rotary: ",rotary.read_u16())
    sleep(1)