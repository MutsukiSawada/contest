# B - 0 or 1 Swap

N = int(input())
P = [int(p) for p in input().split()]
cnt = 0
i = 1
for j in range(N):
    if i != P[j]:
        cnt += 1
    i += 1
print('YES' if cnt <= 2 else 'NO')
