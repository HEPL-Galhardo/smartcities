# File : NTP_time.py
# Simple program to connect to wifi and to publish a string in a server MQTT
# joao.galhardocarraca@student.hepl.be
# 30/04/2023

#Import of libraries
import ntptime
import network
import utime

# Affichage de la date et de l'heure
print(utime.localtime())

# Configuration de la connexion Wi-Fi
SSID="Proximus-Home-50F8"				#Kot: SSID="Proximus-Home-50F8"  PASSWORD="wz92j9eaey3pc"
PASSWORD="wz92j9eaey3pc"
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

# Synchronisation of time and date with a server NTP with the rapsberry
ntptime.settime()

# Show date and time
print(utime.localtime())
