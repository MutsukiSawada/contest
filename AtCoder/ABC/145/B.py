# B - Echo

N = int(input())
S = str(input())
print('Yes' if S[:N // 2] == S[N // 2:] else 'No')
