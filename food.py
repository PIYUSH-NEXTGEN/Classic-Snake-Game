from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, food_color="red"):
        super().__init__()
        self.food_color = food_color
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.food_color)
        self.speed("fastest")
        self.is_visible = True
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def toggle_visibility(self):
        """Toggle food visibility for blinking animation"""
        self.is_visible = not self.is_visible
        if self.is_visible:
            self.color(self.food_color)
        else:
            self.color("black")  # Blend with background

    def show(self):
        """Make food visible"""
        self.is_visible = True
        self.color(self.food_color)



