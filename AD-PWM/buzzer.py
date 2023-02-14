# File : buzzer.py
# Simple program to play some notes with a buzzer
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 14/2/2023

#Import of libraries
from machine import Pin,PWM
from utime import sleep

#Configuration of the buzzer pin
bz=PWM(Pin(20))

#While statement to play a scale of notes with 1 second of delay
while True:
    bz.freq(1046)#DO
    bz.duty_u16(1000)
    sleep(1)
    
    bz.freq(1175)#RE
    bz.duty_u16(1000)
    sleep(1)
    
    bz.freq(1318)#MI
    bz.duty_u16(1000)
    sleep(1)
    
    bz.freq(1397)#FA
    bz.duty_u16(1000)
    sleep(1)
    
    bz.freq(1568)#SOL
    bz.duty_u16(1000)
    sleep(1)
    
    bz.freq(1760)#LA
    bz.duty_u16(1000)
    sleep(1)
    
    bz.freq(1967)#SI
    bz.duty_u16(1000)
    sleep(1)