/smartcities/LED_neo/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

## Library explanation

  ldc1602.py is a  library for Micropython that defines a class named LCD1602, and contains several methods that represent commands that can be sent to a 16x2 character LCD (liquid crystal display) using an I2C interface.

  Here is a brief explanation of each method:

  - `__init__`(self, pin_num, led_count, brightness = 0.5): is the constructor method of the class. It initializes the object with the number of display lines, number of LEDs on the strip and a default brightness.

  - `pixels_show`(self): This method clears the display and sets the cursor position to zero.

  - `pixles_set`(self, i, color): This method sets a color position to zero.

  - `pixels_fill`(self, color): This method sets the cursor position to the specified column and row.

  - `color_chase`(self,color, wait): This method turns off the display.
display
  - `wheel`(self, pos): This method ...

  - `rainbow_cycle`(self, wait): This method ...

## Scripts and explanations

* A simple library for the LED_neo strip
  - [ws2812.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LED_neo/ws2812.py)

* Display a different colors with 1/5th seconds delay on a LED_neo module
  - LED_neo module is wired to the Raspberry Pico W on ***pin 18*** (see demo and link below)

    https://user-images.githubusercontent.com/124893862/223852508-e818ac18-6ae0-4df2-983e-8975a762a297.mp4


  - [rgb_led.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LED_neo/rgb_led.py)
  
* Different types of funtions to display colors with 1/5th seconds delay on a LED_neo module
  - LED_neo module is wired to the Raspberry Pico W on ***pin 18*** (see demo and link below)
      
   

    https://user-images.githubusercontent.com/124893862/223853184-3c58b948-df81-4057-aa03-8dc14dec2703.mp4



  - [rgb_leds.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LED_neo/rgb_leds.py)
  
* Display a different colors on a LED_neo module according to a light and sound sensor
  - LED_neo module is wired to the Raspberry Pico W on ***pin 18***, the light sensor to ***pin ADC0*** and the sound sensor to the ***pin ADC1*** (see demo and link below)
    - If there's light then the led displays white, if the noise is too laud then the led displays red, for medium noise orange light and for low noise green light.
      
     https://user-images.githubusercontent.com/124893862/223853127-7a461918-a458-4cc4-bf53-fdc41bb72782.mp4

  - [smart_light.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/LED_neo/smart_light.py)
