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


