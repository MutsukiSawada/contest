# C - Anti-Division

from fractions import gcd

A, B, C, D = map(int, input().split())

CxD = C * D // gcd(C, D)

total_C = B // C
total_D = B // D
total_CxD = B // CxD

sub_C = (A - 1) // C
sub_D = (A - 1) // D
sub_CxD = (A - 1) // CxD

print((B - (A - 1)) -
        (total_C + total_D - total_CxD) + (sub_C + sub_D - sub_CxD))
