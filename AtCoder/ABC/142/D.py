# D - Disjoint Set of Common Divisors

import fractions

A, B = map(int, input().split())
C = fractions.gcd(A, B)

primes = []
i = 2
while i * i <= C:
    while C % i == 0:
        C //= i
        primes.append(i)
    i += 1
if C > 1:
    primes.append(C)

print(len(set(primes)) + 1)
