def remove_duplicates(L):
    L.sort()
    res = []

    for i in range(len(L)):
        if i == 0 or L[i] != L[i - 1]:
            res.append(L[i])
    return res

print(remove_duplicates([1, 2, 3, 1, 2, 3, 8, 2, 2,19,10, 2, 9, 9, 9, 4, 10]))
