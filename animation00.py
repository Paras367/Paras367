import turtle
import random

class someNights:
    def __init__(self, n):
        global fun, window
        # Initialize the turtle and screen
        window = turtle.Screen()
        fun = turtle.Turtle()
        
        # The title of the window
        turtle.title("Some Nights")
        
        # Mode logo makes positive angles clockwise
        turtle.mode("logo")
        
        # Set a dark color for the background
        window.bgcolor("#2c3e50")
        
        # Set the fastest speed
        fun.speed(0)
        
        # Set the branches' color
        fun.color("#825a2c")
        fun.pensize(10)
        fun.penup()
        fun.backward(300)
        fun.pendown()
        fun.forward(100)
        fun.penup()
        
        # Use `tracer` on the `window` object
        window.tracer(200)
        
        # Draw the tree
        self.drawTree(n, 60, 0, -200, 0, 10)

        # Reset turtle settings for snowflakes
        fun.width(1)
        fun.penup()
        fun.goto(-150, 100)
        
        # Draw the snowflakes
        for i in range(0, 10):
            for j in range(0, 10):
                # Set the color of the snowflakes
                fun.color("#ecf0f1")
                fun.pendown()
                self.drawSnowflake((i + j) % 3 + 1, 2)
                fun.penup()
                fun.setheading(90)
                fun.forward(30)
            fun.setheading(270)
            fun.forward(300)
            fun.setheading(180)
            fun.forward(50)

        # Exit on click
        window.exitonclick()

    # Function to draw the tree
    def drawTree(self, n, length, x, y, prevAngle, sizeOfPen):
        # If the counter is now zero, terminate the branch
        if n == 0:
            return

        # Put at x,y
        fun.setpos(x, y)

        # Set the pensize to the new pensize specified by previous recursive call
        fun.pensize(sizeOfPen)

        if sizeOfPen == 1:
            newPenSize = 1
        else:
            # If pensize isn't 1 decrease the pensize
            newPenSize = sizeOfPen - 1

        fun.pendown()

        # Left branch
        angle1 = prevAngle + random.randrange(20, 40)

        # Right branch
        angle2 = prevAngle - random.randrange(20, 40)

        fun.setheading(angle1)
        fun.forward(length)
        
        # x1 is the current x coordinate
        x1 = fun.pos()[0]
        
        # y1 is the current y coordinate
        y1 = fun.pos()[1]

        # Each leaf has a green dot as a leaf on the tree
        if n == 1:
            fun.dot(4, "#27ae60")

        # 50% of chance that the branch will finish when n = 2
        if n == 2:
            if random.random() <= 0.49:
                fun.dot(2, "#27ae60")
                fun.penup()
                return

        fun.backward(length)
        fun.setheading(angle2)
        fun.forward(length)
        
        x2 = fun.pos()[0]
        y2 = fun.pos()[1]

        if n == 1:
            fun.dot(2, "#c0392b")

        fun.penup()

        # Recursive calls to draw the left and right branches
        self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x1, y1, angle1, newPenSize)
        self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x2, y2, angle2, newPenSize)

    # Helper function for fractal drawing
    def drawFractal(self, length, depth):
        if depth == 1:
            fun.forward(length)
        else:
            self.drawFractal(length, depth - 1)
        fun.right(60)
        if depth == 1:
            fun.forward(length)
        else:
            self.drawFractal(length, depth - 1)
        fun.left(120)
        if depth == 1:
            fun.forward(length)
        else:
            self.drawFractal(length, depth - 1)
        fun.right(60)
        if depth == 1:
            fun.forward(length)
        else:
            self.drawFractal(length, depth - 1)

    # Function to draw each snowflake
    def drawSnowflake(self, length, depth):
        self.drawFractal(length, depth - 1)
        fun.left(120)
        self.drawFractal(length, depth - 1)
        fun.left(120)
        self.drawFractal(length, depth - 1)

# Define the number of iterations
n = 13

# Initialize and draw
thisNight = someNights(n)
