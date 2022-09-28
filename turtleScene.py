import turtle
import random

turtle.screensize(-200,200)


def sun():
    turtle.pu()
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.pencolor("yellow")
    turtle.goto(-130, 200)
    turtle.pd()
    turtle.circle(30)
    turtle.end_fill()



def sky():
    turtle.pu()
    turtle.begin_fill()
    turtle.fillcolor("SkyBlue")
    turtle.pencolor("SkyBlue")
    turtle.goto(-200,-50)
    turtle.setheading(90)
    turtle.pd()
    turtle.forward(300)
    turtle.setheading(0)
    turtle.forward(400)
    turtle.setheading(270)
    turtle.forward(300)
    turtle.setheading(180)
    turtle.setheading(400)
    turtle.setheading(180)
    turtle.forward(400)
    turtle.end_fill()


def water():
    turtle.pu()
    turtle.begin_fill()
    turtle.fillcolor("DarkBlue")
    turtle.pencolor("DarkBlue")
    turtle.goto(-200, -200)
    turtle.pd()
    turtle.setheading(90)
    turtle.forward(150)
    turtle.setheading(0)
    turtle.forward(400)
    turtle.setheading(270)
    turtle.forward(150)
    turtle.setheading(180)
    turtle.forward(400)
    turtle.end_fill()

def oval():
    for i in range(1):
        turtle.fillcolor("chartreuse")
        turtle.begin_fill()
        turtle.circle(10,100)
        turtle.circle(10//2,100)
        turtle.end_fill()
        turtle.pu()
        turtle.setheading(0)
        turtle.forward(20)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(10,100)
        turtle.circle(10//2,100)
        turtle.end_fill()



def island():
    turtle.pu()
    x = random.randint(-150,140)
    turtle.begin_fill()
    turtle.fillcolor("gold3")
    turtle.pencolor("gold3")
    turtle.goto(x,-50)
    turtle.setheading(90)
    turtle.pd()
    turtle.circle(25, 180)
    turtle.setheading(0)
    turtle.forward(50)
    turtle.end_fill()
    turtle.setheading(180)
    turtle.forward(27)
    turtle.setheading(90)
    turtle.forward(25)
    turtle.pencolor("chocolate4")
    turtle.fillcolor("chocolate4")
    turtle.begin_fill()
    turtle.forward(20)
    turtle.setheading(0)
    turtle.forward(5)
    turtle.setheading(270)
    turtle.forward(20)
    turtle.setheading(180)
    turtle.forward(5)
    turtle.end_fill()
    turtle.setheading(90)
    turtle.forward(20)
    turtle.pencolor("chartreuse")
    oval()


def boat():
    x = random.randint(-150,140)
    
    turtle.pu()
    turtle.begin_fill()
    turtle.fillcolor("Brown")
    turtle.pencolor("Brown")
    turtle.goto(x,0)
    turtle.setheading(270)
    turtle.pd()
    turtle.circle(50, 180)
    turtle.setheading(180)
    turtle.forward(100)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.setheading(90)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(60)
    turtle.setheading(270)
    turtle.forward(30)
    turtle.setheading(180)
    turtle.forward(55)
    turtle.setheading(270)
    turtle.forward(25)
    turtle.end_fill()
    
    
   
    

turtle.speed(900)

sky()
water()
sun()
boat()
island()

for i in range(10):
    x = random.randint(-130, 130)
    y = random.randint(-175, -80)
    
    turtle.pu()
    turtle.pencolor("cyan3")
    turtle.goto(x, y)
    turtle.setheading(90)
    turtle.pd()
    turtle.circle(5, 180)
    turtle.setheading(270)
    turtle.circle(-5, 180)
    turtle.circle(5, 180)
    turtle.setheading(270)
    turtle.circle(-5, 180)
    turtle.circle(5, 180)
    turtle.setheading(270)
    turtle.circle(-5, 180)

            
for i in range(20):
        x = random.randint(-180,180)
        y = random.randint(150, 200)
    
        turtle.pu()
        turtle.goto(x,y)
        turtle.pencolor("black")
        turtle.pd()
        turtle.setheading(90)
        turtle.circle(10, 180)
        turtle.pu()

turtle.hideturtle()



