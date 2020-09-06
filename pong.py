import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Pong")
wn.setup(800, 600)
wn.tracer(0)
windowWidth = 800
windowHeight = 600

class bat:
    bat = turtle.Turtle()
    bat.penup()
    bat.shape("square")
    bat.setx(0)
    bat.sety(-250)
    bat.shapesize(1,5)
    bat.color("black")
    bat.speed = 15

    def moveRight(self):
        x = self.bat.xcor()
        x += self.bat.speed
        self.bat.setx(x)

    def moveLeft(self):
        x = self.bat.xcor()
        x -= self.bat.speed
        self.bat.setx(x)


    def update(self):
        pass


class bat2:
    bat = turtle.Turtle()
    bat.penup()
    bat.shape("square")
    bat.setx(0)
    bat.sety(250)
    bat.shapesize(1,5)
    bat.color("black")
    bat.speed = 15

    def moveRight(self):
        x = self.bat.xcor()
        x += self.bat.speed
        self.bat.setx(x)

    def moveLeft(self):
        x = self.bat.xcor()
        x -= self.bat.speed
        self.bat.setx(x)

    def update(self):
        pass

class ball:
    ball = turtle.Turtle()
    ball.penup()
    ball.shape("circle")
    ball.setx(0)
    ball.sety(0)
    ball.color("black")
    ball.xspeed = 5
    ball.yspeed = 5

    def update(self):
        x = self.ball.xcor()
        x += self.ball.xspeed
        self.ball.setx(x)

        y = self.ball.ycor()
        y += self.ball.yspeed
        self.ball.sety(y)

class input:
    def update(self):
        pass

bat = bat()
bat2 = bat2()
ball = ball()

wn.listen()
wn.onkeypress(bat.moveRight, "Right")
wn.onkeypress(bat.moveLeft, "Left")

while True:
    wn.update()
    ball.update()
