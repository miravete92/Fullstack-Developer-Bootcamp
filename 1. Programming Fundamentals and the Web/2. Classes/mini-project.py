import turtle

def draw_triangle(turtle,length):
    i=0
    while (i<3):
        turtle.forward(length)
        turtle.left(120)
        i=i+1

def draw_shape(turtle, iterations):
    i=0
    size=1
    while (i<iterations):
        j=0
        while (j<3):
            draw_triangle(turtle)
            j=j+1
        i=i+1
    
def start_program():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(3)

    draw_triangle(brad,30)

    
    window.exitonclick()
    
start_program()
