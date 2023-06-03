import sys
input = sys.stdin.readline
for tc in range(int(input())):
    s = input().strip()

    chars = set(s)
    # print(chars)
    if len(chars) == 1:
        print("-1")
        continue

    print(len(s) - 1)
