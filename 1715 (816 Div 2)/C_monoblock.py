import sys
input = sys.stdin.readline

def solve():
    n,m = map(int, input().strip().split())
    arr = [0] + list(map(int, input().strip().split())) + [0]
    subarr = int((n*(n+1))/2)
    ans = 0
    # 1 2 2 4 5
    for i in range(1, n+1):
        if arr[i] == arr[i+1]:
            continue
        rem = n-i
       
        ans += (i * rem)
    
    for q in range(m):
        i,num = map(int, input().split())

        if arr[i] != arr[i-1]:
            #this is like from the perspective of the prior element
            ans -= (n-i+1) * (i-1)
        if arr[i] != arr[i+1]:
            #from the perspectife of this element
            ans -= (n-i) * i
        
        arr[i] = num

        if arr[i] != arr[i-1]:
            ans += (n-i+1) * (i-1)
        if arr[i] != arr[i+1]:
            ans += (n-i) * i


        print(ans + subarr)


    

solve()