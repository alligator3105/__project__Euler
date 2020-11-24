def prime_factor(x):
    # b = []
    for i in range(1, x+1):
        if x % i == 0:
            x = x / i
            # b.append(i)
            if x == 1:
                return i


c = prime_factor(600851475143)
print(c)

