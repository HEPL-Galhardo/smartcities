# File : button_led_int.py
# Simple program to control a led with a button via an interrupt
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 08/03/2023

#Import of libraries
from machine import Pin

#Led and button pin configuration
led = Pin(16, Pin.OUT)
bt = Pin(18, Pin.IN)

def interrupt():
    led.toggle

bt.irq(trigger=Pin.IRQ_RISING, handler=interrupt)

#While statement
while True:
    pass