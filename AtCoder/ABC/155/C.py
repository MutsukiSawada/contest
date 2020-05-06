# C - Poll

N = int(input())
D = {}
mx = 0
for _ in range(N):
    s = str(input())
    if s not in D:
        D[s] = 0
    D[s] += 1
    if mx < D[s]:
        mx = D[s]

for a in sorted([d for d in D if D[d] == mx]):
    print(a)
