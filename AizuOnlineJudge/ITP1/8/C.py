import sys

S = sys.stdin.read().lower()
ABC = [chr(ord('a') + i) for i in range(26)]

for abc in ABC:
    print(abc, ':', S.count(abc))