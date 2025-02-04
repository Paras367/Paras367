from turtle import *
import turtle as t
import colorsys
import time
bgcolor('black')
width(1)
speed(1000)
goto(0,0)
seth(0)
a=500
h=0
i=400
ht()
color('white')

while True:
    c=colorsys.hsv_to_rgb(h, 1, 1)
    h+=0.003
    color(c)
    fd(400)
    circle(10)
    goto(0,0)
    lt(1)
done()
    
    
    
