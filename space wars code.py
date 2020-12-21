import turtle
import random
import winsound

window = turtle.Screen()
window.bgcolor('black')
window.title('Space Battle')
window.bgpic('space.gif')
window.setup(width=600, height=600)

turtle.register_shape('player.gif')
turtle.register_shape('enemy.gif')
turtle.register_shape('shoot.gif')

player = turtle.Turtle()
player.color('blue')
player.speed(0)
player.shape('player.gif')
player.setheading(90)
player.penup()
player.goto(0, -250)
player_speed = 20

fire = turtle.Turtle()
fire.color('yellow')
fire.speed(0)
fire.shape('shoot.gif')
fire.setheading(90)
fire.penup()
fire.goto(0, -240)
fire_speed = 20
fire.hideturtle()
fire.turtlesize(1, 1)
fire_control = False

result = turtle.Turtle()
result.color('white')
result.speed(0)
result.penup()
result.goto(0, 200)
result.hideturtle()


def fire_go():
    y = fire.ycor()
    y = y + fire_speed
    fire.sety(y)


def go_left():
    x = player.xcor()
    x = x - player_speed
    if x < -300:
        x = -300
    player.setx(x)


def go_right():
    x = player.xcor()
    x = x + player_speed
    if x > 300:
        x = 300
    player.setx(x)


def go_up():
    y = player.ycor()
    y = y + player_speed
    if y > 270:
        y = 270
    player.sety(y)


def go_down():
    y = player.ycor()
    y = y - player_speed
    if y < -270:
        y = -270
    player.sety(y)


def fire_it():
    global fire_control
    winsound.PlaySound('fire.wav', winsound.SND_ASYNC)
    x = player.xcor()
    y = player.ycor() + 20
    fire.goto(x, y)
    fire.showturtle()
    fire_control = True


targets = []
for i in range(7):
    targets.append(turtle.Turtle())
for target in targets:
    target.color('red')
    target.speed(0)
    target.turtlesize(1, 1)
    target.shape('enemy.gif')
    target.penup()
    target.setheading(90)
    x = random.randint(-280, 280)
    y = random.randint(180, 260)
    target.goto(x, y)

window.listen()
window.onkey(go_left, 'Left')
window.onkey(go_right, 'Right')
window.onkey(go_up, 'Up')
window.onkey(go_down, 'Down')
window.onkey(fire_it, 'space')

while True:
    if fire_control:
        fire_go()
    for target in targets:
        y = target.ycor()
        y = y - 2
        target.sety(y)
        if target.distance(fire) < 20:
            fire.hideturtle()
            target.hideturtle()
            targets.pop(targets.index(target))
            winsound.PlaySound('boom.wav', winsound.SND_ASYNC)
        if target.ycor() < -270 or target.distance(player) < 20:
            result.write('Sorry, You Lost!', align='center', font=('Courier', 24, 'bold'))
    if len(targets) == 0:
        result.write('Well Done, You Won!', align='center', font=('Courier', 24, 'bold'))