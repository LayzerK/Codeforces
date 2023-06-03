import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    diff = 0
    for n1, n2 in zip(a,b):
        diff = max(diff, n1 - n2)
        if n1-n2 < 0:
            print("no")
            return
    

    for n1, n2 in zip(a,b):
        if n2 != 0 and n1-n2 != diff:
            print("no")
            return
    print("yes")

for tc in range(int(input())):
    solve()