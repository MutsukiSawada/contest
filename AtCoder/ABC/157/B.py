# B - Bingo

A = []
for _ in range(3):
    A.append([int(a) for a in input().split()])

N = int(input())
B = [[False] * 3 for _ in range(3)]
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                B[i][j] = True

ans = 'No'
for i in range(3):
    if B[i][0] == B[i][1] == B[i][2] == True:
        ans = 'Yes'
    if B[0][i] == B[1][i] == B[2][i] == True:
        ans = 'Yes'
if B[0][0] == B[1][1] == B[2][2] == True:
    ans = 'Yes'
if B[0][2] == B[1][1] == B[2][0] == True:
    ans = 'Yes'

print(ans)
