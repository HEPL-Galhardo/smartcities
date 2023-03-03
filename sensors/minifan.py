# File : minifan.py
# Simple program to control a minifan with a push-button
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from machine import Pin
from utime import sleep_ms

#Button and minifan pin configuration
bt=machine.Pin(16,machine.Pin.IN)
minifan=machine.Pin(18,macine.Pin.OUT)

val=0	#Default boot value

#While statement to turn the fan on when the button is pushed
while True:
    val=bt.value()	#Get the button readings
    if val==1:	#If pushed fan on
        minifan.value(1)
    else:	#else fan off
        minifan.value(0)
        
        
# #While statement to toggle the power of the fan when the button is pushed        
# while True:
#     val=bt.value()	#Get the button readings
#     if val==1:	#If pushed fan toggle for 100ms
#         minifan.toggle()
#         sleep_ms(100)      
