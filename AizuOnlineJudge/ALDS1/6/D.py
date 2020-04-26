WMAX = 10 ** 4 + 1
N = int(input())
W1 = [int(w) for w in input().split()]
W2 = sorted(W1)
W3 = {}
mn1 = min(W1)
V = [False] * N

for i, w in enumerate(W2):  W3[w] = i

cost = 0
for i in range(N):
    if V[i]: continue
    cur = i
    S = 0
    N2 = 0
    mn2 = WMAX
    while True:
        V[cur] = True
        S += W1[cur]
        mn2 = min(mn2, W1[cur])
        N2 += 1
        cur = W3[W1[cur]]
        if V[cur]: break
    cost += min(mn2 * (N2 - 2) + S, mn2 + S + (1 + N2) * mn1)

print(cost)