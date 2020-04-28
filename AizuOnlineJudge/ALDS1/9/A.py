N = int(input())
H = [int(h) for h in input().split()]

for i in range(1, N + 1):
    print('node {}: '.format(i), end='')
    print('key = {}, '.format(H[i - 1]), end='')
    if i // 2 > 0:
        print('parent key = {}, '.format(H[i // 2 - 1]), end='')
    if i * 2 <= N:
        print('left key = {}, '.format(H[i * 2 - 1]), end='')
    if i * 2 + 1 <= N:
        print('right key = {}, '.format(H[i * 2 + 1 - 1]), end='')
    print()