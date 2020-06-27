
import turtle
import math

anms = turtle.Turtle()
anms.color("green")
anms.speed(10000)

anms.shape("turtle")

anms.begin_fill()
'''
for i in range(2000):
    anms.forward(10)
    anms.forward(math.sin(i/10)*25)
    anms.left(20)
'''
for i in range(2000):
    anms.forward(10)
    anms.left(math.sin(i/10)*25)
    anms.left(20)

anms.end_fill()

turtle.mainloop()

