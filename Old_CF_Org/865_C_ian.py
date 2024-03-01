import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))

    diff = []

    for i in range(len(arr)-1):
        diff.append(arr[i+1] - arr[i])
    print(diff)
    odd = 0
    for i,num in enumerate(diff):
        if i%2 == 0:
            odd += num
    
    #print(odd)
    if n%2 or odd >= 0:
        print("YES")
    else:
        print("NO")
    


for tc in range(int(input())):
    solve()