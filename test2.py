import wiringpi2 as wp
import time
wp.wiringPiSetupGpio()

wp.pinMode(17, 1)

while (True):
    wp.digitalWrite(17, 1)
    time.sleep(1)
    wp.digitalWrite(17, 0)
    time.sleep(1)


