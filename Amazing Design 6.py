import turtle as y
y.speed(0)
y.bgcolor('black')
y.pencolor('cyan')
for a in range(160):
    y.rt(a)
    y.circle(200,a)
    y.fd(a)
    y.rt(90)
y.done()