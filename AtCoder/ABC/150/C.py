# C - Count Order

N = int(input())
A = [str(i) for i in range(1, N + 1)]
P = ''.join([p for p in input().split()])
Q = ''.join([q for q in input().split()])

ans = []

def dfs(ls, s):
    if len(ls) == 0:
        ans.append(s)
    else:
        for i in range(len(ls)):
            dfs(ls[:i] + ls[i + 1:], s + ls[i])

dfs(A, '')
print(abs(ans.index(P) - ans.index(Q)))
