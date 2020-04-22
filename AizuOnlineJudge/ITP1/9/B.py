while True:
    S = input()
    if S == '-':
        break
    M = int(input())
    for i in range(M):
        H = int(input())
        S = S[H:] + S[:H]
    print(S)