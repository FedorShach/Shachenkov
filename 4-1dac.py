import RPi.GPIO as GPIO
import sys
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def foo(a, n):
    return [int(elem) for elem in bin(a)[2:].zfill(n)]
try:
    while (True):
        a = input('Число ')
        if a == 'q':
            sys.exit()
        if not a.isdigit():
            print("Введите число")
        elif int(a)>=256:
            print("Число слишком большое")
        else:
            GPIO.output(dac,foo(int(a), 8))
            print ("{:.4f}".format(int(a)/256*3.3,"Вольт"))
except ValueError:
    print ('Введите число 0-255')
finally:
        GPIO.output(dac,0)
        GPIO.cleanup()