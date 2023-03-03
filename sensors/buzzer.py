from machine import PWM
#create a Freq tuple, including mute,DO,RE,MI,FA,SOL,LA,SI
Freq=(30000,1046,1174,1318,1396,1567,1780,1975,2085)
#define Music object below
class Music:
    #add a construtor to the createsd class:
    def __init__(self,pwm_pin):
        #define PWM pin variable
        self.pwm=pwm_pin
    #define an example method of Music to play different notes
        def music(self,number):
            self.pwm.freq(Freq[number])	#List Freq[number]) contains eight
            #elements from 0 to 7. When we play RE, just write music(3)
            self.pwm.duty_u16(5000)