N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [int(input()) for _ in range(M)]

for i in range(N):
    cnt = 0
    for j in range(M):
        cnt += A[i][j] * B[j]
    print(cnt)