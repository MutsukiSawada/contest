# B - ROT N

abc = [s for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
N = int(input())
S = str(input())

def f(ch, n):
    if len(abc) - 1 < abc.index(ch) + n:
        return abc[(abc.index(ch) + n) - len(abc)]
    else:
        return abc[abc.index(ch) + n]

ans = ''
for s in S:
    ans += f(s, N)

print(ans)
