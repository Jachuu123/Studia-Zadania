import math

def kolo(n,p):
    r = n//2
    for i in range(n):
        print(int(p)*" " ,end="")
        for j in range(n):
            if(i-r)**2 + (j-r)**2 <= r**2 + r:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def balwan(n1,n2,n3):
    kolo(n1,(n3-n2)/2 + (n2-n1)/2)
    kolo(n2,(n3-n2)/2)
    kolo(n3,0)


#kolo(9,0)

balwan(7,9,15)
