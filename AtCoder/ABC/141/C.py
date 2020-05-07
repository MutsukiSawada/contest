# C - Attack Survival

N, K, Q = map(int, input().split())
P = [0] * N
for _ in range(Q):
    P[int(input()) - 1] += 1

for p in P:
    if 0 < K - Q + p:
        print('Yes')
    else:
        print('No')
