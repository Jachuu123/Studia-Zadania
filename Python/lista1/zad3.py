def krzyzyk(n):
    for i in range(n):
        print(" " * n,end="")
        print("*" * n,end="")
        print(" " * n,end="")
        print()

    for i in range(n):
        print("*" * n * 3,end="")
        print()

    for i in range(n):
        print(" " * n, end="")
        print("*" * n, end="")
        print(" " * n, end="")
        print()

krzyzyk(10)