# File : wlan_umqtt.py
# Simple program to connect to wifi and to publish a string in a server MQTT
# joao.galhardocarraca@student.hepl.be
# 30/04/2023

#Import of libraries
from umqttsimple import MQTTClient
import network
from utime import sleep
import urequests

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
        pass
    #If the connection isn't working then re-trying after 1 second
    except:
        print("Wifi connection couldn't be made!, Re-trying...")
        pass
    sleep(1)
#Re-check the connection 
if wlan.isconnected():
    print("Wifi connection made with ",SSID)

print("IP Adresse informations: ",wlan.ifconfig())

#création de l'objet client
monClientMqtt = umqttsimple.MQTTClient(client_id=b"pico",server=b"192.168.2.131",port=1883)
#connexion au serveur
monClientMqtt.connect()
#envoi d'un message vers le serveur (topic, message)
monClientMqtt.publish("testTopic","Hello de mon Pico 2W!")
