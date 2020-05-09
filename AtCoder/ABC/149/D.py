# D - Prediction and Restriction

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = [t for t in str(input())]
U = [''] * N
point = 0

for i in range(N):
    if i < K:
        if T[i] == 'r':
            U[i], point = 'P', point + P
        elif T[i] == 's':
            U[i], point = 'R', point + R
        elif T[i] == 'p':
            U[i], point = 'S', point + S
    else:
        if T[i] == 'r':
            if U[i - K] != 'P':
                U[i], point = 'P', point + P
        elif T[i] == 's':
            if U[i - K] != 'R':
                U[i], point = 'R', point + R
        elif T[i] == 'p':
            if U[i - K] != 'S':
                U[i], point = 'S', point + S

print(point)
