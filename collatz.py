# Collatz conjecture (3x+1 problem).

seed=int(raw_input("Enter the seed: "))
count=1
while seed is not 1:
    if seed%2 is 0:
        seed=seed/2
        print count,": ", seed
        count=count+1
    else:
        seed=seed*3+1
        print count,": ", seed
        count=count+1

