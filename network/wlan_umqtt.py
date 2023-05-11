# File : wlan_umqtt.py
# Simple program to connect to wifi and to publish or subscribe in a MQTT server 
# joao.galhardocarraca@student.hepl.be
# 30/04/2023

#####Import of libraries######
from umqttsimple import MQTTClient
import network
from utime import sleep
import urequests

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print(topic.decode(), msg.decode())
    
#---------------------------------------Wifi Connection-------------------------------------------
#Wifi connection: setting the identifier and the password to the wifi connection
SSID="Android Galhardo"				#Kot: SSID="Proximus-Home-50F8"  PASSWORD="wz92j9eaey3pc"
PASSWORD="Galhardo1996"				#HEPL: SSID="electroProjectWifi"  PASSWORD="M13#MRSE"
wlan = network.WLAN(network.STA_IF)
#Enabeling the wlan
wlan.active(True)
print("Wifi On, Status:",wlan.status())
#Loop while the wifi connection isn't establissed
while not wlan.isconnected():
    wlan.connect(SSID, PASSWORD) #wlan.connect("secrets.SSID", "secrets.PASSWORD")
    print("Waiting for connection with ",SSID)
    print("Wifi Status:",wlan.status())
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

#---------------------------------------MQTT Server Connection-------------------------------------------
#Connection to the server MQTT
print('Authetification for the connecting to MQTT Broker')
monClientMqtt = MQTTClient(client_id="PicoIoT", #Tritan: picow			#Notre: PicoIoT , PicoIoT1
                    server=b"3715debebfa546d29fddbf13ddd328f1.s2.eu.hivemq.cloud",   
                    port=8883, 
                    user= "PicoIoT", 
                    password="PicoIoT1234", #Tritan: Azertyuiop1			#Notre: PicoIoT1234
                    keepalive=7200,
                    ssl=True,
                    ssl_params={'server_hostname':'3715debebfa546d29fddbf13ddd328f1.s2.eu.hivemq.cloud'})
#Tritan: c0deea5d7e584e5fadc9488cba7cb0bf.s2.eu.hivemq.cloud			#Notre: 3715debebfa546d29fddbf13ddd328f1.s2.eu.hivemq.cloud
sleep(1)

#Connection to the server MQTT
print("Connection to the MQTT server")
monClientMqtt.connect()
print("Fonction Callback MQTT")
monClientMqtt.set_callback(sub_cb)

#----------Publishing--------------
#print("Envoi d'un message au serveur MQTT")
#monClientMqtt.publish(b"Topic",b"HellodemonPico2W!")

#----------Subscrition--------------
print("Subscrition to a topic in the MQTT server")
monClientMqtt.subscribe("Test")

while True:
    
    # Non-blocking wait for message
    print("Checking for message from the MQTT server")
    monClientMqtt.check_msg()
       
    # Then need to sleep to avoid 100% CPU usage (in a real
    # app other useful actions would be performed instead)
    sleep(3)
    print("Publishing a message to the MQTT server")
    monClientMqtt.publish(b"Topic",b"Message")
