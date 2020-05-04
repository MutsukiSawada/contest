# D - String Formation

from collections import deque

S = deque([s for s in input()])
Q = int(input())
rev = False

for _ in range(Q):
    T = [t for t in input().split()]
    t = int(T[0])
    if t == 1:
        rev = not rev
    if t == 2:
        f, c = int(T[1]), T[2]
        if f == 1:
            if rev:
                S.append(c)
            else:
                S.appendleft(c)
        if f == 2:
            if rev:
                S.appendleft(c)
            else:
                S.append(c)

S = ''.join(list(S))
print(S if not rev else S[::-1])
