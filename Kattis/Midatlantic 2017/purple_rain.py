import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  s = input().strip()
  
  #max value subarray and min value subarray
  
  minVal = 10000000
  maxVal = -1000000
  
  currMin = 0
  currMax = 0
  
  maxLoc = (0,0)
  minLoc = (0,0)
  minLeft = 0
  maxLeft = 0
  for right, val in enumerate(s):
    adj = -1 if val == "B" else 1
    
    currMin += adj
    currMax += adj
    
    if currMin < minVal:
      minVal = currMin
      minLoc = (minLeft+1,right+1)
    if currMin > 0:
      currMin = 0
      minLeft = right+1
    
    if currMax > maxVal:
      maxVal = currMax
      maxLoc = (maxLeft+1, right+1)
    if currMax < 0:
      currMax = 0
      maxLeft = right + 1
  if abs(minVal) > maxVal:
    print(minLoc[0], minLoc[1])
  elif maxVal > abs(minVal):
    print(maxLoc[0], maxLoc[1])
  else:
    if maxLoc[0] < minLoc[0]:
      print(maxLoc[0], maxLoc[1])
    elif minLoc[0] < maxLoc[0]:
      print(minLoc[0], minLoc[1])
    else:
      print(minLoc[0], min(minLoc[1], maxLoc[1]))


    

solve()
    