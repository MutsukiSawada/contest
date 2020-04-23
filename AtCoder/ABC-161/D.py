# D - Lunlun Number

K = int(input())

N = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0

while len(N) < K:
    n = int(str(N[i]) + str(N[i])[-1:])
    if str(n)[-1:] == '0':
        N += [n, n + 1]
    elif str(n)[-1:] == '9':
        N += [n - 1, n]
    else:
        N += [n - 1, n, n + 1]
    i += 1

print(N[K - 1])