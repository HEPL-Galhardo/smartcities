# File : pir_servo.py
# Simple program to make a turn on a servo motor when motion is deteted
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from machine import Pin
from utime import sleep
from servo import SERVO

#Servo motor and pir pin configuration
servo=SERVO(Pin(20))
pir= Pin(18,Pin.IN)

#While statement to turn one way and to come back to initial position after 10 seconds once there's motion detected
while True:
    if pir.value()==1:
        print('Motion Detected')
        servo.turn(160)
        sleep(10)
        servo.turn(20)