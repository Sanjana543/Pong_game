import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#paddleA
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

#paddleB
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx = 0.01
ball.dy = 0.01

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center",font =("Courier",24,"normal"))

#functions
def pad_a_up():
    y = pad_a.ycor()
    y += 40
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 40
    pad_a.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 40
    pad_b.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 40
    pad_b.sety(y)


#keys
wn.listen()
wn.onkeypress(pad_a_up,"w")
wn.onkeypress(pad_a_down,"s")
wn.onkeypress(pad_b_up,"Up")
wn.onkeypress(pad_b_down,"Down")

#main game loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + 2*ball.dx)
    ball.sety(ball.xcor() + 2*ball.dy)
    ball.rt(20)
    ball.lt(20)
    ball.dx += 0.001
    ball.dy += 0.001

    #border
    if ball.ycor() > 290:
        ball.sety(180*ball.dx)
        ball.dy *= -1
        ball.lt(50)
        ball.rt(50)
        winsound.PlaySound("Pim Poy.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety((-180)*ball.dx)
        ball.dy *= -1
        ball.lt(-50)
        ball.rt(-50)
        winsound.PlaySound("Pim Poy.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto((ball.dx*10),(ball.dy*5))
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),align="center",font=("Courier",24,"normal"))
        winsound.PlaySound("Pim Poy.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto((ball.dx*5),(ball.dy*7))
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("Pim Poy.wav", winsound.SND_ASYNC)

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(240)
        ball.dx *= -1

    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1