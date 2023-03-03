# File : temp_minifan.py
# Simple program to control a minifan with the value of the temperature
#and to display it on a LCD
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

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
dht=DHT(16)

d.display() #enable display

#Minifan pin configuration
minifan=machine.Pin(18,macine.Pin.OUT)

#While statement to turn the fan on when the button is pushed
while True:
    temp=dht.readTemperature()#Get the value of temperature and humidity
    d.clear()#clear display
    d.setCursor(0,0)#Set the cursor to origin
    d.print("Temp: "+str(temp))#display temperature value
    sleep(1)#1 second delay between readings
    if temp>26:	#If temperature is higher than 26°C then fan on
        minifan.value(1)
    else:	#else fan off
        minifan.value(0)