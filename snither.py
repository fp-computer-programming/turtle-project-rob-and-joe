# Creator JM and RD 3/17/23
import turtle as t
import time
import random

orange_wins = 0 # Variables to keep track of score
blue_wins = 0
font = ('Comic Sans', 18, 'bold') # Score font

window = t.Screen() # Turtle Window Setup
window.bgcolor('green')
window.title('Snither')
window.setup(500, 500)

snake = t.Turtle('square') # Create player 1's turtle (blue)
snake.color('light blue')
snake.penup()
snake.speed(0)

snake2 = t.Turtle('square') # Create player 2's turtle (orange)
snake2.setheading(180.0) # make him face the opposite way as player 1
snake2.color('orange')
snake2.penup()
snake2.speed(0)


pieces = [] # keep track of body pieces for the two players
pieces2 = []


def update_score(): # update the score on the top of the screen
    global orange_wins, blue_wins

    snake.goto(-200, 200)
    snake.pendown()
    snake.color('green')
    snake.begin_fill()
    snake.setheading(0.0)
    for z in range(4):
        snake.forward(350)
        snake.left(90)
    snake.end_fill()

    snake.color('white')
    snake.penup()
    snake.goto(0, 200)
    snake.pendown()
    snake.write(f"Blue: {blue_wins} | Orange: {orange_wins}", align='center', font=font)
    snake.penup()
    snake.goto(0, 0)
    snake.color('light blue')


# Movement controls ----------
def go_down():
    if snake.heading() != 90.0:
        snake.setheading(270.0)


def go_left():
    if snake.heading() != 0.0:
        snake.setheading(180.0)


def go_up():
    if snake.heading() != 270.0:
        snake.setheading(90.0)


def go_right():
    if snake.heading() != 180.0:
        snake.setheading(0)


def go_down2():
    if snake2.heading() != 90.0:
        snake2.setheading(270.0)


def go_left2():
    if snake2.heading() != 0.0:
        snake2.setheading(180.0)


def go_up2():
    if snake2.heading() != 270.0:
        snake2.setheading(90.0)


def go_right2():
    if snake2.heading() != 180.0:
        snake2.setheading(0)

# Move the snake --------
def move():
    if snake.heading() == 90.0:
        snake.forward(12)
    else:
        snake.forward(10)


def move2():
    if snake2.heading() == 90.0:
        snake2.forward(12)
    else:
        snake2.forward(10)

def add_apples(): # add red apples on the screen in a random position
    global apple
    apple = t.Turtle('circle')
    apple.color('red')
    apple.penup()
    apple.hideturtle()
    apple.setposition(random.randint(-250, 250), random.randint(-250, 250))
    apple.showturtle()


# Add body pieces to the snake when it eats an apple
def grow():
    global delay
    for x in range(0,2): # add two body pieces at a time (makes the game faster)
        body = t.Turtle() 
        body.color('light blue')
        body.hideturtle()
        body.penup()
        body.speed(0)
        body.shape('square')
        pieces.append(body) # add to pieces list

    if (delay - 0.01) > 0.02:
        delay -= 0.001

def grow2(): # same as above but for player 2
    global delay
    for x in range(0,2):
        body2 = t.Turtle()
        body2.color('orange')
        body2.hideturtle()
        body2.penup()
        body2.speed(0)
        body2.shape('square')
        pieces2.append(body2)

    if (delay - 0.01) > 0.02:
        delay -= 0.001


def restart(): # restart the game when it is over
    global score, i, x, delay
    time.sleep(2) # let the player take it in
    update_score() # update the score
    score = 0
    snake.goto(0, 0)
    for body in pieces: # get rid of the old body pieces
        body.hideturtle()
    pieces.clear()

    snake2.goto(0, 0)
    for body in pieces2:
        body.hideturtle()
    pieces2.clear()

    delay = 0.05 # reset variables
    i = 0
    x = 0


def restartscore(): # reset the score variables (can be done by pressing C)
    global orange_wins, blue_wins
    orange_wins = 0
    blue_wins = 0
    update_score()
    restart()


def pause(): # pause the game by creating a text input
    window.textinput('Paused', 'Press OK to resume.')
    window.listen()


# Key assignments ----------
window.listen()

# Player 1 movement
window.onkeypress(go_down, 'Down')
window.onkeypress(go_up, 'Up')
window.onkeypress(go_right, 'Right')
window.onkeypress(go_left, 'Left')

# Player 2 movement
window.onkeypress(go_down2, 's')
window.onkeypress(go_up2, 'w')
window.onkeypress(go_right2, 'd')
window.onkeypress(go_left2, 'a')

# Extra functions
window.onkeypress(restartscore,'c')
window.onkeypress(pause, 'space')

i = 0
x = 0


add_apples() # add the starting apple

delay = 0.05 # game delay (how fast it goes)

while True:
    t.tracer(0, 0) # turn turtle animation off so we can draw everything off-screen

    move() # move the two snakes
    move2()

    time.sleep(delay) # sleep

    # Check if snakes have gone out of bounds ----------
    if snake.xcor() >= 250.00 or snake.xcor() <= -250.00:
        orange_wins += 1
        restart()

    if snake.ycor() >= 250.00 or snake.ycor() <= -250.00:
        orange_wins += 1
        restart()

    if snake2.xcor() >= 250.00 or snake2.xcor() <= -250.00:
        blue_wins += 1
        restart()

    if snake2.ycor() >= 250.00 or snake2.ycor() <= -250.00:
        blue_wins += 1
        restart()

    # Check if snakes have eaten the apple
    if snake.distance(apple) <= 20:
        grow()
        apple.hideturtle()
        apple.setposition(
            random.randint(-240, 240), random.randint(-240, 240))
        apple.showturtle()

    if snake2.distance(apple) <= 20:
        grow2()
        apple.hideturtle()
        apple.setposition(
            random.randint(-240, 240), random.randint(-240, 240))
        apple.showturtle()

    # Check if a snake has run into the other snake's body or its own body
    for body in pieces2:
        if snake2.distance(body) <= 4:
            restart()
        if snake.distance(body) <= 4:
            orange_wins += 1
            restart()
    
    for body in pieces:
        if snake.distance(body) <= 4:
            restart()
        if snake2.distance(body) <= 4:
            blue_wins += 1
            restart()

    # Move the body pieces with the snake
    if len(pieces) > 0:
        pieces[i].setposition(snake.xcor(), snake.ycor())
        pieces[i].showturtle()
        i += 1
        if i > len(pieces) - 1:
            i = 0

    if len(pieces2) > 0:
        pieces2[x].setposition(snake2.xcor(), snake2.ycor())
        pieces2[x].showturtle()
        x += 1
        if x > len(pieces2) - 1:
            x = 0

    # Show the game
    t.update()

# Done!!! :)
