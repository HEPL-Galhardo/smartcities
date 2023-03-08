/smartcities/GPIO/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

## Syntax implemented in

 The `machine` class is a built-in class in MicroPython that provides functionalities to access the hardware resources of the microcontroller on which MicroPython is running. This class is mainly used to perform I/O (input/output) operations such as reading and writing to GPIO pins, managing hardware interrupts, putting the microcontroller to sleep, and controlling the clock.

Here are some of the important features of the 'machine' class:

  - `Pin`: This  class in MicroPython is used for controlling the General-Purpose Input/Output (GPIO) pins of the microcontroller. The GPIO pins can be configured as either inputs or outputs, allowing you to read external signals or control external devices such as LEDs, motors, sensors, and more. The "Pin" class provides several functions to control the behavior of the GPIO pins. Here are some of the important functions available in the "Pin" class:

      - init(): This function initializes the Pin object and sets the direction of the GPIO pin as either an input or an output.
      - value(): This function gets or sets the value of the GPIO pin. When used as a getter, it returns the current logical level of the pin (0 or 1). When used as a setter, it sets the logical level of the pin to 0 or 1.
      - on(): This function sets the GPIO pin to a logical high level (1).
      - off(): This function sets the GPIO pin to a logical low level (0).
      - toggle(): This function toggles the logical level of the GPIO pin between 0 and 1.
      - irq(): This function configures the interrupt handler for the GPIO pin, allowing you to respond to external events such as button presses or sensor readings.
  - `Timer`: class in MicroPython is used for controlling the hardware timers of the microcontroller. Timers are useful for performing periodic tasks, measuring time intervals, generating PWM signals, and more. The "Timer" class provides several functions to configure and control the behavior of the hardware timers.

      - init(): This function initializes the Timer object and sets its frequency, prescaler, and period values.
      - deinit(): This function stops and deallocates the Timer object, releasing any hardware resources used by the timer.
      - freq(): This function gets or sets the frequency of the timer clock, in Hertz (Hz).
      - prescaler(): This function gets or sets the prescaler value of the timer, which divides the timer clock frequency by a certain factor.
      - period(): This function gets or sets the period value of the timer, which determines the time interval between timer events.
      - callback(): This function sets the interrupt handler function for the timer, which is called when the timer event occurs.
  - `ADC`: This feature allows you to read analog values from GPIO pins configured to function as analog inputs.
      - read(): This function reads a single value from the ADC and returns it as an integer between 0 and 4095 (inclusive).
  - `PWM`: This class in MicroPython is used for controlling the Pulse-Width Modulation (PWM) output signals of the microcontroller. PWM signals are used for controlling the speed of motors, dimming LEDs, generating audio signals, and more. The "PWM" class provides several functions to configure and control the behavior of the PWM signals. Here are some of the important functions available in the "PWM" class:
      - init(): This function initializes the PWM object and sets its frequency and duty cycle values.
      - deinit(): This function stops and deallocates the PWM object, releasing any hardware resources used by the PWM signal.
      - frequency(): This function gets or sets the frequency of the PWM signal, in Hertz (Hz).
      - duty(): This function gets or sets the duty cycle of the PWM signal, as a floating-point value between 0.0 (0%) and 1.0 (100%).
      - pulse_width(): This function gets or sets the pulse width of the PWM signal, in seconds.
      - start(): This function starts the PWM signal output.
      - stop(): This function stops the PWM signal output.
  - `RTC`: This feature allows you to configure and control the real-time clock (RTC) of the microcontroller.
  
  The `utime` module is another built-in module in MicroPython that provides time-related functions for the microcontroller. Here are some of the important functions available in the "utime" module:

  - `time()`: This function returns the number of seconds since the Epoch (January 1, 1970, 00:00:00 UTC) as a floating-point number.
  - `sleep()`: This function puts the microcontroller into a low-power state for a specified number of seconds.

## Scripts and explanations

* Turn a LED ON
  - Led module is wired to the Raspberry Pico W on ***pin 16*** (see demo and link below)
      
    ![20230308_083714](https://user-images.githubusercontent.com/124893862/223837715-153c06fe-cabd-41b8-896f-579fce2bceea.jpg)

  - [led.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/led.py)
  
* Turn a LED ON
  - Led module is wired to the Raspberry Pico W on ***pin 16*** (see demo and link below)
    
    ![20230308_083714](https://user-images.githubusercontent.com/124893862/223837715-153c06fe-cabd-41b8-896f-579fce2bceea.jpg)

    
  - [led1.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/led1.py)
 
* Turn a LED OFF
  - Led module is wired to the Raspberry Pico W on ***pin 16*** (see demo and link below)
 
    ![20230308_083750](https://user-images.githubusercontent.com/124893862/223839184-9c4354d2-c6d3-4d1a-83f7-65b7fe33d142.jpg)

  - [led2.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/led2.py)
  
* Control a LED with a button
  - Led module is wired to the Raspberry Pico W on ***pin 16*** and the button to the ***pin 18*** (see demo and link below)

    https://user-images.githubusercontent.com/124893862/223842190-7527f393-43f2-4c19-beb0-4137b6b5dfeb.mp4
  
  - [button_led.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/button_led.py)
  
* Control a LED with a button with 1 second delay
  - Led module is wired to the Raspberry Pico W on ***pin 16*** and the button to the ***pin 18*** (see demo and link below)

    https://user-images.githubusercontent.com/124893862/223850492-cab7baaa-cba4-414d-964d-baf9c28e23bb.mp4

  - [button_led2.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/button_led2.py)

* Blink a LED 10 times
  - Led module is wired to the Raspberry Pico W on ***pin 16*** to turn on and off with 1 second of delay(see demo and link below)
     
    https://user-images.githubusercontent.com/124893862/223842703-ade20a20-2373-4e14-b7c3-d16ca1e87682.mp4 
     
  - [blink.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/blink.py)

* More Blinking a LED
  - Led module is wired to the Raspberry Pico W on ***pin 16*** to blink with 1/10th of a second of delay(see demo and link below)
  
    https://user-images.githubusercontent.com/124893862/223843011-cf5f5826-7772-42b3-bb72-17a53a0c164a.mp4
  - [more_blink.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/more_blink.py)

* While Blinking a LED
  - Led module is wired to the Raspberry Pico W on ***pin 16*** to blink forever with 1 second of delay (see demo and link below)
 
    https://user-images.githubusercontent.com/124893862/223842703-ade20a20-2373-4e14-b7c3-d16ca1e87682.mp4 

  - [while_blink.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/while_blink.py)

* Control a LED with a button by an interrupt
  - Led module is wired to the Raspberry Pico W on ***pin 16*** and the button to the ***pin 18*** (see demo and link below)

    https://user-images.githubusercontent.com/124893862/223842190-7527f393-43f2-4c19-beb0-4137b6b5dfeb.mp4
  
  - [button_led_int.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/GPIO/button_led_int.py)
