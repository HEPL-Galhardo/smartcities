# File : smart_light.py
# Simple program to display diferent colors with a RGB led
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from ws2812 import WS2812
from utime import sleep
from machine import Pin,I2C,ADC

#Led pin configuration
led=WS2812(18,1)
#Light and sound sensor pin configuration
LS=ADC(0)
SS=ADC(1)

#While statement the read the sensors values, print them and the led who has diferents values for specific cases
while True:
    average=0
    #Get light and sound readings and adapt them to a value to the led
    light=LS.read_u16()/256
    for i in range (1000):
        noise=SS.read_u16()/256
        average+=noise
    noise=average/1000
    print("Light and Noise: ",light,"	",noise)
    if light<80:	#If light sensor is covered then the led shows white color
        led.pixels_fill((255,255,255))
        led.pixels_show()
        sleep(0.1)
    else:
        if noise<25:	#If sound sensor detects noise then the led shows red,green and orange color.
                        #Red for laud sound, orange for medium sound and green for good sound  green
            led.pixels_fill((0,255,0))
            led.pixels_show()
            sleep(1)
        if noise>=25 and noise<50:
            led.pixels_fill((255,255,0))
            led.pixels_show()
            sleep(1)
        if noise>=50:
            led.pixels_fill((255,0,0))
            led.pixels_show()
            sleep(1)