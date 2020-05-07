# C - Walk on Multiplication Table

N = int(input())
start = [1, 1]
end = [0, 0]
for i in range(1, int(N ** (1 / 2)) + 1):
    if N % i == 0:
        end[0] = i
        end[1] = N // i

print((end[0] - start[0]) + (end[1] - start[1]))
