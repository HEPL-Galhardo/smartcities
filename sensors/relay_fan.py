# File : relay_fan.py
# Simple program to control a minifan with a push-button via a relay
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from machine import Pin
from utime import sleep

#Button, Fan and Relay pin configuration
bt=Pin(16, Pin.IN)
relay=Pin(20,Pin.OUT)

#While statemenr set and keep the fan power on
while True:
    fan.value(1)
    #While statement to toggle the relay switch wicht time we push the button
    while bt.value()==1:
        relay.toggle()
        sleep(1)
