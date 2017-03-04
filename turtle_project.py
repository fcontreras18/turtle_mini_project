import turtle

def draw_diamond(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.left(45)
        some_turtle.forward(100) 
        some_turtle.left(135)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("yellow")

    franklin = turtle.Turtle()
    franklin.shape("turtle")
    franklin.color("green")
    franklin.speed(0)

    for i in range(1,37):
        draw_diamond(franklin)
        franklin.right(10)
    franklin.right(90)
    franklin.forward(250)
    
    window.exitonclick()

draw_shape()
