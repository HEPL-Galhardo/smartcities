/smartcities/LCD/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

* A simple library for the LCD Display
  - [lcd1602.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LCD/lcd1602.py)

* Display a string of charaters on a LCD display
  - LCD display module is wired to the Raspberry Pico W on ***pin I2C1*** (see demo and link below)
  
      ![20230308_091038](https://user-images.githubusercontent.com/124893862/223850877-f353c863-0fbb-4828-8274-06ffe1368471.jpg)

  - [LCD_hello_world.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LCD/LCD_hello_world.py)
  
* Display the value of a rotary sensor on a LCD display
  - LCD display module is wired to the Raspberry Pico W on ***pin I2C1*** and the rotary sensor on ***pin ADC0***(see demo and link below)

      https://user-images.githubusercontent.com/124893862/223851065-52e6908e-083d-44cf-a3fc-2616409e878f.mp4

  - [LCD_knob.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LCD/LCD_knob.py)
  
* Display the value of a rotary sensor on a LCD display and with a fading LED
  - LCD display module is wired to the Raspberry Pico W on ***pin I2C1***, the rotary sensor on pin ***ADC0*** and the LED module on ***pin 16*** (see demo and link below)
  
      https://user-images.githubusercontent.com/124893862/223852078-d91a36e0-eb82-4fe0-b83e-8e177576b117.mp4

  - [LCD_led.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LCD/LCD_led.py)
