from duze_cyfry import daj_cyfre
from random import choice, randint
from turtle import Turtle, tracer

GRID_SIZE = 30
ITEM_WIDTH = 5
ITEM_HEIGHT = 5
grid = []
for i in range(GRID_SIZE):
    grid.append([])
for item in grid:
    for i in range(GRID_SIZE):
        item.append('-')

      


COLORS = {
    'r': 'red',
    'g': 'green',
    'b': 'blue',
    'y': 'yellow',
    "a": 'aqua'
}
COLORS_KEYS = list(COLORS.keys())


def print_grid(grid):
    for row in grid:
        for item in row:
            print(item, end='')
        print('')
    

def can_spawn(item, area,color, pos_x, pos_y):
    for y in range(pos_y, pos_y + ITEM_HEIGHT):
        for x in range(pos_x, pos_x+ ITEM_WIDTH):
            if item[y - pos_y][x - pos_x] == "#" and area[y][x] != '-':
                return False
            elif item[y - pos_y][x - pos_x] == "#" and y+1 < GRID_SIZE and area[y+1][x] == color:
                return False
            elif item[y - pos_y][x - pos_x] == "#" and x+1 < GRID_SIZE and area[y][x+1] == color:
                return False
            elif item[y - pos_y][x - pos_x] == "#" and y+1 < GRID_SIZE and x+1 < GRID_SIZE and area[y+1][x+1] == color:
                return False
            elif item[y - pos_y][x - pos_x] == "#" and pos_y > 0 and area[y-1][x] == color:
                return False
            elif item[y - pos_y][x - pos_x] == "#" and pos_x > 0 and area[y][x-1] == color:
                return False
    return True
    
def spawn(item, area, char, pos_x, pos_y): 
    for y in range(pos_y, pos_y + ITEM_HEIGHT):
        for x in range(pos_x, pos_x + ITEM_WIDTH):
            if item[y - pos_y][x - pos_x] == '#':
                area[y][x] = char 



def generate_grid(grid, numbers):
    for number in numbers:
        color = choice(COLORS_KEYS)
        number_array = daj_cyfre(number)
        x = randint(0, GRID_SIZE - ITEM_WIDTH)
        y = randint(0, GRID_SIZE - ITEM_HEIGHT)
        while not can_spawn(number_array, grid, color, x,y):
            x = randint(0, GRID_SIZE - ITEM_WIDTH)
            y = randint(0, GRID_SIZE - ITEM_HEIGHT)
        spawn(number_array, grid, color,x,y)

numbers = [randint(0,9) for x in range(25)]
generate_grid(grid,numbers)

t = Turtle()
t.speed(0)
t.penup()
tracer(0,1)

TURTLE_START_X = -200
TURTLE_START_Y = 300

def draw_square(x,y,color, size=10):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    t.penup()

def draw_grid(grid,square_size):
    t.setposition(TURTLE_START_X, TURTLE_START_Y)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] != '-':
                draw_square(TURTLE_START_X + x* square_size, TURTLE_START_Y - y * square_size, COLORS[grid[y][x]], square_size)
    input()


draw_grid(grid,15)