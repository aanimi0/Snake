from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt",mode="r") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.write(arg=f"Score : {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)



    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1


