while True:
    N = int(input())
    if N == 0:
        break
    A = [int(a) for a in input().split()]
    m = sum(A) / N
    print((sum(map(lambda a: (a - m) ** 2, A)) / N) ** 0.5)