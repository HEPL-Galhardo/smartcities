/smartcities/sensors/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

* A Buzzer simple library to play a note from 0 to 7 with a delay of choise
  - [buzzer.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/buzzer.py)
  
* Play a Jingle bells on a buzzer module using a simple self-created  adaptive PWM library
  - A Buzzer module is wired to the Raspberry Pico W on ***pin 27 or ADC1*** (see demo and link below)
      ![20230308_085812](https://user-images.githubusercontent.com/124893862/223853713-32c86030-e12c-49dc-a3f9-6ff33074a87a.jpg)

  - [buzzer_lib.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/buzzer_lib.py)
  
* Turn on and off a minifan with a button module
  - The minifan module is wired to the Raspberry Pico W on ***pin 18*** and the button module to the  ***pin 16***(see demo and link below)

      https://user-images.githubusercontent.com/124893862/223853895-9e3d16bb-44ac-457e-a612-5b78a985bff7.mp4

  - [minifan.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/minifan.py)

* Turn on and off a minifan using a button module with a relay
  - The minifan module is wired to the Raspberry Pico W on ***pin 18***, the button module to the  ***pin 16*** and the relay to the ***pin 20***(see demo and link below)

      https://user-images.githubusercontent.com/124893862/223854010-4d6051f4-d1d7-4c9f-9023-fbb8d9890d72.mp4

  - [relay_fan.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/relay_fan.py)
  
 * Servo-motor simple library PWM controler
    - [servo.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/servo.py)
  
 * Turn a servo-motor between 2 different angles 10 times with a 1 second of delay
    - The servo-motor module is wired to the Raspberry Pico W on ***pin 20***(see demo and link below)
       https://user-images.githubusercontent.com/124893862/223854131-1845e0b7-acc1-425e-a70f-0460d1e8579a.mp4
    - [servo_.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/servo_.py)
  
 * Turn a servo-motor in an infite loop, 1° each 1/10th of a second
    - The servo-motor module is wired to the Raspberry Pico W on ***pin 20***(see demo and link below)
     
        https://user-images.githubusercontent.com/124893862/223854307-995a09fc-c21c-4c93-989f-b27a4d6652ad.mp4

    - [servo_2.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/servo_2.py)
  
 * Turn a servo-motor to open a door each time motion is detected
    - The servo-motor module is wired to the Raspberry Pico W on ***pin 20*** and the PIR sensor module to the ***pin 18***(see demo and link below)
      [PHOTO DEMO]
    - [pir_servo.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/pir_servo.py)
  
 * Display the temperature and humidity on a LCD display each second
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16*** and the DHT sensor module to the ***pin 18***(see demo and link below)
    
      ![20230308_100602](https://user-images.githubusercontent.com/124893862/223855002-ff5b7782-832a-4c94-9a41-fe12dfcaf10b.jpg)

    - [temp_humid.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/temp_humid.py)
  
 * Display the temperature and humidity on a LCD display each second and play an alarm for the worst readings conditions
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16***, the DHT sensor module to the ***pin 18*** and the buzzer module to the ***pin 20***(see demo and link below)
    
      ![20230308_100853](https://user-images.githubusercontent.com/124893862/223855083-4d0b2cde-769f-4030-96e2-32e32ead4160.jpg)

    - [temp_humid_alarm.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/temp_humid_alarm.py)
  
 * Display the temperature on a LCD display each second and turn on the minifan if it is too hot
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16***, the DHT sensor module to the ***pin 18*** and the minifan module to the ***pin 20***(see demo and link below)
    
      ![20230308_101131](https://user-images.githubusercontent.com/124893862/223855145-9501aaa1-3449-4d8e-98df-80de940689d7.jpg)

    - [temp_minifan.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/temp_minifan.py)
  
 * Display of "WELCOME" on a LCD display, open a door with a servo-motor and play a song each time a passenger triggers the motion sensor
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16***, the servo-motor to the ***pin 20***, the buzzer module to the ***pin 27*** and the PIR sensor module toe the ***pin 18***(see demo and link below)

      https://user-images.githubusercontent.com/124893862/223855291-2e363788-d05d-4d8b-bf0e-35af061089de.mp4

    - [welcome.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/welcome.py)
    
 * Display the temperature humidity and time on a LCD display each second 
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16***, the DHT sensor module to the ***pin 18*** and the minifan module to the ***pin 20***(see demo and link below)
    
      https://user-images.githubusercontent.com/124893862/223855671-1dcd6c59-44c3-4e95-ad32-6c83b0936422.mp4

    - [meteo_time.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/meteo_time.py)
