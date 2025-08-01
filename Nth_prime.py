#nth prime
l = []
for i in range(2, 10000):  # Increased range to ensure 1000 primes are covered
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        l.append(i)
        if len(l) == input1:
            return l[-1]
