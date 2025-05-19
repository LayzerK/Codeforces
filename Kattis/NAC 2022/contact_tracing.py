import sys
input = sys.stdin.readline
from collections import defaultdict
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  arr = []

  n,k,c = multiple_ints()
  
  day_one = set()
  non_day_one = set()
  d_meetings = defaultdict(list)

  meetings = []
  last = defaultdict(int)
  for i in range(c):
    a,b,day = multiple_ints()
    if day == 1:
      day_one.add(a)
      day_one.add(b)
    else:
      non_day_one.add(a)
      non_day_one.add(b)
    meetings.append((a,b, day))
    last[a] = max(last[a], day)
    last[b] = max(last[b], day)
  p_zeros = {x for x in day_one if x not in non_day_one}
  

  #if people have a meeting on a day they cannot have been infecte
  for a,b,d in meetings:
    bound = max(last[a], last[b])

    if d >= bound - 1:
      d_meetings[d].append((a,b))
  
  #print(p_zeros)
  # try the scenario with every viable person as a patient zero
  # a patient is only viable if they had a meeting on day 1 and only day 1
  # continually check for 'chain of viability' beyond that  

  def check(p_zero):
    contagious = {p_zero}
    newly_infected = set()
    #let contagious be the set of people who are contagious on day D
    for d in range(1, k+1):
      for a,b in d_meetings[d]:
        if a in contagious:
          newly_infected.add(b)
        if b in contagious:
          newly_infected.add(a)
      #print(day, newly_infected, symptomatic, p_zero)
      if d == k:
        return newly_infected
      contagious = newly_infected.copy()
      newly_infected.clear()
    

  req = set()
  for p in p_zeros:
    req |= check(p)
  if req:
    req = list(req)
    req.sort()
  print(len(req))
  for p in req:
    print(p)
solve()
    