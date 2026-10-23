import turtle
screen = turtle.Screen()
screen.title("Interactive Turtle Drawing")
t = turtle.Turtle()
t.speed(10)
def move_forward():
    t.forward(20)
def move_backward():
    t.backward(20)
def turn_left():
    t.left(30)
def turn_right():
    t.right(30)
def clear_screen():
    t.clear()
def reset_screen():
    t.reset()
def change_red():
    t.pencolor("red")
def change_green():
    t.pencolor("green")
def change_blue():
    t.pencolor("blue")
def change_white():
    t.pencolor("white")
def change_grey():
    t.pencolor("grey")
def change_yellow():
    t.pencolor("yellow")
def change_orange():
    t.pencolor("orange")
def change_black():
    t.pencolor("black")
def change_darkblue():
    t.pencolor("darkblue")
def change_brown():
    t.pencolor("brown")
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")
screen.onkey(reset_screen, "r")
screen.onkey(change_red,"1")
screen.onkey(change_green,"2")
screen.onkey(change_blue,"3")
screen.onkey(change_white,"0")
screen.onkey(change_grey,"5")
screen.onkey(change_yellow,"6")
screen.onkey(change_orange,"7")
screen.onkey(change_darkblue,"8")
screen.onkey(change_brown,"9")
screen.onkey(change_black,"4")
screen.mainloop()
