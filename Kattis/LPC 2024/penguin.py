import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  times = []

  for i in range(n):
    line = input().strip()

    j = len(line)-1

    while line[j] != "-":
      j -= 1
    
    name = line[:j-1].strip()
    time = int(line[j+1:])

    
    times.append((time, name))
  
  times.sort()

  print(f"First: {times[0][1]}")
  print(f"Second: {times[1][1]}")
  print(f"Third: {times[2][1]}")


solve()
    