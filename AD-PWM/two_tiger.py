# File : two_tiger.py
# Simple program to play a song two-tiger
# https://docs.micropython.org/en/latest/library/machine.Pin.html
# joao.galhardocarraca@student.hepl.be
# 14/2/2023

#Import of libraries
from machine import Pin,PWM
from utime import sleep

#Configuration of the buzzer pin
bz=PWM(Pin(20))
vol=1000

#Note Functions
def DO(time):
    bz.freq(1046)#DO
    bz.duty_u16(vol)
    sleep(time)

def RE(time):    
    bz.freq(1175)#RE
    bz.duty_u16(vol)
    sleep(time)

def MI(time):    
    bz.freq(1318)#MI
    bz.duty_u16(vol)
    sleep(time)
    
def FA(time):  
    bz.freq(1397)#FA
    bz.duty_u16(vol)
    sleep(time)

def SOL(time):   
    bz.freq(1568)#SOL
    bz.duty_u16(vol)
    sleep(time)

def LA(time): 
    bz.freq(1760)#LA
    bz.duty_u16(vol)
    sleep(time)

def SI(time):  
    bz.freq(1967)#SI
    bz.duty_u16(vol)
    sleep(time)
    
def N(time):
    bz.duty_u16(0)#close
    sleep(time)

#While Statement to play a music while repeting the upper functions
while True:
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    N(0.01)
    
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    
    MI(0.25)
    FA(0.25)
    SOL(0.5)
    
    MI(0.25)
    FA(0.25)
    SOL(0.5)
    N(0.01)
    
    SOL(0.125)
    FA(0.125)
    SOL(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    SOL(0.125)
    LA(0.125)
    SOL(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    RE(0.25)
    SOL(0.25)
    DO(0.5)
    N(0.01)
    
    RE(0.25)
    SOL(0.25)
    DO(0.5)