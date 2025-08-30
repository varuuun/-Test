import turtle
import time

WIDTH, HEIGHT = 800, 600
PADDLE_MOVE = 30
BALL_SPEED = 5

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-WIDTH // 2 + 50, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(WIDTH // 2 - 50, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_SPEED
ball.dy = BALL_SPEED

score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, HEIGHT // 2 - 40)
pen.write("0 : 0", align="center", font=("Courier", 24, "normal"))


def update_score():
    pen.clear()
    pen.write(f"{score_a} : {score_b}", align="center", font=("Courier", 24, "normal"))


def move_paddle(paddle, delta):
    y = paddle.ycor() + delta
    max_y = HEIGHT // 2 - 50
    if y > max_y:
        y = max_y
    if y < -max_y:
        y = -max_y
    paddle.sety(y)


def paddle_a_up():
    move_paddle(paddle_a, PADDLE_MOVE)


def paddle_a_down():
    move_paddle(paddle_a, -PADDLE_MOVE)


def paddle_b_up():
    move_paddle(paddle_b, PADDLE_MOVE)


def paddle_b_down():
    move_paddle(paddle_b, -PADDLE_MOVE)


running = True


def quit_game():
    global running
    running = False


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(quit_game, "q")
wn.onkeypress(quit_game, "Escape")


while running:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > HEIGHT / 2 - 10:
        ball.sety(HEIGHT / 2 - 10)
        ball.dy *= -1

    if ball.ycor() < -HEIGHT / 2 + 10:
        ball.sety(-HEIGHT / 2 + 10)
        ball.dy *= -1

    if ball.xcor() > WIDTH / 2 - 10:
        score_a += 1
        update_score()
        ball.goto(0, 0)
        ball.dx = -BALL_SPEED
        ball.dy = BALL_SPEED if ball.dy > 0 else -BALL_SPEED

    if ball.xcor() < -WIDTH / 2 + 10:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        ball.dx = BALL_SPEED
        ball.dy = BALL_SPEED if ball.dy > 0 else -BALL_SPEED

    right_center_x = WIDTH // 2 - 50
    left_center_x = -WIDTH // 2 + 50

    if (
        right_center_x - 20 < ball.xcor() < right_center_x
        and abs(ball.ycor() - paddle_b.ycor()) <= 50
    ):
        ball.setx(right_center_x - 20)
        ball.dx *= -1

    if (
        left_center_x < ball.xcor() < left_center_x + 20
        and abs(ball.ycor() - paddle_a.ycor()) <= 50
    ):
        ball.setx(left_center_x + 20)
        ball.dx *= -1

    time.sleep(0.01)

try:
    wn.bye()
except turtle.Terminator:
    pass
