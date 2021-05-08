import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)

@app.route('/led_on')
def led_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, GPIO.HIGH)
    return 'LED_ON'

@app.route('/led_off')
def led_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, GPIO.LOW)
    return 'LED_OFF'


if __name__== '__main__':
    app.run()