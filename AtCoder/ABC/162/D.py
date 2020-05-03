# D - RGB Triplets

N = int(input())
S = input()
cnt_R = S.count('R')
cnt_G = S.count('G')
cnt_B = S.count('B')
total = cnt_R * cnt_G * cnt_B

expt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = j + (j - i)
        if k < N and (S[i] != S[j] and S[j] != S[k] and S[i] != S[k]):
            expt += 1

print(total - expt)
