
import turtle
import math

anms = turtle.Turtle()
anms.color("red", "yellow")
anms.speed(1000)

anms.shape("turtle")

anms.begin_fill()

for i in range(2200):
    anms.forward(math.sqrt(i))
    anms.left(i%180)

anms.end_fill()

turtle.mainloop()

