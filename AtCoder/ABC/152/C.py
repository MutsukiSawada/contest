# C - Low Elements

N = int(input())
P = [int(p) for p in input().split()]

mn = float('inf')
cnt = 0
for i in range(N):
    mn = min(mn, P[i])
    if P[i] <= mn:
        cnt += 1

print(cnt)
