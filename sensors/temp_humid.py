# File : temp_humid.py
# Simple program to write to an LCD the value of a temperature and humidity sensor
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 15/2/2023

#Import of libraries
from lcd1602 import LCD1602
from dht11 import *
from machine import Pin,I2C,ADC
from utime import sleep

#I2C bus line configuration
i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
#Label data type, number of lines and characters per line
d=LCD1602(i2c,2,16)
#DHT sensor pin configuration
dht=DHT(18)

d.display() #enable display

#While statement to print the value of the rotary buttton to the LCD
while True:
    temp, humid=dht.readTempHumid()#Get the value of temperature and humidity
    d.clear()#clear display
    d.setCursor(0,0)#Set the cursor to origin
    d.print("Temp: "+str(temp))#display temperature value
    d.setCursor(0,1)#Set the cursor to second line
    d.print("Humid: "+str(humid))#display temperature value
    sleep(1)#1 second delay between readings


