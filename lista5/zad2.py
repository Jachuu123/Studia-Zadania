import turtle
import random

t = turtle.Turtle()
t.speed(0)  




def draw_square(x, y, color, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()



start_x = -300
start_y = 300

grid_size = 4  
size = 20

light_max = 1
light_min = 0.8
dark_max = 0.2
dark_min = 0.3

def random_light_color():
    rand = random.randint(0,3)
    red_multiplier = 1
    green_multiplier = 1
    blue_multiplier = 1
    if rand == 0:
        red_multiplier = 0.7
    elif rand == 1:
        green_multiplier = 0.7
    elif rand == 2:
        blue_multiplier = 0.7
    return (red_multiplier * random.uniform(light_min, light_max), green_multiplier * random.uniform(light_min, light_max), blue_multiplier * random.uniform(light_min, light_max))


def random_dark_color():
    return (random.uniform(dark_min, dark_max), random.uniform(dark_min, dark_max), random.uniform(dark_min, dark_max))

for i in range(0, grid_size):
    for j in range(0, grid_size):
        is_light_block = True
        if (i + j) % 2 == 0:
            is_light_block = False
        for k in range(0, grid_size):
            for l in range(0, grid_size):
                x_pos = start_x + i * size * grid_size + k*size
                y_pos = start_y - j * size  * grid_size - l*size                   
                color = random_dark_color()
                if is_light_block:
                    color = random_light_color()
                draw_square(x_pos,y_pos, color, size)

       
   
input()




#  for col in range(0, grid, size):
#         is_light_block = (row // size + col // size) % 2 == 0

#         for i in range(size):
#             for j in range(size):
#                 if row + i < grid and col + j < grid:
#                     x = start_x + (col + j) * square
#                     y = start_y - (row + i) * square              
#                     color = random_dark_color()
#                     if is_light_block:
#                         color = random_light_color()
#                     draw_square(x, y, color, size)