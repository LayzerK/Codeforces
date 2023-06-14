import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n = int(input())
    if n <= 2:
        print("YES")
        return
    a = list(map(int, input().strip().split()))
    b = deque()
    b.append(a[0])
    b.append(a[1])
    c = []
    lside = 0
    rside = 1


    for element in a[2:]:
        #print(b, element)
        if rside < lside:
            if element > b[-1]:
                b.append(element)
                rside += 1
            elif element > b[0]:
                b.appendleft(element)
                lside += 1
            else:
                print("No")
                return
        else:
            if element > b[0]:
                b.appendleft(element)
                lside += 1
            elif element > b[-1]:
                b.append(element)
            else:
                print("No")
                return
    if abs(lside-rside) <= 1:
        print("yes")

for tc in range(int(input())):
    solve()