def sieve(limit):
    primes = [True] * (limit+1) 
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * 2, limit + 1, p):
                primes[i] = False  
        p += 1
    primes = [element for element in range(2, limit+1) if primes[element]]
    return primes 
