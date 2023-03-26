import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(10)
t.pensize(2)
t.pencolor("white")



def s_curve():
    for i in range(90):
        t.left(1)
        t.forward(1)

def r_curve():
    for i in range(90):
        t.right(1)
        t.forward(1)

def l_curve():
    s_curve()
    t.forward(80)
    s_curve()

def l_curve1():
    s_curve()
    t.forward(90)
    s_curve()

def half():
    t.forward(50)
    s_curve()
    t.forward(90)
    l_curve()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(120) #on test
    l_curve1()
    t.forward(30)
    t.left(90)
    t.forward(50)
    r_curve()
    t.forward(40)
    t.end_fill()

def get_pos():
    t.penup()
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.pendown()

def eye():
    t.penup()
    t.right(90)
    t.forward(160)
    t.left(90)
    t.forward(70)
    t.pencolor("black")
    t.dot(35)

def sec_dot():
    t.left(90)
    t.penup()
    t.forward(310)
    t.left(90)
    t.forward(120)
    t.pendown()

    t.dot(35)




t.fillcolor("#306998")
t.begin_fill()
half()
t.end_fill()
get_pos()
t.fillcolor("#FFD43B")
t.begin_fill()
half()
t.end_fill()

eye()
sec_dot()



def pause():
    t.speed(2)
    for i in range(100):
        t.left(90)
pause(shuyer 1-logo)

import turtle
#get the instance of turtle
t=turtle.Turtle()
#select color
t.color('#4285F4','#4285F4') ## RBG value of color
#change the pen size
t.pensize(5)
#change the drawing speed
t.speed(3)

t.forward(120)
t.right(90)
t.circle(-150,50)  ## first circle for red color
t.color('#0F9D58')
t.circle(-150,100)
t.color('#F4B400')
t.circle(-150,60)
t.color('#DB4437','#DB4437')

t.begin_fill()
t.circle(-150,100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(100,100)
t.right(90)
t.forward(50)
t.end_fill()

t.begin_fill()

## second circle for yellow color

t.color("#F4B400","#F4B400")
t.right(180)
t.forward(50)
t.right(90)

t.circle(100,60)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150,60)
t.end_fill()


# third circle of green color
t.right(90)
t.forward(50)
t.right(90)
t.circle(100,60)
t.color('#0F9D58','#0F9D58')
t.begin_fill()
t.circle(100,100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150,100)
t.right(90)
t.forward(50)
t.end_fill()


##Draw last circle

t.right(90)
t.circle(100,100)
t.color('#4285F4','#4285F4')
t.begin_fill()
t.circle(100,25)
t.left(115)
t.forward(65)
t.right(90)
t.forward(42)
t.right(90)
t.forward(124)
t.right(90)
t.circle(-150,50)
t.right(90)
t.forward(50)

t.end_fill()
t.penup(buyer 2-logo)
