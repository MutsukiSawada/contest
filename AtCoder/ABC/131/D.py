# D - Megalomania

from operator import itemgetter

N = int(input())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
AB = sorted(AB, key=itemgetter(1), reverse=True)
deadline = AB[0][1]
for i in range(N):
    deadline = min(deadline, AB[i][1]) - AB[i][0]

print('Yes' if 0 <= deadline else 'No')
