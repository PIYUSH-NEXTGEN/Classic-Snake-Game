from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
SMALL_FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                high_score = int(file.read())
                return high_score
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(280, 270)
        self.write(f"High Score: {self.high_score}", align="right", font=SMALL_FONT)

    def incr_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        # Update high score if current score is higher
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", align=ALIGNMENT, font=SMALL_FONT)

