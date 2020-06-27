import turtle

anms = turtle.Turtle()
anms.color("red", "yellow")
anms.speed(100)
anms.fd(-150)

anms.begin_fill()

for i in range(90):
    anms.forward(300)
    anms.left(170)

anms.end_fill()

turtle.mainloop()
