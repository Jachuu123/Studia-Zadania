def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def get_energy(n):
    a = n
    arr = [a]
    while 1 not in arr:
        a = F(a)
        arr.append(a)

    return len(arr) - 1


def mediane(arr):
    temp = arr[::]
    temp.sort()
    length = len(temp)
    if length % 2 == 1:
        return temp[length // 2]
    return temp[length//2- 1] / 2 + temp[length//2] /2 


def collatz_analysis(a,b):
    values = [get_energy(v) for v in range(a,b+1)]    
    print("Average: ", sum(values) / len(values))
    print("Mediane: ", mediane(values))
    print("Minimal: ", min(values))
    print("Maximal: ", max(values))


collatz_analysis(10,15)