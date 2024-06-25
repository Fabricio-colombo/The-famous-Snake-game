from turtle import Screen, Turtle
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

start_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in start_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

food = Turtle("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

def move():
    global segments
    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)
    segments[0].forward(20)

screen.listen()
screen.onkey(lambda: segments[0].setheading(90), "Up")
screen.onkey(lambda: segments[0].setheading(270), "Down")
screen.onkey(lambda: segments[0].setheading(0), "Right")
screen.onkey(lambda: segments[0].setheading(180), "Left")

game_is_on = True
while game_is_on:
    screen.update()
    move()
    time.sleep(0.1)

    head_x = segments[0].xcor()
    head_y = segments[0].ycor()
    if head_x > 290 or head_x < -290 or head_y > 290 or head_y < -290:
        game_is_on = False
        print("Game Over - Colidiu com as bordas!")

    if segments[0].distance(food) < 20:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        food.goto(random.randint(-290, 290), random.randint(-290, 290))

screen.exitonclick()
