import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    i=4
    while (i>0):
        brad.forward(100)
        brad.right(90)
        i=i-1
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    dwar=turtle.Turtle()
    dwar.shape("turtle")
    dwar.color("green")
    dwar.forward(320)
    dwar.left(120)
    dwar.forward(320)
    dwar.left(120)
    dwar.forward(320)
    dwar.left(120)
    window.exitonclick()

draw_square()    
        
