# Scripted minesweeper implementation. Will do graphics soon.
# Kinda pointless, but whatever. I like minesweeper.

def countMines(space):
    c = 0
    if field[space] == 1:
        return c
    elif field[space] !=1:
        if field[space-13]==1:
            c=c+1
        if field[space-12]==1:
            c=c+1
        if field[space-11]==1:
            c=c+1
        if field[space-1]==1:
            c=c+1
        if field[space+1]==1:
            c=c+1
        if field[space+11]==1:
            c=c+1
        if field[space+12]==1:
            c=c+1
        if field[space+13]==1:
            c=c+1
        return c

import random
from random import choice
field = []
mines = []
for i in range(144):
    field.append(0)
c = 0
while c < 15:
    r = choice([random.randint(13,22),random.randint(25,34),random.randint(37,46),random.randint(49,58),random.randint(61,70),random.randint(73,82),random.randint(85,94),random.randint(97,106),random.randint(109,118),random.randint(121,130)])
    print r
    if r not in mines:
        mines.append(r)
        c = c + 1
for mine in mines:
    field[mine] = 1

pused = []
loop = 9999
while loop!=0:
    p = int(raw_input("Enter a position: "))
    if p not in pused:
        pused.append(p)
    else:
        print "Already selected."
    loop = countMines(p)

print "Thanks for playing!"
