from math import sqrt

def circle(n, offset = 0):
    radius = n / 2
    for i in range(n):
        line = " "*offset
        for j in range(n):
            distance = sqrt((i - radius + 0.5) ** 2 + (j - radius + 0.5) ** 2)
            if distance < radius:
                line += "#"
            else:
                line += " "
        print(line)

print("--- Bałwan --- \n")
circle(5,4)
circle(9,2)
circle(13)