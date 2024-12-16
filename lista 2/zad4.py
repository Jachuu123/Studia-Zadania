from duze_cyfry import daj_cyfre

def display(n, spacing = 1):
    arr = str(n)
    for i in range(5):
        line = ""
        for j in arr:
            line += daj_cyfre(int(j))[int(i)]+" "*spacing
        print(line)


display(1257634,2)
print()
display(30737,5)