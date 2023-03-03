# File : LCD_led.py
# Simple program to write to an LCD the value of a rotary button and to change the led light intensity
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 15/2/2023

#Import of libraries
from lcd1602 import LCD1602
from machine import Pin,I2C,ADC,PWM
from utime import sleep

#I2C bus line configuration
i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
#Label data type, number of lines and characters per line
d=LCD1602(i2c,2,16)
#Rotary button and led configuration
led=PWM(Pin(16))
led.freq(500)#Setting PWM frequency
rotary=ADC(0)

d.display() #enable display

#While statement to print the value of the rotary buttton to the LCD
while True:
    val=rotary.read_u16()#Get the value of rotary button
    led.duty_u16(val)
    d.clear()#clear display
    d.setCursor(0,0)#Set the cursor to origin
    d.print("Rotary: "+str(val))#display value
    sleep(1)#1 second delay between readings

