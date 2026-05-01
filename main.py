from turtle import Turtle, Screen
from snakecode import Snake
from food import Food
from score import Scoreboard
import time
import winsound

# Global pause state
game_paused = False
pause_display = None
theme_colors = {
    "green": {"snake": "lime", "food": "red", "bg": "black"},
    "blue": {"snake": "cyan", "food": "yellow", "bg": "navy"},
    "purple": {"snake": "magenta", "food": "white", "bg": "indigo"}
}

def get_difficulty():
    """Ask user for difficulty selection with validation"""
    valid_difficulties = ["easy", "medium", "hard"]
    difficulty = None
    error_display = Turtle()
    error_display.penup()
    error_display.hideturtle()
    error_display.color("red")
    
    while difficulty not in valid_difficulties:
        user_input = screen.textinput("Difficulty", "Choose difficulty: easy, medium, or hard").lower()
        if user_input in valid_difficulties:
            difficulty = user_input
            error_display.clear()
        else:
            error_display.goto(0, -250)
            error_display.clear()
            error_display.write(f"Invalid input '{user_input}' Enter: easy, medium, or hard", align="center", font=("Arial", 12, "normal"))
            screen.update()
    
    error_display.clear()
    return difficulty

def get_theme():
    """Ask user for color theme selection"""
    theme = None
    theme_list = list(theme_colors.keys())
    theme_prompt = f"Choose theme: {', '.join(theme_list)}"
    
    while theme not in theme_colors:
        theme = screen.textinput("Theme Selection", theme_prompt).lower()
        if theme not in theme_colors:
            screen.textinput("Invalid Theme", f"Please choose: {', '.join(theme_list)}")
    
    return theme

def get_delay(difficulty):
    """Get delay based on difficulty level"""
    if difficulty == "easy":
        return 0.15  # Slower
    elif difficulty == "hard":
        return 0.07  # Faster
    else:
        return 0.1   # Medium

def draw_grid():
    """Draw grid on background"""
    grid = Turtle()
    grid.speed(0)
    grid.color("gray")
    grid.pensize(1)
    grid.hideturtle()
    
    # Draw vertical lines
    for x in range(-300, 300, 20):
        grid.penup()
        grid.goto(x, -300)
        grid.pendown()
        grid.goto(x, 300)
    
    # Draw horizontal lines
    for y in range(-300, 300, 20):
        grid.penup()
        grid.goto(-300, y)
        grid.pendown()
        grid.goto(300, y)
    
    grid.penup()
    return grid

def toggle_pause():
    """Toggle pause state and display pause message"""
    global game_paused, pause_display
    
    game_paused = not game_paused
    
    if pause_display is None:
        pause_display = Turtle()
        pause_display.penup()
        pause_display.hideturtle()
        pause_display.color("yellow")
    
    pause_display.clear()
    if game_paused:
        pause_display.goto(0, 0)
        pause_display.write("PAUSED", align="center", font=("Arial", 30, "bold"))
        winsound.Beep(800, 200)  # Pause sound
    else:
        pause_display.clear()
        winsound.Beep(600, 200)  # Resume sound

def play_sound(sound_type):
    """Play sound effects"""
    try:
        if sound_type == "food":
            winsound.Beep(1000, 100)  # High beep for food
        elif sound_type == "collision":
            winsound.Beep(200, 300)   # Low beep for collision
        elif sound_type == "game_over":
            winsound.Beep(400, 500)   # Game over sound
    except:
        pass  # Silent fail if sound not available

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Adventure")
screen.tracer(0)

difficulty = get_difficulty()
theme = get_theme()
delay = get_delay(difficulty)
colors = theme_colors[theme]

def play_game():
    """Main game loop"""
    global screen, running, game_paused, pause_display
    
    game_paused = False
    pause_display = None
    
    # Apply theme
    screen.bgcolor(colors["bg"])
    
    # Draw grid
    grid = draw_grid()
    
    snake = Snake(skin_color=colors["snake"])
    food = Food(food_color=colors["food"])
    score = Scoreboard()
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(toggle_pause, "space")
    
    running = True
    blink_counter = 0
    
    while running:
        screen.update()
        
        # Food blink animation
        blink_counter += 1
        if blink_counter % 20 == 0:
            food.toggle_visibility()
        
        # Skip game logic if paused
        if not game_paused:
            time.sleep(delay)
            snake.move_snake()
            
            if snake.head.distance(food) < 15:
                food.refresh()
                food.show()
                snake.extend(animate=True)
                score.incr_score()
                play_sound("food")
            
            # Detect collision with wall
            if (
                snake.head.xcor() > 290 or
                snake.head.xcor() < -290 or
                snake.head.ycor() > 290 or
                snake.head.ycor() < -290
            ):
                running = False
                play_sound("collision")
                score.game_over()
            
            # Detect collision with tail
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    running = False
                    play_sound("collision")
                    score.game_over()
        else:
            time.sleep(0.1)
    
    play_sound("game_over")


play_game()

screen.exitonclick()
