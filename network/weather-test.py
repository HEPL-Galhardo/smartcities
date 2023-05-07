# File : weather-test.py
# Simple program to connect to wlan and get the weather from an api
# joao.galhardocarraca@student.hepl.be
# 28/03/2023

#Import of libraries
import network
from utime import sleep
import urequests
from machine import I2C,Pin
from lcd1602 import LCD1602

#I2C bus line configuration
i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
#Label data type, number of lines and characters per line
d=LCD1602(i2c,2,16)


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
d.create_char(0,degree)
d.display() #enable display
d.autoscroll()

#Wifi connection
SSID=""
PASSWORD=""
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print("Wifi On:",wlan.status())


while not wlan.isconnected():
    wlan.connect(SSID, PASSWORD) #wlan.connect("secrets.SSID", "secrets.PASSWORD")
    print("Waiting for connection with ",SSID)
    try:
        print("...")
        if wlan.isconnected():
            print("Wifi connection made with ",SSID)
            break
        wlan.connect(SSID, PASSWORD)
        pass
    except:
        print("Wifi connection couldn't be made!, Re-trying...")
        pass
    sleep(1)
if wlan.isconnected():
    print("Wifi connection made with ",SSID)

print("IP Adresse informations: ",wlan.ifconfig())

#Reaching openweather site to get the weather from Liege
weather = urequests.get("https://api.openweathermap.org/data/2.5/weather?q=Liège,BE&appid=13a95c0ef51beac263b0f855decf5963").json()
#print (weather)
#Transform the json file into a dictionary to access objets in the file with micropython
weather=dict(weather)
print ("Temperature of Liège",(weather['main']['temp'])-272.15,"°C")#-272.15 to get the temperature in °C otherwise is in K(kelvin)
print ("Temperature feels like of Liège",(weather['main']['feels_like'])-272.15,"°C")
print ("Temperature maximal of Liège",(weather['main']['temp_max'])-272.15,"°C")
print ("Temperature minimal of Liège",(weather['main']['temp_min'])-272.15,"°C")

print ("Humidity of Liège",weather['main']['humidity'],"%")
print ("Pressure of Liège",weather['main']['pressure'],"mb")
print ("Wind speed of Liège",weather['wind']['speed']*3.6,"km/h")#3.6 to get the speed in km/h otherwise is in m/s
print ("Sky description of Liège:",weather['weather'][0]['description'])

while True:
    #d.clear()#clear display
    d.setCursor(0,0)#Set the cursor to origin
    d.print("Temp:{:.1f}".format((weather['main']['temp'])-272.15))#display temperature value
    
    d.write(0)
    d.print("C")

    d.setCursor(16,1)#Set the cursor to origin
    
    sleep(0.5)
