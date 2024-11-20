class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1
    

import sys
from math import floor
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
    archers, events = multiple_ints()
    starting = list(multiple_ints())
    
    scores = {}
    for i, val in enumerate(starting):
        scores[i+1] = val
    
    #print(starting)

    fenny = FenwickTree(starting)

    for event in range(events):
        shooter, chosen, l, r = multiple_ints()

        rbound = fenny.query(r)
        lbound = fenny.query(l-1)

        total = rbound - lbound


        sz = r-l + 1

        avg = floor(total/sz)

        #print(avg, "here", total, lbound, rbound)
        fenny.update(shooter-1, avg)
        fenny.update(chosen-1, -avg)
        scores[shooter] += avg
        scores[chosen] -= avg
        #print(scores)
    
    best = -(10**20)
    ans = -1
    for i in range(1, archers+1):
        score = scores[i]
        if score > best:
            best = score
            ans = i
    #print(scores)
    print(ans)


solve()