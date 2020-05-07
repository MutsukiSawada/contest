# C - Exception Handling

N = int(input())
A = [int(input()) for _ in range(N)]
mx1 = sorted(A)[-1]
mx2 = sorted(A)[-2]
for i in range(N):
    if A[i] != mx1:
        print(mx1)
    else:
        print(mx2)
