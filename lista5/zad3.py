import turtle
import random
from duze_cyfry import daj_cyfre


t = turtle.Turtle()
t.speed(0)


def print_square(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def print_number(number, x_start, y_start, size):
    arr = []
    while number > 0:
        arr.append(number % 10)
        number //= 10
    arr.reverse()

    colors = ["red", "green", "blue", "purple", "orange", "pink", "yellow"]  
    for i in arr:
        num = daj_cyfre(i)
        color = random.choice(colors)
        for i in range(5): 
            for j in range(5):  
                if num[i][j] == "#":
                    print_square(x_start + j * size, y_start - i * size, size, color)
        x_start += size*6



start_x = -300
start_y = 100
print_number(123456, -300,100, 20)
input()
