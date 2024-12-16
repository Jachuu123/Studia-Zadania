import random
from collections import Counter, defaultdict as dd

pol_ang = dd(lambda:[])

brown = dict()

for line in open('brown.txt','r', encoding='utf-8').readlines():
    for word in line.split():
        if word not in brown:
            brown.update({word: 1})
        else:
            brown[word]+=1


for x in open('pol_ang.txt','r', encoding='utf-8'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)
    
def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang: 
            selected = ''
            max_len = 0          
            for translation in pol_ang[s]:
                if translation in brown:
                    brown[translation] > max_len
                    max_len = brown[translation]
                    selected = translation
            wynik.append(selected)
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()

print(tlumacz(zdanie))          
        
