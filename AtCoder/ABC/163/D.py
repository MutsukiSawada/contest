# D - Sum of Large Numbers

N, K = map(int, input().split())

cnt = 0
for i in range(K, N + 2):
    mn = i * (i - 1) // 2
    mx = i * (N + (N - i + 1)) // 2
    cnt += mx - mn + 1

print(cnt % ((10 ** 9) + 7))
