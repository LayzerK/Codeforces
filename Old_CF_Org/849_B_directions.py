import sys
input = sys.stdin.readline


def solve():
    valid = False
    x = 0
    y = 0
    n = int(input())
    s = input().strip()

    for char in s:
        if char == "L":
            x -= 1
        elif char == "R":
            x += 1
        elif char == "U":
            y += 1
        elif char == "D":
            y -= 1
        if x == 1 and y == 1:
            valid = True
            break
    if valid:
        print("YES")
    else:
        print("NO")


for tc in range(int(input())):
    solve()
