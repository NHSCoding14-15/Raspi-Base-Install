import wiringpi2 as wp
import time
wp.wiringPiSetupGpio()
import math

wp.pinMode(17, 1) 
wp.pinMode(18, 1)
wp.pinMode(27, 1)

sleep = input('start: ')

while (True):
    
    
    wp.digitalWrite(17, 1)
    time.sleep(sleep)
    wp.digitalWrite(17, 0)
    time.sleep(sleep)
    wp.digitalWrite(18, 1)
    time.sleep(sleep)
    wp.digitalWrite(18, 0)
    time.sleep(sleep)
    wp.digitalWrite(27, 1)
    time.sleep(sleep)
    wp.digitalWrite(27, 0)
    time.sleep(sleep)
    sleep = (sleep*0.5)
    print (sleep)


    
