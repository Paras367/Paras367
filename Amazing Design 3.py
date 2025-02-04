from turtle import *
import colorsys
bgcolor('black')
tracer(5)
h=0

for i in range(600):
    c=colorsys.hsv_to_rgb(h, 1, 1)
    h+=0.005
    color(c)
    fillcolor('black')
    up()
    circle(i,45)
    down()
    begin_fill()
    circle(40,145)
    left(80)
    circle(40,145)
    end_fill()
done()