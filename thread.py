import RPi.GPIO as GPIO
from flask import Flask
from flask import request
import threading
import time



def job():
    my_led_status = request.args.get('value')
    while 7==7:
            GPIO.output(25, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(25, GPIO.LOW)
            time.sleep(1)
    return 'LED_string'

t = threading.Thread(target = job)


def start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, GPIO.HIGH)
    return 'LED_ON'

if __name__== '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)


for i in range(3):
    print("Main thread:", i)
    time.sleep(1)

t.join()
print("Done.")
