from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score :{self.score}", align="center", font=("Arial", 18, "normal"))

        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score :{self.score}  High Score :{self.high_score}", align="center", font=("Arial", 18, "normal"))

    def increase(self):

        self.score+=1
        self.update()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update()


    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 18, "normal"))


