# D - Dice in Line

N, K = map(int, input().split())
P = [int(p) for p in input().split()]

Q = [0] * (N + 1)
for i in range(N):
    q = ((1 + P[i]) * P[i] / 2) / P[i]
    Q[i + 1] = Q[i] + q

mx = 0
for i in range(N - K + 1):
    mx = max(mx, Q[i + K] - Q[i])

print(mx)
