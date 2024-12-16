from turtle import *

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def kwadrat(bok):
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
    
def murek(s,bok):
  for a in s:
     if a == 'f':
         kwadrat(bok)
         fd(bok)
     elif a == 'b':
         kwadrat(bok)
         fd(bok)         
     elif a == 'l':
         bk(bok)
         lt(90)
     elif a == 'r':
        rt(90)
        fd(bok)
     elif 0 <= int(a) and int(a) < len(COLORS):
        color('black', COLORS[int(a)])

        
color('black', 'yellow')

ht()

tracer(0,0) # szybkie rysowanie     
# murek('ff0ffrfrf2ff4lflf3ffrfrf4ff',10)

for i in range(40):
    msg = 'r' + str(i % 6) + 'f'*(40-i)
    murek(msg, 10)
#murek('ff0ffrfrf2ff4lflf3ffrfrf4ff',10)


update() # uaktualnienie rysunku

input()
