from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.points = 0

    def refresh(self, color,position):
        self.clear()
        self.pencolor(color)
        self.goto(position)
        self.write(arg=f"{self.points}", font=("Arial", 100, "normal"))

    def point(self, player):
        self.points += 1
        if player == "p1":
            self.refresh(color="red", position=(-120, 250))
        else:
            self.refresh(color="blue", position=(40, 250))

class ScoreboardP1(Scoreboard):
    def __init__(self):
        super().__init__()
        self.refresh(color="red", position=(-120, 250))


class ScoreboardP2(Scoreboard):
    def __init__(self):
        super().__init__()
        self.refresh(color="blue", position=(40, 250))
