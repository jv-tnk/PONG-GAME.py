from turtle import Turtle
SHAPE = "square"


class Platform(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setheading(180)
        self.speed("fastest")
        self.goto(position)


    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
