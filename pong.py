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

    def moveRight(self):
        x = self.bat.xcor()
        x += 15
        self.bat.setx(x)

    def moveLeft(self):
        x = self.bat.xcor()
        x -= 15
        self.bat.setx(x)


    def update(self):
        pass


class bat2:
    bat2 = turtle.Turtle()
    bat2.penup()
    bat2.shape("square")
    bat2.setx(0)
    bat2.sety(250)
    bat2.shapesize(1,5)
    bat2.color("black")

    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def update(self):
        pass

class ball:
    ball = turtle.Turtle()
    ball.penup()
    ball.shape("circle")
    ball.setx(0)
    ball.sety(0)
    ball.color("black")

    def update(self):
        pass

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
    
