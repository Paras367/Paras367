import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pensize(4)
t.speed(0)
n=40
h=0

for i in range(360):
    c=colorsys.hsv_to_rgb(h, 1, 1)
    h+=0.005
    t.color(c)
    t.forward(i*2)
    t.left(145)
t.done()
