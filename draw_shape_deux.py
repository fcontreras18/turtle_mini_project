import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("yellow")

    franklin = turtle.Turtle()
    franklin.shape("turtle")
    franklin.color("green")
    franklin.speed(0)
    
    for i in range(1,37):
        draw_square(franklin)
        franklin.right(10)
    

    #brad = turtle.Turtle()
    #brad.shape("arrow")
    #brad.color("blue")
    #brad.circle(100)

    #angie = turtle.Turtle()
    #angie.shape("classic")
    #angie.color("red")
    #a_count = 0

    #while a_count < 3:
    #    angie.forward(100) 
    #    angie.left(120)
    #    a_count = a_count + 1
            
    window.exitonclick()

draw_shape()
