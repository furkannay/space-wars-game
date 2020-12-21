# SPACE WARS GAME
## Introduction to engineering project
###### Furkan Ay & Zafer Yılmaz
This game is a space combat game. 
You have a space shuttle and you try to destroy the aliens.

You move the ship with the right and left keys. 

You shoot with the spacebar.

If you destroy all aliens you win.

This game for 1 people.

<img src="https://user-images.githubusercontent.com/74255322/102798779-c65fd480-43db-11eb-9db8-e6ccc8f2cca1.png">

## **REQUIREMENTS**

space wars code.py

necessary pictures and sound files

python 3

# CODE
firstly we import our module
```
import turtle
import random
import winsound
```

After we are set window
```
window = turtle.Screen()
window.bgcolor('black')
window.title('Space Battle')
window.bgpic('space.gif')
window.setup(width=600, height=600)
```
We introduce our additional files to the program

```
turtle.register_shape('player.gif')
turtle.register_shape('enemy.gif')
turtle.register_shape('shoot.gif')
```
We are set object of player
```
player = turtle.Turtle()
player.color('blue')
player.speed(0)
player.shape('player.gif')
player.setheading(90)
player.penup()
player.goto(0, -250
player_speed = 20
```
we are create object of shoot
```
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
```
We are create result writing

```
result = turtle.Turtle()
result.color('white')
result.speed(0)
result.penup()
result.goto(0, 200)
result.hideturtle()
```
Now we are defined function of moves and shoot

```
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
```
Now create target.

```
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
```
Now we command the window
```
window.listen()
window.onkey(go_left, 'Left')
window.onkey(go_right, 'Right')
window.onkey(go_up, 'Up')
window.onkey(go_down, 'Down')
window.onkey(fire_it, 'space')
```
We are set gaming
```
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
```
That's all


