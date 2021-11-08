
def prime_in_range(a,b):
    for i in range(a,b):
        isprime = True
        div = 2
        while (isprime and (div <= i**(0.5))):
            if (i % div) == 0 :
                isprime = False
            div += 1
        if isprime:
            print(i,"is prime")
