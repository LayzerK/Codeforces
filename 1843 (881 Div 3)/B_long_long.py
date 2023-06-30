import sys
input = sys.stdin.readline

def solve():
      n = int(input())
      arr = list(map(int, input().strip().split()))
      ans = 0
      segs = 0
      prior = False
      for x in arr:
          ans += abs(x)
          if x < 0:
              if prior:
                  continue
              segs += 1
              prior = True
          elif x > 0:
              prior = False
        

      print(ans, segs)

for tc in range(int(input())):
    solve()