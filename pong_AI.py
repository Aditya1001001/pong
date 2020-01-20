import turtle as t
from random import randint
import winsound

window = t.Screen()
window.title("Pong Light")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# scores
score_a = 0
score_b = 0


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


# ball speed
BALL_SPEED = .15

# ball
ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_SPEED if randint(0, 1000) % 2 == 0 else -1 * BALL_SPEED
ball.dy = -1 * BALL_SPEED if randint(0, 9500) % 2 == 0 else BALL_SPEED

# writing the score 
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player: {} | AI: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))


# functions for moving the left paddle
def left_paddle_up():
    y = left_paddle.ycor()
    y = y+20 if y < 250 else  250
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y = y-20 if y > -250 else  -250
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
# window.onkeypress(right_paddle_up, "Up")
# window.onkeypress(right_paddle_down, "Down")


# Game Loop
while True:
    window.update()

    # moving the right paddle on its own
    if ball.ycor() > right_paddle.ycor() + 50:
       right_paddle_up()        
    if ball.ycor() < right_paddle.ycor() - 50:
        right_paddle_down()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # bound checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",  winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player: {} | AI: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player: {} | AI: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))


    # collisions between paddles and ball
    if ball.xcor() > 330 and ball.xcor() < 350 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.xcor() < -330 and ball.xcor() > -350 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)