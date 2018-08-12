#!/usr/bin/env python
import os, random

def rndmp3 ():
   randomfile = random.choice(os.listdir("/home/pi/or/mp3h/"))
   file = '/home/pi/or/mp3h/'+ randomfile
#   os.system ('omxplayer -o local ' + file)
   os.system ('mpg123 ' + file)

rndmp3 ()
