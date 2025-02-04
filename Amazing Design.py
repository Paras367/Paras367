import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)

for i in range (200):
    t.pencolor('cyan')
    t.circle(-i+1,200)
    t.rt(80)
    
turtle.done()
