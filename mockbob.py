# Program which outputs Spongebob meme text for any inputted text.

import math # For floor function.
import random # For randint function.

# Capitalize a given letter in a list.

def cap(s,n):
  s[n] = s[n].upper()
  return s

msg = raw_input('Enter message: ')
msg_lst = list(msg)

n = int(math.floor(3*len(msg)/4))
c = 0
lst = []

while c < n:
  while True:
    x = random.randint(0,len(msg)-1)
    if x not in lst:
      lst.append(x)
      break
  msg_lst = cap(msg_lst,x)
  c = c + 1

final = ""
for item in msg_lst:
  final = final + item

print final
