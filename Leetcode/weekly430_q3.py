import sys
input = sys.stdin.readline
from collections import defaultdict
from random import randint


def multiple_ints():
  return map(int, input().strip().split())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 
    137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 
    227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]

factors = [defaultdict(int)]

for i in range(1, 1001):
    f = defaultdict(int)
    x = i
    for p in primes:
        while x % p == 0:
            x //= p
            f[p] += 1
    if x != 1:
        f[x] += 1
    factors.append(f)
def solve(nums):
        #can I check for (p*r)/q with a precomputed suffix check? -> n^3
        #how can I get this tooo n^2 reeeeee
        #p/q = s/r
        #does this give any insights?
        
        #compute the prime factor "division" and then check for it in the suffix??
        
        def sub(a, b):
            #a-b
            n = defaultdict(int)
            
            for val in a:
                if a[val] != b[val]:
                    n[val] = a[val] - b[val]
            for val in b:
                if val not in a:
                    n[val] = -b[val]
            return n
        suffix = [defaultdict(int) for i in range(len(nums))] 
        for r in range(len(nums) - 2, 3, -1):
            rfac = factors[nums[r]]
            suffix[r] = suffix[r+1].copy()
            for s in range(r+2, len(nums)):
                sfac = factors[nums[s]]
                
                diff = sub(sfac, rfac)
                suffix[r][tuple(sorted(diff.items()))] += 1
        
        
        ans = 0
        for p in range(len(nums)):
            pfac = factors[nums[p]]
            for q in range(p+2, len(nums) - 4):
                qfac = factors[nums[q]]
                
                diff = sub(pfac, qfac)
                ans += suffix[q+2][tuple(sorted(diff.items()))]
        return ans

def brute(nums):
    ans = 0

    for p in range(len(nums)):
        for q in range(p+2, len(nums)):
            for r in range(q+2, len(nums)):
                for s in range(r+2, len(nums)):
                    if nums[p] * nums[r] == nums[q] * nums[s]:
                        #print(p,q, r, s)
                        ans += 1
    return ans


def generate():
    size = randint(8, 50)

    arr = []

    for i in range(size):
        arr.append(randint(1, 1000))
    
    return arr


test = [10,4,2,10,9,3,45]

brute(test)

for i in range(50):
    arr = generate()

    b_ans = brute(arr)
    s_ans = solve(arr)

    if b_ans != s_ans:
      print(arr)
      print("Brute", b_ans, "Solve", s_ans)
    

