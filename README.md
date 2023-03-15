# Raspberry Pi Pico W


## Introduction of Pico

The Raspberry Pi Pico W is a compact and affordable microcontroller board that is designed for embedded projects and IoT applications. It features a powerful Arm Cortex-M0+ processor running at 133MHz, 264KB of RAM, 2MB of onboard flash memory, and a wide range of I/O pins, including 26 multifunctional GPIO pins, SPI, I2C, UART, and PWM.

![image](https://user-images.githubusercontent.com/124893862/219611249-dd82aad6-da4c-41f7-a80e-fc87fd51e38a.png)

The Pico W also includes a built-in Wi-Fi module, which allows for wireless connectivity and communication with other devices or networks. This makes it ideal for building connected devices and IoT projects that require remote control and data exchange.

To program the Raspberry Pi Pico W, you can use MicroPython, a lightweight version of the Python programming language that is specifically designed for microcontrollers. MicroPython allows you to write code in Python syntax, which makes it easy to learn and use, even for beginners.

![image](https://user-images.githubusercontent.com/124893862/219622236-a85db1f7-3dd8-4ba2-a3bf-8396c5b27cb0.png)

MicroPython provides a rich set of libraries and modules that you can use to interact with the board's hardware peripherals, including GPIO, PWM, I2C, SPI, and UART. You can also leverage third-party libraries and modules that are compatible with MicroPython to extend the functionality of your projects.

Overall, the Raspberry Pi Pico W, combined with MicroPython, offers a powerful and accessible platform for building embedded and IoT projects. Whether you're a beginner or an experienced developer, the Pico W provides a versatile and affordable solution for prototyping and implementing your ideas.

## GPIO Pins

In addition to the powerful new chip, the board of Raspberry Pi Pico exposes 26 multi-function GPIO pins, including 2 * SPI, 2 * I2C, 2 * UART, 3 * 12-bit ADC, and 16 controllable 
PWM channels. I will explain the functions of these pins in each respective directory.
In addition to these GPIO pins, Pico also has eight ground pins and a series of power pins. 


![image](https://user-images.githubusercontent.com/124893862/219611075-1f9e3f77-ad73-4504-9a44-8857870773e3.png)

### Shield Case

The shield case has white connectors to link the rapsberry to the diferent modules using a cable, this way there is no mistake that can't be made and we can focus more on the programming. We can find the name of each pin (that we want to call) written to the connector that we just wired. Power voltage of these connectors can be switched between 5 to 3.3V with a simple switch. It have a double female pin header for the use of single wiring to the RPi GPIO

Grove Shield For Pi Pico v1.0 by Seed Studio https://www.seeedstudio.com/

![image](https://user-images.githubusercontent.com/124893862/219610776-ff0e4372-5288-4e84-8a42-88c22d09d84c.png)
