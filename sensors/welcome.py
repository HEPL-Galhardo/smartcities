# File : welcome.py
# Simple program to play Jingle Bells throw a buzzer
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from machine import Pin,PWM,I2C
from lcd1602 import LCD1602
from utime import sleep
from buzzer import Music
from servo import SERVO


#I2C bus line configuration
i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
#Label data type, number of lines and characters per line
d=LCD1602(i2c,2,16)
#Buzzer, Servo Motor, pir: pin configuration
servo=SERVO(Pin(20))
pwm=PWM(Pin(27))
mu=Music(pwm)
pir= Pin(18,Pin.IN)

#While statement to play a music, show a message on the LCD and open a door when motion detected
while True:
    if pir.value()==1:
        print('Motion Detected')
        servo.turn(180)
        d.display()
        sleep(1)
        d.clear()
        d.print('Welcome')
        
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
        
        servo.turn(0)
