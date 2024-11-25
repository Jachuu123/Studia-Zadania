lines = set([line.strip() for line in open('popularne_slowa2023.txt', 'r', encoding='utf-8').readlines()])

res = set()
for line in lines:
    if line[::-1] in lines and (line[::-1], line) not in res and line != line[::-1]:
        res.add((line, line[::-1]))

print(res)