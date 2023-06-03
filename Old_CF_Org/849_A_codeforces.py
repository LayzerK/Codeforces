import sys
input = sys.stdin.readline

for tc in range(int(input())):
    c = input().strip()
    if c in "codeforces":
        print("yes")
    else:
        print("no")
