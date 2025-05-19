import sys
input = sys.stdin.readline
def solve():
    anna, kate, both = map(int, input().strip().split())

    anna += both//2 + both%2
    kate += both//2

    if anna > kate:
        print("First")
    else:
        print("Second")


for tc in range(int(input())):
    solve()
    