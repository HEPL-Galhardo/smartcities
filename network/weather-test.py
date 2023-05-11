# File : weather-test.py
# Simple program to connect to wlan and get the weather from an api
# joao.galhardocarraca@student.hepl.be
# 20/04/2023

#-----------------Import of libraries------------------
import network
from utime import sleep
import urequests
from machine import I2C,Pin
from lcd1602 import LCD1602

#-------------------Modules Configurations---------------------
#I2C bus line configuration
i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
#Label data type, number of lines and characters per line
d=LCD1602(i2c,2,16)

#-------------------Variables---------------------
#Setting a special character ° for the temperature degrees
degree=[
    0b00111,
    0b00101,
    0b00111,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,]
#Clearing the display
d.clear()
#Create the special character and save in memory 
d.create_char(0,degree)
d.display() #enable display

#---------------------------------------Wifi Connection-------------------------------------------
#Wifi connection: setting the identifier and the password to the wifi connection
SSID=""
PASSWORD=""
wlan = network.WLAN(network.STA_IF)
#Enabeling the wlan
wlan.active(True)
print("Wifi On, Status:",wlan.status())
#Loop while the wifi connection isn't establissed
while not wlan.isconnected():
    #
    wlan.connect(SSID, PASSWORD) #wlan.connect("secrets.SSID", "secrets.PASSWORD")
    print("Waiting for connection with ",SSID)
    print("Wifi Status:",wlan.status())
    #Checking the connection, if connection jus
    try:
        print("...")
        if wlan.isconnected():
            print("Wifi connection made with ",SSID)
            break
        wlan.connect(SSID, PASSWORD)
        print("Wifi Status:",wlan.status())
        pass
    #If the connection isn't working then re-trying after 1 second
    except:
        print("Wifi connection couldn't be made!, Re-trying...")
        pass
    sleep(1)
#Re-check the connection 
if wlan.isconnected():
    print("Wifi connection made with ",SSID)
#Show the actual connection features
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
print ("Wind speed of Liège",int(weather['wind']['speed']*3.6),"km/h")#3.6 to get the speed in km/h otherwise is in m/s
print ("Sky description of Liège:",weather['weather'][0]['description'])

while True:
    d.clear()#clear display
    d.setCursor(0,0)#Set the cursor to origin
    d.print("City: "+str(weather['name'])+" "+str(weather['sys']['country']))#display City and Country
    d.setCursor(0,1)#Set the cursor to the second line
    d.print("Sky Desc:"+str(weather['weather'][0]['description']))#display Sky description
    sleep(3)
    d.clear()#clear display
    d.setCursor(0,0)#Set the cursor to origin
    d.print("Temp:{:.1f}".format((weather['main']['temp'])-272.15))#display temperature value
    d.write(0)
    d.print("C")
    d.setCursor(0,1)#Set the cursor to the second line
    d.print("Humid:"+str(weather['main']['humidity'])+"%")#display humidity value
    sleep(3)
    d.clear()#clear display
    d.setCursor(0,0)#Set the cursor to origin
    d.print("Pressure:"+str(weather['main']['pressure'])+"mb")#display pressure value
    d.write(0)
    d.print("C")
    d.setCursor(0,1)#Set the cursor to the second line
    d.print("Wind Sp:"+str(int(weather['wind']['speed']*3.6))+"km/h")#display wind speed value
    sleep(3)
