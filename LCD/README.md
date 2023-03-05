/smartcities/LCD/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

* Display a string of charaters on a LCD display
  - LCD display module is wired to the Raspberry Pico W on ***pin I2C1*** (see demo and link below)
      [PHOTO DEMO]
  - [LCD_hello_world.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LCD/LCD_hello_world.py)
  
* Display the value of a rotary sensor on a LCD display
  - LCD display module is wired to the Raspberry Pico W on ***pin I2C1*** and the rotary sensor on pin ADC0(see demo and link below)
      [PHOTO DEMO]
  - [LCD_knob.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LCD/LCD_knob.py)
  
* Display the value of a rotary sensor on a LCD display and with a fading LED
  - LCD display module is wired to the Raspberry Pico W on ***pin I2C1***, the rotary sensor on pin ***ADC0*** and the LED module on ***pin 16*** (see demo and link below)
      [PHOTO DEMO]
  - [LCD_led.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LCD/LCD_led.py)
