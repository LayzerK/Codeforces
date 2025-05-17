import sys
from math import sqrt
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())


def sieve(mx):
  primes = []
  is_prime = [True] * (mx+1)
  is_prime[0] = False
  is_prime[1] = False
  
  for i in range(2, mx+1):
    if is_prime[i] == False:
      continue
    for j in range(i*i, mx+1, i):
      is_prime[j] = False
  
  for i in range(2, mx+1):
    if is_prime[i]:
      primes.append(i)
  return primes


primes = sieve(10**6)
def is_good(k, l):
    # We only need to check divisibility by primes up to sqrt(k)
    limit = int(sqrt(k)) + 1
    
    for p in primes:
        if p >= l:
            break
        if p > limit:  # Stop if prime is larger than sqrt(k)
            break
        if k % p == 0:
            return f"BAD {p}"
    
    return "GOOD"

while True:
    k, l = input().strip().split()
    k = int(k)
    l = int(l)
    if k == 0 and l == 0:
        break
    print(is_good(k, l))
    