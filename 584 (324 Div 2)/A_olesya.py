import sys
input = sys.stdin.readline

def solve():
    n,t = map(int,input().strip().split())

    x = 1 if t != 10 else 2

    if n == 1 and t!= 10:
        print(t)
    elif n == 1 and t == 10:
        print(-1)
    elif n == 2:
        print(9*t)
    elif n == 3:
        print(69 * t)
    else:
        print(int(str(t) + "0"*(n-x*2) + str(t)))
  

solve()