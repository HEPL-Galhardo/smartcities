/smartcities/sensors/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

## Library explanation
### wlan and requests library
  
  Here is an explanation of the different parts of the code:

  - `__init__`(self,pwm_pin): .....
  
## Scripts and explanations

* Simple program to connect to wlan and get the weather from an api.

  It is needed an API key from the weather API.
  - [weather-test.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/network/weather-test.py)
  
  - Desmonstration:
  ![wt](https://github.com/HEPL-Galhardo/smartcities/assets/124893862/f5bef73e-0cbe-4cfb-98a1-efb7289ed2eb)
  
  +VIDEO DEMO
  
* Simple program to connect to wifi and to publish or subscribe in a MQTT server. 
  
  To test this one, it is needed a MQTT server to connect and the library umqttsimple.py.
  - [wlan_umqtt.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/network/wlan_umqtt.py)
  
  - Desmonstration:
   + PHOTO DEMO
* Get the to update time of the RTC using NTP.

    This program uses a ntptime.py library that goes get the universal date and time in the internet at UTC +0.
  - [NTP_time.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/network/NTP_time.py)
  
  - Desmonstration:
  + PHOTO DEMO IN INGLISH
 
    ![NTP_time](https://github.com/HEPL-Galhardo/smartcities/assets/124893862/3471b8ac-f0d0-4719-b702-43e02689d385)
    By observing the results, the RTC is updated to with the NTP because we found our selfs in UTC +2 and the results are in UTC +0, so the results needs to be further ajusted before displaying it.


