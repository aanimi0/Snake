from turtle import Turtle

STARTING_X = -298
STARTING_Y = -298

class Borders(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.draw_border()

    def draw_border(self):
        self.goto(STARTING_X,STARTING_Y)
        self.pendown()
        for corners in range(0,4):
            self.forward((STARTING_X * -1) * 2)
            self.left(90)

