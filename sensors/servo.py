from machine import Pin, PWM	#call machine library
#define a servo object below:
class SERVO:
    #add a constructor to the created class:
    def __init__(self, pin):
        #define two instance variables , pin and PWM:
        self.pin=pin
        self.pwm=PWM(self.pin)
    #define example method of turn to calculate the rotation angle of Servo:
    def turn(self,val):
        self.pwm.freq(100)
        self.pwm.duty_u16(int(val/180*13000+4000))