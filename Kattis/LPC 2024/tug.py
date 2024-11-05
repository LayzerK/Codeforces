import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())
def multiple_floats():
  return map(float, input().strip().split())


def solve():
  n, p =map(float, input().strip().split())
  n = int(n)
  pulling = list(multiple_floats())
  multiplier = list(multiple_floats())

  nums = list(range(n))

  output = []
  def backtrack(curr):
      if curr == n:
          output.append(nums[:])
      
      for swap in range(curr, n):
          nums[curr], nums[swap] = nums[swap], nums[curr]
          backtrack(curr+1)
          nums[curr], nums[swap] = nums[swap], nums[curr]
  backtrack(0)
  
  ans = 0

  def check(perm):
    val = 0
    for pos, player in enumerate(perm):
      val += multiplier[pos] * pulling[player]
    return val > p

  for perm in output:
     ans += check(perm)

  print(ans)


solve()
    