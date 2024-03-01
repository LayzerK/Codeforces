import sys
input = sys.stdin.readline
from math import sqrt
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  points = []
  def dist(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
  for vertice in range(n):
    x,y = map(float, input().strip().split())
    points.append((x,y))
  
  ans = 0
  for i,p1 in enumerate(points):
    for j in range(i+1, len(points)):
      ans = max(ans, dist(p1, points[j]))
  print(ans)
  

solve()
    