# D - Blue and Red Balls

N, K = map(int, input().split())

def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

mod = 10 ** 9 + 7
n = 10 ** 4
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

for i in range(1, K + 1):
    B = cmb(K - 1, i - 1, mod)
    R = cmb(N - K + 1, N - K - i + 1, mod)
    print(B * R % mod)
