# File : servo_.py
# Simple program to turn a servo motor
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from machine import Pin
from utime import sleep
from servo import SERVO

#Servo motor pin configuration
servo=SERVO(Pin(20))

#For statement to turn the servo motor in 2 diferent angles with a delay of 1 second
for i in range(10):
    servo.turn(20)
    sleep(1)
    servo.turn(160)
    sleep(1)