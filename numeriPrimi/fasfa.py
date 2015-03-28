from math import sqrt
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n, i)}
        p = {x for x in range(2, n) if x not in no_p}
    return p

primes(100)
#print(sorted(primes(100)))