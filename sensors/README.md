/smartcities/sensors/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

* A Buzzer simple library to play a note from 0 to 7 with a delay of choise
  - [buzzer.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/buzzer.py)
  
* Play a Jingle bells on a buzzer module using a simple self-created  adaptive PWM library
  - A Buzzer module is wired to the Raspberry Pico W on ***pin 27 or ADC1*** (see demo and link below)
      [PHOTO DEMO]
  - [buzzer_lib.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/buzzer_lib.py)
  
* Turn on and off a minifan with a button module
  - The minifan module is wired to the Raspberry Pico W on ***pin 18*** and the button module to the  ***pin 16***(see demo and link below)
      [PHOTO DEMO]
  - [minifan.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/minifan.py)

* Turn on and off a minifan using a button module with a relay
  - The minifan module is wired to the Raspberry Pico W on ***pin 18***, the button module to the  ***pin 16*** and the relay to the ***pin 20***(see demo and link below)
      [PHOTO DEMO]
  - [relay_fan.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/relay_fan.py)
  
 * Servo-motor simple library PWM controler
    - [servo.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/servo.py)
  
 * Turn a servo-motor between 2 different angles 10 times with a 1 second of delay
    - The servo-motor module is wired to the Raspberry Pico W on ***pin 20***(see demo and link below)
      [PHOTO DEMO]
    - [servo_.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/servo_.py)
  
 * Turn a servo-motor in an infite loop, 1° each 1/10th of a second
    - The servo-motor module is wired to the Raspberry Pico W on ***pin 20***(see demo and link below)
      [PHOTO DEMO]
    - [servo_2.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/servo_2.py)
  
 * Turn a servo-motor to open a door each time motion is detected
    - The servo-motor module is wired to the Raspberry Pico W on ***pin 20*** and the PIR sensor module to the ***pin 18***(see demo and link below)
      [PHOTO DEMO]
    - [pir_servo.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/pir_servo.py)
  
 * Display the temperature and humidity on a LCD display each second
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16*** and the DHT sensor module to the ***pin 18***(see demo and link below)
      [PHOTO DEMO]
    - [temp_humid.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/temp_humid.py)
  
 * Display the temperature and humidity on a LCD display each second and play an alarm for the worst readings conditions
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16***, the DHT sensor module to the ***pin 18*** and the buzzer module to the ***pin 20***(see demo and link below)
      [PHOTO DEMO]
    - [temp_humid_alarm.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/temp_humid_alarm.py)
  
 * Display the temperature on a LCD display each second and turn on the minifan if it is too hot
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16***, the DHT sensor module to the ***pin 18*** and the minifan module to the ***pin 20***(see demo and link below)
      [PHOTO DEMO]
    - [temp_minifan.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/temp_minifan.py)
  
 * Display of "WELCOME" on a LCD display, open a door with a servo-motor and play a song each time a passenger triggers the motion sensor
    - The LCD display module is wired to the Raspberry Pico W on ***pin 16***, the servo-motor to the ***pin 20***, the buzzer module to the ***pin 27*** and the PIR sensor module toe the ***pin 18***(see demo and link below)
      [PHOTO DEMO]
    - [welcome.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/sensors/welcome.py)
