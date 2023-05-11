# File : NTP_time.py
# Description: Get the to update time of the RTC using NTP 
# joao.galhardocarraca@student.hepl.be
# 01/05/2023

#-----------------Import of libraries------------------
import machine
import network
import ntptime
import utime

#-----------------Modules configuration------------------
rtc = machine.RTC()

#-----------------Wifi connection------------------
ssid = 'Android Galhardo'
password = 'Galhardo1996'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
# Waiting for connection
while not station.isconnected():
    pass


print("PC clock, local time without update! ",utime.localtime())
# RTC hours readings and display
year, month, day, weekday, hours, minutes, seconds, subseconds = rtc.datetime()
print("Time RTC 1 : {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))

# Update of RTC time with NTP
ntptime.settime()

# RTC hours readings and display
year, month, day, weekday, hours, minutes, seconds, subseconds = rtc.datetime()
print("Time RTC 2 after NTP: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
print("Local time with NTP update! ",utime.localtime())
current_time = utime.localtime()
print("Correction of the clock hours with +2H")
# Ajusting time with 2 more hours
adjusted_hour = (current_time[3] + 2) % 24

# Display Date
print("Date: {:02d}-{:02d}-{:02d}".format(current_time[2], current_time[1], current_time[0]))
# Display time
print("Time: {:02d}:{:02d}:{:02d}".format(adjusted_hour, current_time[4], current_time[5]))