from turtle import Turtle

class Division(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(5)
        self.pencolor("white")
        self.goto(0, 405)
        self.pendown()
        self.goto(0, -405)
