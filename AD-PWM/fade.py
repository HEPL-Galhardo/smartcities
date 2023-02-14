# File : fade.py
# Simple program to fade a led power
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import Pin,PWM
from utime import sleep_ms

# Led and rotary sensor pin configuration
led=PWM(Pin(16))

#Default boot values
val=0
led.freq(500)	#Default boot PWM frequency

#While Statement to change the frequency of the PWM
while True:
    while val<65535:
        val+=50
        sleep_ms(1)
        led.duty_u16(val)
    while val>0:
        val-=50
        sleep_ms(1)
        led.duty_u16(val)