import itertools
import sys

for n in itertools.count(100000000,1):
    prime = True
    factor = int(n**(1/2)) + 1
    while prime:
        if factor > 1:
            if n % factor == 0:
                prime = False
            factor -= 1
        else:
            break
    if prime == True:
        print(n)
        sys.exit()

