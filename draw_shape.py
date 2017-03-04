import turtle


def draw_shape():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    franklin = turtle.Turtle()
    franklin.shape("turtle")
    franklin.color("green")
    franklin.speed(10)
    f_count = 0

    while f_count < 4:
        franklin.forward(100)
        franklin.right(90)
        f_count = f_count + 1
    
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    brad.circle(100)

    angie = turtle.Turtle()
    angie.shape("classic")
    angie.color("red")
    a_count = 0

    while a_count < 3:
        angie.forward(100) 
        angie.left(120)
        a_count = a_count + 1
            
    window.exitonclick()
    
draw_shape()
