import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    if n >= 5:
        print("Alice")
    else:
        print("Bob")

for tc in range(int(input())):
    solve()