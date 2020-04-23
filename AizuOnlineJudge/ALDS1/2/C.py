N = int(input())
A = input().split()
A1 = [a for a in A]
A2 = [a for a in A]

# Bubble Sort
flag = True
i = 0
while flag:
    flag = False
    for j in range(1, N - i):
        if int(A1[j][1]) < int(A1[j - 1][1]):
            A1[j - 1], A1[j] = A1[j], A1[j  -1]
            flag = True
    i += 1

print(*A1)
print('Stable')

# Selection Sort
for i in range(N - 1):
    mni = i
    for j in range(i + 1, N):
        if int(A2[j][1]) < int(A2[mni][1]):
            mni = j
    if mni != i:
        A2[i], A2[mni] = A2[mni], A2[i]

print(*A2)
print('Stable' if A1 == A2 else 'Not stable')