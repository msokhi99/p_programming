from turtle import Turtle

SCORETEXT="SCORE: "
GAMEOVERTEXT="GAME OVER"
RESTARTTEXT="PRESS SPACE TO RESTART"
ALIGN="center"
FONT=('Courier',12,'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.display_scoreboard()
    
    def display_scoreboard(self):
        self.write(arg=f"{SCORETEXT}{self.score} ",align=ALIGN,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.display_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"{GAMEOVERTEXT}",align=ALIGN,font=FONT)
    
    def restart_game(self):
        self.goto(0,-20)
        self.write(arg=f"{RESTARTTEXT}",align=ALIGN,font=FONT)