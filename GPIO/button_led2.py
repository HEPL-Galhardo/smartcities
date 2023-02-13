# File : button_led2.py
# Simple program to control a led with a button
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import Pin
from utime import sleep

#Led and button pin configuration
led = Pin(16, Pin.OUT)
bt = Pin(18, Pin.IN)

val=0	#Default boot value

#While statement
while True:
    #If statement to turn led on when the button is pushed with 1 seconds of delay
    if bt.value()==1:
        val+=1
        sleep(1)
    elif val==2:
        val=0
        sleep(1)
    led.value(val)