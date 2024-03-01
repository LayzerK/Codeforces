import sys
from math import gcd, ceil, sqrt
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def prime(n):
    for divisor in range(2, int(sqrt(n))+1):
        if n % divisor == 0:
            return divisor
        
    return n

def solve():
    l,r = multiple_ints()

    for num in range(l, r+1):
        divisor = prime(num)
        if divisor != num:
            print(divisor, num-divisor)
            return
    print(-1)
for tc in range(int(input())):
    solve()
    