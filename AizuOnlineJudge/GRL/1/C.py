INF = float('inf')

V, E = map(int, input().split())
A = [[INF] * V for _ in range(V)]

for i in range(V):
    A[i][i] = 0

for _ in range(E):
    s, t, d = map(int, input().split())
    A[s][t] = d

for k in range(V):
    for i in range(V):
        if A[i][k] == INF:
            continue
        for j in range(V):
            if A[k][j] == INF:
                continue
            A[i][j] = min(A[i][j], A[i][k] + A[k][j])

negative = False
for i in range(V):
    if A[i][i] < 0:
        negative = True

if negative:
    print('NEGATIVE CYCLE')
else:
    for i in range(V):
        ans_row = []
        for j in range(V):
            if A[i][j] == INF:
                ans_row.append('INF')
            else:
                ans_row.append(A[i][j])
        print(*ans_row)
