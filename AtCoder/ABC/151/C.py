# C - Welcome to AtCoder

N, M = map(int, input().split())
AC = {}
WA = {}
for _ in range(M):
    p, s = input().split()
    if p not in AC and p not in WA:
        AC[p], WA[p] = 0, 0
    if AC[p] < 1:
        if s == 'AC':
            AC[p] += 1
        elif s == 'WA':
            WA[p] += 1

for p in AC:
    if AC[p] == 0:
        WA[p] = 0

print(sum(AC.values()), sum(WA.values()))
