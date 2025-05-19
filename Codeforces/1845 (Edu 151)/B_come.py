import sys
input = sys.stdin.readline

def solve():
    ax,ay = map(int, input().strip().split())
    bx, by = map(int, input().strip().split())
    cx, cy = map(int, input().strip().split())


    shared = 1

    if (bx > ax and cx > ax) or (bx < ax and cx < ax):
        shared += min(abs(ax-bx), abs(ax-cx))
    if (by > ay and cy > ay) or (by < ay and cy < ay):
        shared += min(abs(ay-by), abs(ay - cy))

    print(shared)
for tc in range(int(input())):
    solve()