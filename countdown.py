# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:51:56 2023

@author: anitta

program to create a countdown timer
"""

import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        print("stops in ", time_sec)


num = int(input("set your time in sec : "))
countdown(num)
