import turtle
import math
def draw_triangle(turtle,length,fill):
    i=0
    if (fill):
        turtle.fill(True)
    while (i<3):
        turtle.forward(length)
        turtle.left(120)
        i=i+1
    if (fill):
        turtle.fill(False)
def draw_fractal(turtle, iteration, size):
    if (iteration>0):
        draw_fractal(turtle,iteration-1,size/2)
        turtle.left(60)
        turtle.forward(size/2)
        turtle.right(60)
        draw_fractal(turtle,iteration-1,size/2)
        turtle.right(120)
        turtle.forward(size/2)
        turtle.left(120)
        turtle.forward(size/2)
        draw_fractal(turtle,iteration-1,size/2)
        turtle.right(180)
        turtle.forward(size/2)
        turtle.right(180)
    else:
        draw_triangle(turtle,size,True)

#levels: number of levels of recursivity
#size: size of the greatest triangle

def start_program(levels,size):
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("blue")
    brad.fillcolor("green")
    brad.speed(100)
    
    #center triangle on screen
    brad.up()
    brad.setx(-size/2)
    brad.sety(-(size/2*math.sqrt(3))/2)
    brad.down()
    
    draw_fractal(brad,levels,size)

    
    window.exitonclick()
    
start_program(8,1000)
