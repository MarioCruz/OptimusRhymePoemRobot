import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
        os.system("sudo python orh.py")
        print('Button Stoped')
        
    input_state = GPIO.input(23)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
        os.system("sudo python or.py")
        print('Button Stoped')
        
        
        
GPIO.cleanup() 
        
        
