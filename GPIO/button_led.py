# File : button_led.py
# Simple program to control a led with a button
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import Pin

#Led and button pin configuration
led = Pin(16, Pin.OUT)
bt = Pin(18, Pin.IN)

#While statement
while True:
    val=bt.value()	#Readings of the button
    #If statement to turn led on when the button is pushed
    if val==1:
        led.value(1)
    else:
        led.value(0)