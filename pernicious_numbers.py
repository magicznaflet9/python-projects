#n = 39
#print("decimal: ",n,"binary: ", format(n,"b"), "bin() ",bin(n))

def is_prime(n):
    if n < 2:
        return False
    elif n <4:
        return True
    else:
        for factor in range(2,int(n**(1/2))+1):
            if n % factor == 0:
                return False
        return True

#print(is_prime(1007))


def pernicoulous(a,b):
    for n in range(a,b):
        count = 0
        for bit in str(format(n,"b")):
            if bit == "1":
                count += 1
        if is_prime(count):
            print(n)

pernicoulous(2222222,2223333)
