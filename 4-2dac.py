import RPi.GPIO as GPIO
import time as tm
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
GPIO.setup(dac,GPIO.OUT)
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    T=float(input("T="))
    N=int(input("N="))
    m=0
    for j in range(N):
        while m<255:
            GPIO.output(dac,dec2bin(m))
            m=m+1
            tm.sleep(T)
        while m>0:
            GPIO.output(dac,dec2bin(m))
            m=m-1
            tm.sleep(T)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()