from turtle import Turtle

t = Turtle()

t.speed(10.5)


def generate_figure(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

    t.right(60)
    t.forward(size)

    t.left(120)
    t.forward(size)
    t.right(60)


for i in range(10):
    generate_figure(80)
    t.right(36)


input()