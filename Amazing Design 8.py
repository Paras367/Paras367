import turtle as t
t.bgcolor('black')
colors=('cyan','blueviolet','green','orange')
t.speed(0)
for i in range(50):
    t.pencolor(colors[1%3])
    t.width(2)
    t.forward(2)
    t.circle(95,steps=4)
    t.forward(i)
    t.right(45)
t.hideturtle()
t.done()
