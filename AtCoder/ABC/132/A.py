# A - Fifty-Fifty

S = [s for s in str(input())]
ls = list(set(S))
if len(ls) == 2:
    if S.count(ls[0]) == 2 and S.count(ls[1]):
        print('Yes')
    else:
        print('No')
else:
    print('No')
