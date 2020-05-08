# B - Guidebook

from operator import itemgetter

N = int(input())
SP = []
for i in range(N):
    s, p = input().split()
    SP.append((int(i + 1), str(s), int(p)))

SP = sorted(SP, key=itemgetter(2), reverse=True)
SP = sorted(SP, key=itemgetter(1))
for sp in SP:
    print(sp[0])
