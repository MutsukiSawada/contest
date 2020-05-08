# C - Dice and Coin

N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    if K <= i:
        ans += 1 / N
    else:
        coins = 0
        while i < K:
            i = i * 2
            coins += 1
        ans += (1 / N) * ((1 / 2) ** coins)

print(ans)
