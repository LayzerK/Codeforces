import sys
input = sys.stdin.readline

def solve():
    s = input().strip()

    diff = 0
    proper = "abc"

    for c1, c2 in zip(s, proper):
        if c1 != c2:
            diff += 1
    
    if diff <= 2:
        print("YES")
    else:
      print("NO")

for tc in range(int(input())):
    solve()