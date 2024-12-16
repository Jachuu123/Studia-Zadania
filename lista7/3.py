text = open('lalka.txt', 'r', encoding='utf-8').read()
sentences = text.replace('\n', ' ').split('.')

polish_signs = ['ę','ó', 'ą', 'ś', 'ł', 'ż' , 'ź', 'ć', 'ń']
def is_correct(msg):
    for sign in polish_signs:
        if sign in msg:
            return False
    return True

text_without_polish = []

for sentence in sentences:
    if is_correct(sentence):
        text_without_polish.append(sentence)

print(max(text_without_polish, key=len))
print(sorted(text_without_polish, key=len, reverse=True))
