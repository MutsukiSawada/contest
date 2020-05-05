# D - Bouquet

MOD = 10 ** 9 + 7
n, a, b = map(int, input().split())
total = pow(2, n, MOD) - 1

def choose(n, r):
    X = 1
    Y = 1
    for i in range(r):
        X *= n - i
        X %= MOD
        Y *= i + 1
        Y %= MOD
 
    return X * pow(Y, MOD - 2, MOD) % MOD

A = choose(n, a)
B = choose(n, b)
print((total - A - B) % MOD)
