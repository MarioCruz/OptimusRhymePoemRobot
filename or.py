#!/usr/bin/env python
import os, random

def rndmp3 ():
   randomfile = random.choice(os.listdir("/home/pi/or/mp3/"))
   file = '/home/pi/or/mp3/'+ randomfile
#   os.system ('omxplayer -o local ' + file)
   os.system ('mpg123 ' + file)

rndmp3 ()
