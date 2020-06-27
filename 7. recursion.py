
import turtle

anms = turtle.Turtle()
turtle.getscreen().bgcolor("yellow")

anms.shape("turtle")
anms.speed(100)
anms.color("red", "green")

# for i in range(5):
#     anms.forward(50)
#     anms.left(216)

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()
        
star(anms, 360)

turtle.mainloop()

