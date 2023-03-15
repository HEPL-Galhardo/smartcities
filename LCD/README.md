/smartcities/LCD/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

## Library explanation

  This is a  library for Micropython that defines a class named LCD1602, and contains several methods that represent commands that can be sent to a 16x2 character LCD (liquid crystal display) using an I2C interface.

  Here is a brief explanation of each method:

  - `__init__`(self, i2c, lines, dotsize, lcd_addr=0x3E): is the constructor method of the class. It initializes the object with the I2C interface, number of display lines, dot size, and LCD address.

  - `clear`(self): This method clears the display and sets the cursor position to zero.

  - `home`(self): This method sets the cursor position to zero.

  - `setCursor`(self, col, row): This method sets the cursor position to the specified column and row.

  - `no_display`(self): This method turns off the display.
display
  - `display`(self): This method turns on the display.

  - `no_cursor`(self): This method turns off the underline cursor.

  - ´cursor´(self): This method turns on the underline cursor.

  - `no_blink`(self): This method turns off the blinking cursor.

  - `blink`(self): This method turns on the blinking cursor.

  - `autoscroll`(self): This method allows text to be scrolled automatically.
  
  - ``no_autoscroll(self): This method allows text to stay put or fixed automatically.

  - `createChar`(self, location, charmap): This method creates a new custom character at the specified location.

  - `command`(self, command): This method sends a command to the LCD.

  - `write`(self, command): This method writes the commands to the LCD.

  - `print`(self, text): This method sends a string of characters to the LCD.

## Scripts and explanations

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
