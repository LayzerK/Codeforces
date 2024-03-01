import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort(reverse= True)

  
    x,a = map(int, input().strip().split())
    y,b = map(int, input().strip().split())
    req = int(input())

    if y > x:
        x,a,y,b = y,b,x,a
    xprop, yprop = x/100, y/100

  
    
    def check(take):
        #if take >= len(arr):
           # return True
        
        both = 0
        xtake = 0
        ytake = 0
        ans = 0
        for i in range(1, take+1):
            if i % a == 0 and i % b == 0:
                both += 1
            elif i % a == 0:
                xtake += 1
            elif i % b == 0:
                ytake += 1
        
        for i in range(both):
            ans += arr[i] * (xprop+yprop)
        for i in range(xtake):
            ans += arr[both+i] * xprop
        for i in range(ytake):
            ans += arr[both+i+xtake] * yprop
        #print(left, right, take, ans, "in func")
        #print(ans, "here")
        return ans >= req
    
    left = 1
    right = n + 1
    while left < right:
        mid = (left+right)//2
        #print(left, right, mid, check(mid))

        if check(mid):
            right = mid
        else:
            left = mid + 1
    #print(left, mid, right, "all")
    if left > n:
        left = -1
    print(left)
    #print(check(4), "jerere")
for tc in range(int(input())):
    solve()


                

    
    
  



    

    

