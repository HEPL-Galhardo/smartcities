# File : servo_2.py
# Simple program to make a turn on a servo motor
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from machine import Pin
from utime import sleep
from servo import SERVO

#Servo motor and pir pin configuration
servo=SERVO(Pin(20))
a=180

#While statement
while True:
    a=a==0 and 180 or a-1
    servo.turn(a)
    sleep(0.1)