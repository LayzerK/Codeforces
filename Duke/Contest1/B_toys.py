import sys
input = sys.stdin.readline
from math import ceil
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n, cost = multiple_ints()

    #number of integers <= n such that A+B = cost


    if cost > n + n - 1:
        print("0")
        return
    elif n >= cost - 1:
        if cost % 2:
          print(cost//2)
        else:
          print(cost//2 - 1)
    else:
      #we are bounded by n now, not cost
      #10 and 15   
      #number of naturals < bound such a + b = cost
      
      #for 10 and 15

      #10 and 5
      #9 and 6
      # 8 and 7

      #for 16 and 20


      #11 and 9
      #12 and 8
      #13 and 7
      #14 and 16
      #15 and 5
      #16 and 4

      mini = ceil(cost/2)

      if mini == cost//2:
          mini += 1

      space = n - mini + 1
      print(space)
      #print(mini, n, cost, "here")
solve()