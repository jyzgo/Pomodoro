#!/usr/bin/env python
# -*- coding: utf8 -*-
import time
import os
import sys
from subprocess import call
import winsound 
 


music = "alarm.wav"
workMusic = "alarm.wav"

loop = True
played = False
m = 45
curM =0
while(loop):
    # now
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]

    if(m == minute and played == False):
        winsound.PlaySound(music, winsound.SND_ALIAS)
        played = True
        curM = minute
    if(played == True and curM != minute):
        played =False
    # display current time
    timestr = "%04d-%02d-%02d %02d:%02d:%02d\r" \
            % (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5])
    sys.stdout.write(timestr)
    sys.stdout.flush()
    time.sleep(1)
    # end
