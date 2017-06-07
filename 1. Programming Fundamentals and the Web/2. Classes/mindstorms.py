import turtle

def draw_regular_poly(turtle,sides):
    i=0
    angle = 360/sides
    while (i<sides):
        turtle.forward(100)
        turtle.right(angle)
        i=i+1

def draw_circle(turtle):
    turtle.circle(100)

def draw_multiple_squares(turtle,n):
    i=0
    while (i<n):
        draw_regular_poly(turtle,4)
        turtle.right(360/n)
        i=i+1
        
def start_program():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(50)

    draw_multiple_squares(brad,360)
##    draw_regular_poly(brad,4)
    
##    angie = turtle.Turtle()
##    angie.shape("turtle")
##    angie.color("blue")
##    angie.speed(2)
##    draw_circle(angie)
##    
##    draw_regular_poly(brad,3)
##    draw_regular_poly(brad,10)
    
    window.exitonclick()
    
start_program()
