from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, skin_color="white"):
        self.segments = []
        self.skin_color = skin_color
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color(self.skin_color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self, animate=False):
        # Add new segment at the position of the last segment
        if animate:
            # Growth animation - scale up
            new_segment = self.segments[-1]
            original_size = 1.0
            for scale in [1.2, 1.4, 1.2, 1.0]:
                new_segment.shapesize(scale, scale)
                time.sleep(0.05)
        
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



