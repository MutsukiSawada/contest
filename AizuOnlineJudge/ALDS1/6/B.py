N = int(input())
A = [int(a) for a in input().split()]

x = A[N - 1]
i = -1
for j in range(N):
    if A[j] <= x:
        i += 1
        A[i], A[j] = A[j], A[i]

for j, a in enumerate(A):
    if j == 0:
        print(a, end='')
    elif j == i:
        print(' [{}]'.format(a), end='')
    else:
        print(' {}'.format(a), end='')
print()