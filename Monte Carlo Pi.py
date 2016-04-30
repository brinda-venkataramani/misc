"""
Approximation of pi by Monte Carlo implementation.
2016-04-30
"""

import random

r=2
n=100000
hits=0

"""
Simulates a game where rocks are thrown into a square with a circle inscribed within.
Ratio of hits (throws inside the circle) to number of throws is given by the ratio of the area of the circle to the square.
That is, pi*r^2/4r^2=pi/4.
"""

for i in range(n):
    x=random.uniform(-2,2)
    y=random.uniform(-2,2)
    if x**2+y**2<=r**2:
        hits = hits + 1

# To return pi, multiply the ratio by 4.

print 4*float(hits)/n
