# File : rgb_led.py
# Simple program to display diferent colors with a RGB led
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 18/2/2023

#Import of libraries
from ws2812 import WS2812
from utime import sleep

#Setting colors tupples
black=(0,0,0)
red=(255,0,0)
yellow=(255,150,0)
green=(0,255,0)
cyan=(0,255,255)
blue=(0,0,255)
purple=(180,0,255)
white=(255,255,255)
colors=(black,red,yellow,green,cyan,blue,purple,white)

#RGB Led pin configuration
led=WS2812(18,1)	#WS2812(pin_num,led_count)

#While statement to show the diferent colors throw the led with a delay os 0.2 seconds
while True:
    for color in colors:
        led.pixels_fill(color)
        led.pixels_show()
        sleep(0.2)
