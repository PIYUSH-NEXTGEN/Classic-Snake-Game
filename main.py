from turtle import Turtle, Screen
from snakecode import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Adventure")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

running = True
while running:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.incr_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290 or
        snake.head.xcor() < -290 or
        snake.head.ycor() > 290 or
        snake.head.ycor() < -290
    ):
        running = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            running = False
            score.game_over()

screen.exitonclick()


