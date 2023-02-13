# File : led2.py
# Simple program to turn a led off
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import Pin

#Led pin configuration
led = Pin(16, Pin.OUT)

#Turn the led off
led.value(0)