# File : LCD_temp_humid_time.py
# Simple program to control a led with a button via an interrupt
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 08/03/2023

#Import of libraries
from machine import Pin
from lcd1602 import LCD1602
from dht11 import *
from machine import Pin,I2C,ADC,PWM,RTC
from utime import sleep


#I2C bus line configuration
i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
#Label data type, number of lines and characters per line
d=LCD1602(i2c,2,16)
#DHT sensor pin configuration
dht=DHT(16)
rtc=RTC()

#Bit configuration of a new charater
degree=[
    0b00111,
    0b00101,
    0b00111,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,]

d.clear()
#Creation of a new charater at the placement 0
d.create_char(0,degree)
d.display() #enable display


while True:
    temp, humid=dht.readTempHumid()#Get the value of temperature and humidity
    dt=rtc.datetime()#Get the date and time from the uC
    d.clear()#clear display
    d.setCursor(0,0)#Set the cursor to origin
    d.print("Temp:{:.1f}".format(temp))#display temperature value
    d.write(0)
    d.print("C")
    d.setCursor(11,1)#Set the cursor to origin
    d.print("{:2d}:{:02}".format(dt[4],dt[5]))#display temperature value
    d.setCursor(0,1)#Set the cursor to second line
    d.print("Humid:"+str(humid))#display temperature value
    d.setCursor(8,0)#Set the cursor to origin
    sleep(1)#1 second delay between readings

