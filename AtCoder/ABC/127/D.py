# D - Integer Cards

from operator import itemgetter

N, M = map(int, input().split())
A = sorted([int(a) for a in input().split()])

BC = []
for i in range(M):
    b, c = map(int, input().split())
    BC.append([b, c])

BC = sorted(BC, key=itemgetter(1), reverse=True)

ans = 0
for i in range(N):
    if len(BC) != 0 and A[i] <= BC[0][1]:
        ans += BC[0][1]
        BC[0][0] -= 1
        if BC[0][0] == 0:
            BC.pop(0)
    else:
        ans += A[i]

print(ans)
