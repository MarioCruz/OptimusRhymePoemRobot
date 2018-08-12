from EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
import time
import os
from datetime import datetime
import random , glob , subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previous_robot = None
previous_human = None
curdir = os.path.dirname(os.path.realpath(__file__))

def play_random(voice, previous):
   pattern = "/mp3h/*.mp3" if voice == "human" else "/mp3/*.mp3"
   randomfile = random.choice(glob.glob(curdir + pattern))
   if randomfile == previous:
    return play_random(voice, previous)
   else:
    return randomfile

def button_pressed(voice, previous):
   random.seed(datetime.now())
   time.sleep(0.2)
   file = play_random(voice, previous)
   os.system ('mpg123 ' + file)
   return file

while True:
    input_state = GPIO.input(18)
    if input_state == False:
       previous_human = button_pressed('human', previous_human)

    input_state = GPIO.input(23)
    if input_state == False:
        previous_robot = button_pressed('robot', previous_robot)

GPIO.cleanup()
