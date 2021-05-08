import RPi.GPIO as GPIO
from flask import Flask
from flask import request
import threading
import time
global var
app = Flask(__name__)

@app.route('/',methods = ['GET'])


def job():
    global var
    my_led_status = request.args.get('/var')
    while 7==7:
      if var == 2:
          break
      GPIO.output(25, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(25, GPIO.LOW)
      time.sleep(1)

def start():
    global var
    my_led_status = request.args.get('/var')
    if my_led_status == "0":
       GPIO.output(25, GPIO.LOW)
       return 'LED_OFF'
       var = 2
    elif my_led_status == "1":
       GPIO.output(25, GPIO.HIGH)
       return 'LED_ON'
       var = 2
    elif my_led_status == "2":
        t = threading.Thread(target = job)
        t.start()
        var = 1
        return "start"
    elif my_led_status == "3":
        var = 2
        return "stop"
    t.start()
    t.join()
for i in range(3):
    print("Main thread:", i)
    time.sleep(1)


print("Done.")

if __name__== '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    app.run()
    global var
    var = 1
    print(var)
    func()
    print(var)

