#pythonDraw.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()#提起画笔
turtle.fd(-250)
turtle.pendown()#落下画笔
turtle.pensize(25)
turtle.pencolor("#1C1C1C")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
