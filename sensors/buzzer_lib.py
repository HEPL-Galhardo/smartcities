# File : buzzer_lib.py
# Simple program to play Jingle Bells throw a buzzer
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from machine import Pin,PWM
from utime import sleep
from buzzer import Music

#Buzzer pin configuration
pwm=PWM(Pin(27))
mu=Music(pwm)

#While statement to play a music in a loop
while True:
    mu.music(4)
    sleep(0.25)
    mu.music(0)
    sleep(0.1)
    mu.music(4)
    sleep(0.25)
    mu.music(0)
    sleep(0.1)
    mu.music(4)
    sleep(0.5)
    mu.music(0)
    sleep(0.1)
    
    mu.music(4)
    sleep(0.25)
    mu.music(0)
    sleep(0.1)
    mu.music(4)
    sleep(0.25)
    mu.music(0)
    sleep(0.1)
    mu.music(4)
    sleep(0.5)
    mu.music(0)
    sleep(0.1)
    
    mu.music(4)
    sleep(0.25)
    mu.music(6)
    sleep(0.25)
    mu.music(2)
    sleep(0.35)
    mu.music(3)
    sleep(0.15)
    mu.music(4)
    sleep(0.1)
    mu.music(0)
    sleep(0.1)