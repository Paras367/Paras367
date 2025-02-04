import turtle
colors=['orange','cyan','pink','white','blue','red','magenta','green','violet','purple','yellow']
t=turtle.Pen()
turtle.bgcolor('black')
turtle.pencolor('blueviolet')
turtle.speed(50)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(50)
    
    
