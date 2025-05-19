import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n = int(input())
    arr = list(multiple_ints())
    arr.sort()
    
    total = sum(arr)
    goal = total//n
    rem = total%rem
    
    ans = 0

    greater = 0
    less = 0

    for num in arr:
        if num > med:
            greater += num-med
        else:
            less += med-num
    

solve()
    