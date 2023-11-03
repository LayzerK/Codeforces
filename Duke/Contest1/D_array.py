import sys
input = sys.stdin.readline
from collections import defaultdict
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    #if a non zero number < something appears in between instances of a number < than it, it is invalid

    required_zeros = 0

    n,queries = multiple_ints()
    first_non_zero = -1
    arr = list(multiple_ints())
    locs = defaultdict(list)
    for i,num in enumerate(arr):
        if num != 0 and first_non_zero == -1:
            first_non_zero = num
        locs[num].append(i)
    
    zeros = len(locs[0])
    if zeros == n:
        print("YES")
        ans = [queries] * n
        print(*ans)
        return
    prior = False
    lb = n + 1
    rb = -1
    banned = [False] * n
    for q in range(queries, 0, -1):
        if len(locs[q]) == 0:
            #it was either overwritten by some other query OR
            #it can only be overwritten by a prior query if said prior query exists
            #Otherwise, it must have been zeroed
            if not prior:
                required_zeros = 1
        else:
            pick = -1
            prior = True
            for i in locs[q]:
                if banned[i]:
                    print("NO")
                    return
            lb = locs[q][0]
            rb = locs[q][-1]

            for i in range(lb, rb+1):
                banned[i] = True
    if required_zeros > zeros:
        print("no")
        return
    
    for i, val in enumerate(arr):
        if val == 0:
            if i == 0:
                arr[i] = first_non_zero
            else:
                arr[i] = arr[i-1]
    print("YES")
    print(*arr)

solve()
    