N = int(input())
S = [i for i in range(1, 14)]
H = [i for i in range(1, 14)]
C = [i for i in range(1, 14)]
D = [i for i in range(1, 14)]

for n in range(N):
    suit, num = input().split()
    num = int(num)
    if suit == 'S': S.remove(num)
    if suit == 'H': H.remove(num)
    if suit == 'C': C.remove(num)
    if suit == 'D': D.remove(num)

for s in S: print('S', s)
for h in H: print('H', h)
for c in C: print('C', c)
for d in D: print('D', d)