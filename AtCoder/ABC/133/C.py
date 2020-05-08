# C - Remainder Minimization 2019

L, R = map(int, input().split())

mn = float('inf')
for i in range(L, L + 2019):
    for j in range(i + 1, L + 2019 + 1):
        if L <= i < j and i < j <= R:
            mn = min(mn, i * j % 2019)

print(mn)
