#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 21:28:09 2018

@author: danamulligan
"""

#%% Imports
import turtle


#%% Define functions
def koch_curve(t, length, lvl=0):
    '''
    Draw Koch Curve of given length and level
    '''
    if lvl == 0:
        t.forward(length)
    if lvl >= 1:
        koch_curve(t, length/3, lvl-1)
        t.lt(60)
        koch_curve(t, length/3, lvl-1)
        t.lt(-120)
        koch_curve(t, length/3, lvl-1)
        t.lt(60)
        koch_curve(t, length/3, lvl-1)

def init_turtle(t):
    '''
    Set pen size, speed, and color
    '''
    t.pensize(2)
    t.speed(0)
    t.color('white')
     
#%% Main code if script is run
if __name__ == '__main__':
    wn = turtle.Screen()
    wn.clearscreen()
    wn.bgcolor('black')
    try:
        kasa = turtle.Turtle()
    except:
        kasa = turtle.Turtle()
    
    #change below number to change detail
    levelnum = 6
    
    init_turtle(kasa)
    kasa.penup()
    kasa.setposition(-300, 0)
    kasa.pendown()
    koch_curve(kasa, 600, levelnum)
    
# each problem will be put together and turned in separately
    
    from sys import platform
    if platform=='win32':
        wn.exitonclick()