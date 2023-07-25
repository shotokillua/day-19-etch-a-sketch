from turtle import Turtle, Screen

tam = Turtle()
screen = Screen()

def move_forward():
  tam.forward(10)

def move_backward():
  tam.backward(10)

def turn_left():
  tam.left(10)

def turn_right():
  tam.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=screen.clear)


screen.mainloop()
# screen.exitonclick
