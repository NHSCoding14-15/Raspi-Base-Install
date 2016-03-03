import wiringpi2 as wp
import time
wp.wiringPiSetupGpio()
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

rawdata = input("power selection")
pwm = gpio.PWM(17, 500)
pwm.start(rawdata)

'''wp.pinMode(17, 1)
while(True):
    wp.digitalWrite(17 ,1)
    time.sleep(1)
    wp.digitalWrite(17, 0)
    time.sleep(1) 
rawdata = input("power selection")
pwm = gpio.PWM(17, 500)
pwm.start(rawdata)'''
    
