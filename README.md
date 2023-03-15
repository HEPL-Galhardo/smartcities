# Raspberry Pi Pico W


## Introduction of Pico

No one expected that Raspberry Pi, the most popular single-board computer maker in the world, would suddenly release a microcontroller of its own. What's more surprising is that Raspberry Pi Pico does not base its design on the common ESP32 or SAMD21, but instead a brand new microcontroller chip: the RP2040 microcontroller. The RP2040 microcontroller is a microcontroller chip independently designed by Raspberry Pi, and is powered by a dual-core ARM 
Cortex-M0+ processor that runs up to 133Mhz. Programming will run with MicroPython, MicroPython has made strides in keeping compatibility with ordinary Python as much as possible.

![image](https://user-images.githubusercontent.com/124893862/219622236-a85db1f7-3dd8-4ba2-a3bf-8396c5b27cb0.png)

![image](https://user-images.githubusercontent.com/124893862/219611249-dd82aad6-da4c-41f7-a80e-fc87fd51e38a.png)


## GPIO Pins

In addition to the powerful new chip, the board of Raspberry Pi Pico exposes 26 multi-function GPIO pins, including 2 * SPI, 2 * I2C, 2 * UART, 3 * 12-bit ADC, and 16 controllable 
PWM channels. I will explain the functions of these pins in each respective directory.
In addition to these GPIO pins, Pico also has eight ground pins and a series of power pins. 


![image](https://user-images.githubusercontent.com/124893862/219611075-1f9e3f77-ad73-4504-9a44-8857870773e3.png)

### Shield Case

The shield case has white connectors to link the rapsberry to the diferent modules using a cable, this way there is no mistake that can't be made and we can focus more on the programming. We can find the name of each pin (that we want to call) written to the connector that we just wired. Power voltage of these connectors can be switched between 5 to 3.3V with a simple switch. It have a double female pin header for the use of single wiring to the RPi GPIO

Grove Shield For Pi Pico v1.0 by Seed Studio https://www.seeedstudio.com/

![image](https://user-images.githubusercontent.com/124893862/219610776-ff0e4372-5288-4e84-8a42-88c22d09d84c.png)
