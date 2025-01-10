a = [1,3,4,5,5,8]
b = [2,3,6,7,8,9]
len_a = len(a)
len_b = len(b)
res = []
i = 0
j = 0

while i < len_a and j < len_b:
    if a[i] < b[j]:
        res.append(a[i])
        i+=1
    else:
        res.append(b[j])
        j+=1

if i < len_a:
    res.append(a[i])
if j < len_b:
    res.append(b[j])

print(res)


