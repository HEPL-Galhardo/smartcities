# File : LCD_hello_world.py
# Simple program to write to an LCD using a library
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 14/2/2023

#Import of libraries
from lcd1602 import LCD1602
from machine import Pin,I2C
from utime import sleep

#I2C bus line configuration
i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
#Label data type, number of lines and characters per line
d=LCD1602(i2c,2,16)


d.display() #enable display
sleep(1)
d.clear()#clear display
d.print("Hello ")#display characters
d.setCursor(0,1)#set display position, row and column start from 0
d.print("World!")