# B - Battle

from math import ceil

A, B, C, D = map(int, input().split())
print('Yes' if ceil(C / B) <= ceil(A / D) else 'No')