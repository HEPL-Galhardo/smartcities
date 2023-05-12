/smartcities/sensors/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

## Libraries explanation
### network library
  
  Here is an explanation of the methods of the library used in the code:

  - `network.WLAN()`: This method creates an instance of the WLAN class, which is used to manage Wi-Fi connections. It may take an optional argument that specifies the mode of the WLAN (f.ex: STA or AP mode).

  - `WLAN.active()`: This method is used to activate or deactivate the Wi-Fi interface.

  - `WLAN.connect(ssid, password)`: This method connects the device to a Wi-Fi network with the given SSID and password.

  - `WLAN.ifconfig()`: This method returns the current IP address, subnet mask, gateway, and DNS server settings for the Wi-Fi interface.

  - `WLAN.isconnected()`: This method returns True if the device is currently connected to a Wi-Fi network, and False otherwise.

  - `network.Socket()`: This method creates a new socket object, which is used for network communication using various protocols, such as TCP and UDP.

  - `Socket.bind(address)`: This method binds the socket to a specific IP address and port number.

  - `Socket.accept()`: This method waits for a new incoming connection and returns a new socket object representing the connection.

  - `Socket.recv(bufsize)`: This method receives data from the socket.

  - `Socket.send(bytes)`: This method sends data to the socket.
### urequests library
  Here are some of the methods provided by the urequests library:

  - `urequests.request(method, url, data=None, json=None, headers={}, stream=None)`: This method sends an HTTP request to the specified URL using the specified method (f.ex: GET, POST, PUT, DELETE, etc.). It also takes optional parameters like data, json, headers, and stream to customize the request.

  - `urequests.get(url, **kwargs)`: This method sends an HTTP GET request to the specified URL.

  - `urequests.Response()`: This method creates a new Response object that contains the response data and metadata returned by the server.

  - `Response.text()`: This method returns the response data as a Unicode string.

  - `Response.json()`: This method parses the response data as JSON and returns it as a Python object.
### umqttsimple library
  Here are some of the methods provided by the umqttsimple library:

  - `umqttsimple.MQTTClient(client_id, server, user=None, password=None, port=0, keepalive=0, ssl=False, ssl_params={})`: This method creates an instance of the MQTTClient class, which is used to connect to an MQTT broker. It takes parameters like client_id, server, user, password, port, keepalive, ssl, and ssl_params to configure the connection.

  - `MQTTClient.connect()`: This method connects the client to the MQTT broker.

  - `MQTTClient.disconnect()`: This method disconnects the client from the MQTT broker.

  - `MQTTClient.publish(topic, msg, retain=False, qos=0)`: This method publishes a message to the specified MQTT topic.

  - `MQTTClient.subscribe(topic, qos=0)`: This method subscribes to the specified MQTT topic.

  - `MQTTClient.check_msg()`: This method checks for incoming MQTT messages and processes them.

  - `MQTTClient.wait_msg()`: This method waits for an incoming MQTT message and processes it.

  - `MQTTClient.set_callback(callback)`: This method sets the callback function to be called when an MQTT message is received.
  
### ntptime library
  Here are some of the methods provided by the ntptime library:

  - `ntptime.settime()`: This method sets the system time based on the time obtained from an NTP server. It uses the network library to connect to the NTP server and retrieve the current time. It also update the time and date of the module RTC, the internal clock of the pico.

  - `ntptime.host_to_ip(host)`: This method resolves the IP address of the specified host name using DNS.
  
## Scripts and explanations

* Simple program to connect to wlan and get the weather from an api.

  It is needed an API key from the weather API.
  - [weather-test.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/network/weather-test.py)
  
  - Desmonstration:
    ![wt](https://github.com/HEPL-Galhardo/smartcities/assets/124893862/f5bef73e-0cbe-4cfb-98a1-efb7289ed2eb)
  
    https://github.com/HEPL-Galhardo/smartcities/assets/124893862/c1102eb5-3a07-42bd-9d9c-5d462c3d898a
  
* Simple program to connect to wifi and to publish or subscribe in a MQTT server. 
  
  To test this one, it is needed a MQTT server to connect and the library umqttsimple.py.
  - [wlan_umqtt.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/network/wlan_umqtt.py)
  
  - Desmonstration:
  
    From Raspberry Pico W:
    ![image](https://github.com/HEPL-Galhardo/smartcities/assets/124893862/074f369a-b924-4bab-9b6b-d4c5b4975aa7)
    From MQTT Server:
    ![image](https://github.com/HEPL-Galhardo/smartcities/assets/124893862/f4b1077d-8c2c-4912-bf8d-35fe861303f3)

* Get the to update time of the RTC using NTP.

    This program uses a ntptime.py library that goes get the universal date and time in the internet at UTC +0.
  - [NTP_time.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/network/NTP_time.py)
  
  - Desmonstration:
    ![image](https://github.com/HEPL-Galhardo/smartcities/assets/124893862/fdb82ca0-3335-459f-88f1-88f5fd7cb82b)
    By observing the results, the RTC is updated to with the NTP because we found our selfs in UTC +2 and the results are in UTC +0, so the results needs to be further ajusted before displaying it.


