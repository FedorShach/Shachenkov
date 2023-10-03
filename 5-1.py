import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)
def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    a = 0
    for i in range(7, -1, -1):
        a += 2 ** i
        daccc = dec2bin(a)
        gpio.output(dac, daccc)
        sleep(0.005)
        compvalue = gpio.input(comp)
        if compvalue == 1:
            a -= 2 ** i
    return a


try:
    while True:
        i = adc()
        if i != 0:
            print(3.3*i/256, 'Bольт')

finally:
    gpio.output(dac, 0)
    gpio.cleanup()