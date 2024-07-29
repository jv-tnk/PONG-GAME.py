from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.down = False
        self.left = False


    def move(self):
        if self.left:
            new_x = self.xcor() - 1
        else:
            new_x = self.xcor() + 1
        if self.down:
            new_y = self.ycor() - 1
        else:
            new_y = self.ycor() + 1
        self.goto(new_x, new_y)

    def change_color(self,color):
        self.color(color)


