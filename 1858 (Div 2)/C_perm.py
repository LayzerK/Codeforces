import sys
input = sys.stdin.readline
from math import gcd
def solve():
    n = int(input())

    banned = set()
    pairs = []
    output = []
    for num in range(1, n+1):
        if num in banned:
            continue
        pair = []

        while num <= n:
            banned.add(num)
            pair.append(num)

            num *= 2
        pairs.append(pair)

    
    for num in range (1,n+1):
        if num in banned:
            continue
        output.append(num)
    for p in pairs:
        for n in p:
            output.append(n)
    print(*output)
    #print(banned)
        

for tc in range(int(input())):
    solve()
    