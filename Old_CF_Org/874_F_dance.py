import sys
input = sys.stdin.readline

from collections import Counter


def solve():
  n,m = map(int, input().strip().split())
  arr = list(map(int, input().split()))

  arr.sort()
  cnts = Counter(arr)

  arr = list(set(arr))
  n = len(arr)

  #if n is less than M, that means we have less unique numbers than m which is auto disqual
  ans = 0
  if n < m:
    print(0)
    return
  MOD = 10**9 + 7
  #since the people are pairwise distinct, the number of combos we can make is the product of the number of all people in a window per the product rule

  #prepopulate window with the people in the first M numbers, avoids an annoying if statement at the beginning

  windowchoices = 1
  for first in range(m):
    windowchoices *= cnts[arr[first]]

  for left in range(n-m+1):
    if arr[left+m-1] - arr[left] < m: #has to be strictly less than m. Could this also be == m-1? I'm not sure if any other case works tbh
      ans += windowchoices
      ans = ans % MOD

    #slide the window by including the element on the right and removing element on the left
    #somehow this index out of bounds?

    if left + m < n:
      windowchoices //= cnts[arr[left]]
      windowchoices *= cnts[arr[left+m]]


  print(ans)


for tc in range(int(input())):
  solve()
