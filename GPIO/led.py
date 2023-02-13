# File : led.py
# Simple program to turn a led on
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 13/2/2023

#Import of libraries
from machine import Pin
from utime import sleep

# Led pin configuration
led = Pin(16, Pin.OUT)

#Turn the led on
led.value(1)