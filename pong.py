import turtle as t
from random import randint

window = t.Screen()
window.title("Pong Light")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# ball speed
BALL_SPEED = .1

# left paddle

left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.color("white")
left_paddle.penup()
left_paddle.goto(-350, 0)


# right paddle

right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(350, 0)

# ball

ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_SPEED if randint(0,1000) % 2 == 0 else -1 * BALL_SPEED
ball.dy = -1 * BALL_SPEED if randint(0,9500) % 2 == 0  else BALL_SPEED

# functions for moving the left paddle

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


# functions for moving the right paddle

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


# Keyboard bindings

window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_up, "W")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(left_paddle_down, "S")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_up, "Down")



# Game Loop

while True:
    window.update()
    
    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #bound checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
    if ball.xcor() < -390:
        ball.goto(0,0)