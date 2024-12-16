def koperta(n):
    size = 2 * n + 1
    
    for i in range(size):
        line = ""
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                line += "*"
            elif i == j or i + j == size - 1:
                line += "*"
            else:
                line += " "
        print(line)

koperta(4)