from collections import defaultdict
from itertools import accumulate
from random import randint
def solve(coins, k):
  coins.sort()
        
  print(coins)
  ans = 0

  left = 0

  subbed = defaultdict(int)

  curr = 0
  size = 0
  for right, (lb, rb, ci) in enumerate(coins):
      
      
      gap = 0
      if right != 0 and coins[right-1][1] + 1 != lb:
          
          gap = lb - coins[right-1][1] - 1


      c_size = rb - lb + 1
      new_size = size + c_size + gap

      if new_size <= k:
          curr += c_size * ci
          size = new_size
          ans = max(ans, curr)

      else:
          #compute the answer trimming the right, then trim the left
          
          right_spare = k - size - gap
          
          if right_spare > 0:
              ans = max(ans, curr + right_spare * ci)



          
          #print(new_size, k, rb, left, right)

          while new_size > k:
              over = new_size - k
              l_size = coins[left][1] - coins[left][0] + 1 - subbed[left]
              if l_size > over:
                  subbed[left] += over
                  curr -= over * coins[left][2]
                  new_size = k
                  curr += over * ci
                  ans = max(ans, curr)
                  #print("HERERERE", curr, l_size)
              else:
                  curr -= l_size * coins[left][2]
                  left += 1
                  new_size -= l_size
                  ans = max(ans, curr)
                  
                  rem_gap = coins[left][0] - coins[left-1][1] - 1
                  
                  new_size -= rem_gap
                  
                  
                  
      #print(curr, lb, rb, ci, left, right)
  return ans


def brute(coins, k):
    coins.sort()
    rb = coins[-1][1]

    sweep = [0] * (rb+2)

    for l,r,v in coins:
        for i in range(l, r+1):
            sweep[i] += v
    
    sweep = list(accumulate(sweep))
    ans = 0
    for left in range(1, len(sweep) - k + 1):
        right = sweep[left+k-1]
        over = sweep[left-1]
        if right - over == 226:
            print(left, left+k-1, "AAAA")
        ans = max(ans, right-over)
    return ans



def generate():
    k = randint(1, 200)

    size = randint(1, 50)

    left = 0

    coins = []

    for i in range(len(size)):
        diff = randint(0, 500)
        rb = left + diff
        
        cval = randint(1, 1000)

        coins.append([left, rb, cval])
        left = rb + 1 + randint(0, 10)
    return (k, coins)
  

def test():
    for i in range(20):
        k, coins = generate()
        coins.sort()

        b_ans = brute(coins, k)
        s_ans = solve(coins, k)

        if b_ans != s_ans:
            print(k, coins)

def manual(k, coins):
    coins.sort()
    b_ans = brute(coins, k)
    s_ans = solve(coins, k)
    print(b_ans,s_ans)
    if b_ans != s_ans:
        print("NEQ")

manual(28, [[8,12,13],[29,32,2],[13,15,2],[40,41,18],[42,48,18],[33,36,11],[37,38,6]])