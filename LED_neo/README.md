/smartcities/LED_neo/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

* Display a different colors with 1/5th seconds delay on a LED_neo module
  - LED_neo module is wired to the Raspberry Pico W on ***pin 18*** (see demo and link below)
      [PHOTO DEMO]
  - [rgb_led.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LED_neo/rgb_led.py)
  
* Different types of funtionto display colors with 1/5th seconds delay on a LED_neo module
  - LED_neo module is wired to the Raspberry Pico W on ***pin 18*** (see demo and link below)
      [PHOTO DEMO]
  - [rgb_leds.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LED_neo/rgb_leds.py)
  
* Display a different colors on a LED_neo module according to a light and sound sensor
  - LED_neo module is wired to the Raspberry Pico W on ***pin 18***, the light sensor to ***pin ADC0*** and the sound sensor to the ***pin ADC1*** (see demo and link below)
    - If there's light then the led displays white, if the noise is too laud then the led displays red, for medium noise orange light and for low noise green light.
      [PHOTO DEMO]
  - [smart_light.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LED_neo/smart_light.py)
