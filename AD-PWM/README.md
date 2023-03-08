/smartcities/AD-PWM/README.md

This file is to index the different files in this directory and inform users about the functionning and the essential wiring of each script. 

## Syntax implemented in

  The `machine` class is a built-in class in MicroPython that provides functionalities to access the hardware resources of the microcontroller on which MicroPython is running. This class is mainly used to perform I/O (input/output) operations such as reading and writing to GPIO pins, managing hardware interrupts, putting the microcontroller to sleep, and controlling the clock.

Here are some of the important features of the machine class:

  - `Pin`: This  class  is used for controlling the General-Purpose Input/Output (GPIO) pins of the microcontroller. The GPIO pins can be configured as either inputs or outputs, allowing you to read external signals or control external devices such as LEDs, motors, sensors, and more. The "Pin" class provides several functions to control the behavior of the GPIO pins.

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
      - freq(): This function gets or sets the frequency of the PWM signal, in Hertz (Hz).
      - duty(): This function gets or sets the duty cycle of the PWM signal, as a floating-point value between 0.0 (0%) and 1.0 (100%).
      - pulse_width(): This function gets or sets the pulse width of the PWM signal, in seconds.
      - start(): This function starts the PWM signal output.
      - stop(): This function stops the PWM signal output.
  - `RTC`: This feature allows you to configure and control the real-time clock (RTC) of the microcontroller.
  
  The `utime` module is another built-in module in MicroPython that provides time-related functions for the microcontroller. Here are some of the important functions available in the "utime" module:

  - `time()`: This function returns the number of seconds since the Epoch (January 1, 1970, 00:00:00 UTC) as a floating-point number.
  - `sleep()`: This function puts the microcontroller into a low-power state for a specified number of seconds.

## Scripts and explanations

* Read the value of a rotary sensor
  - Rotary sensor module is wired to the Raspberry Pico W on ***pin ADC0*** (see demo and link below)
   
    ![20230308_090206](https://user-images.githubusercontent.com/124893862/223845046-07dd0d4f-ce9c-43fa-802c-5cca55d75e56.jpg)
   
    And the results
   
    ![knob](https://user-images.githubusercontent.com/124893862/223845211-f4228f41-4b49-46ab-86ff-f8c53c1b0f53.png)
   
  - [knob.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/AD-PWM/knob.py)
  
* Turn a LED ON with a rotary sensor
  - Led module is wired to the Raspberry Pico W on ***pin 16*** and rotary sensor to the ***pin ADC0*** (see demo and link below)
  

    https://user-images.githubusercontent.com/124893862/223846517-3ddef25b-75d5-4ece-8e07-d1392fdfe7cc.mp4
    
    And the results
    
    ![knob2](https://user-images.githubusercontent.com/124893862/223846670-73a7b565-4474-48d6-8c4c-f6dd3f6d3228.png)

   
  - [knob2.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/AD-PWM/knob2.py)
 
* Turn a LED ON with a rotary sensor at a bandwith
  - Led module is wired to the Raspberry Pico W on ***pin 16*** and rotary sensor to the ***pin ADC0*** (see demo and link below)
    
    https://user-images.githubusercontent.com/124893862/223846747-e13c2af7-5440-4e28-bc37-3e95525fae3a.mp4
    
    And the results
    
    ![knob3](https://user-images.githubusercontent.com/124893862/223846887-af09e1ff-42fd-49b2-bd3e-4a6238482844.png)

  - [knob3.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/AD-PWM/knob3.py)

* Fade IN & OUT a LED light
  - Led module is wired to the Raspberry Pico W on ***pin 16*** (see demo and link below)

     https://user-images.githubusercontent.com/124893862/223848106-b01a6881-3d47-46af-b922-2e41071143e4.mp4

  - [fade.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/AD-PWM/fade.py)

* Fade an LED with a rotary sensor
  - Led module is wired to the Raspberry Pico W on ***pin 16*** and rotary sensor to the ***pin ADC0*** (see demo and link below)
  
     https://user-images.githubusercontent.com/124893862/223847719-77713eee-fe27-4bd9-a8f8-d063724b55f8.mp4
      
  - [knob_led.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/AD-PWM/knob_led.py)

* Play an octave of music scales with a buzzer
  - Buzzer module is wired to the Raspberry Pico W on ***pin 20*** (see demo and link below)
  
    ![20230308_085812](https://user-images.githubusercontent.com/124893862/223848375-f2635012-e942-4bb3-b238-a3f54e4a5cd3.jpg)

  - [buzzer.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/AD-PWM/buzzer.py)

* Play "Little Star" with a buzzer
  - Buzzer module is wired to the Raspberry Pico W on ***pin 20*** (see demo and link below)
  
    ![20230308_085812](https://user-images.githubusercontent.com/124893862/223848375-f2635012-e942-4bb3-b238-a3f54e4a5cd3.jpg)

  - [little_star.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/AD-PWM/little_star.py)

* Play "Two Tigers" with a buzzer
  - Buzzer module is wired to the Raspberry Pico W on ***pin 20*** (see demo and link below)
  
    ![20230308_085812](https://user-images.githubusercontent.com/124893862/223848375-f2635012-e942-4bb3-b238-a3f54e4a5cd3.jpg)

  - [two_tiger.py](https://github.com/HEPL-Galhardo/smartcities/blob/main/AD-PWM/two_tiger.py)

