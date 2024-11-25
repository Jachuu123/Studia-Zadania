def szachownica(n, k):
    for i in range(n):
        #if i%2 == 0:
            for j in range(k):
                print(n * ((k * " ") + (k * "#")), end="")
                #print("A", end="")
                print()
        #else:
            for j in range(k):
                print(n * ((k * "#") + (k * " ")), end="")
                #print("A", end="")
                print()

szachownica(5,5)
