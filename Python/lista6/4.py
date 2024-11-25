def custom_split(text, divider = ' '):
    result = []
    current = ''
    for char in text:
        if char == divider:
            if len(current):
                result.append(current)
                current = ''
        else:
            current+=char
    if len(current):
        result.append(current)
    return result

print(custom_split('Ala ma kota i psa ale nie ma małpy'))