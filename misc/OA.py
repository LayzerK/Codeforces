from math import ceil
testcases = int(input())
for tc in range(1, testcases+1):
    n = int(input())
    req = list(map(int, input().strip().split())) 

    total = 0
    for base in req:
        spare = ceil(base*.1)
        total += base+spare
    
    print(f"Case #{tc}: {total}")
