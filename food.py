import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        rx=random.randint(-280,280)
        ry=random.randint(-280,280)


        self.goto(x=rx,y=ry)

    def refresh(self):
        randomx=random.randint(-280,280)
        randomy = random.randint(-280, 280)
        self.goto(randomx,randomy)