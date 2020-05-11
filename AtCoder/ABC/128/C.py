# C - Switches

N, M = map(int, input().split())
switches = []
for _ in range(M):
    k, *s = map(int, input().split())
    switches.append([i - 1 for i in s])
lights = [int(p) for p in input().split()]

def f(i, on_off):
    if N <= i:
        result = 1
        for i in range(M):
            on = 0
            for j in switches[i]:
                on += on_off[j]
            if on % 2 != lights[i]:
                result = 0
        return result
    return f(i + 1, on_off + [1]) + f(i + 1, on_off + [0])

print(f(0, []))
