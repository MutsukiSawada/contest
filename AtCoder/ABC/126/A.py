# A - Changing a Character

N, K = map(int, input().split())
S = str(input())
print(S[:K - 1] + S[K - 1].lower() + S[K:])
