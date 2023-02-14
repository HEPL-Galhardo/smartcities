# File : knob_led.py
# Simple program to control the PWM frequency of a led with a rotary sensor button
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import ADC,Pin,PWM

# Led and rotary sensor pin configuration
led=PWM(Pin(16))
rotary=ADC(0)

led.freq(500)	#Default boot PWM frequency

#While Statement to change the frequency of the PWM with rotary sensor
while True:
    val=rotary.read_u16()
    led.duty_u16(val)