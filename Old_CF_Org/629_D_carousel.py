import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    
    cnt = 0
    k = 1
    ans = [0] * n
    ans[0] = 1

    #I get the feeling that only the last element can be a 3
    #it's a 3 IFF the adjacent is a 2 AND the next is a 1 or the adj is a 2 and the next is a one
    #failing this TC:
    """
    8
    13 13 9 12 13 1 13 1
    """
    #if the graph is bipartite then it is 2, otherwise it is 3
    #graph is bipartite if the total length of the graph is even since this is just a cyclic graph and bipartite-ness is being an even cycle
    #if it's odd, you can imagine a compression and then it becomes even
    loc = None
    compress = False
    for i in range(len(arr)):
        compress |= arr[i] == arr[(i+1)%n]
        if arr[i] == arr[(i+1)%n] and loc is None:
          loc = i
        
    if len(set(arr)) == 1:
        print(1)
        ans = [1] * n
        print(*ans)
        return
    ans = [0] * n
    used = False
    if len(ans) % 2 and not compress:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                ans[i] = 3
            elif ans[i-1] == 1:
                ans[i] = 2
            else:
                ans[i] = 1
    elif len(arr) % 2 == 0:
        for i in range(len(arr)):
          if ans[i-1] == 1:
            ans[i] = 2
          else:
            ans[i] = 1
    else:
        #("here", loc)
        ans[loc] = 1
        ans[(loc+1)%n] = 1

        for nxt in range(loc+2, n):
            if ans[nxt-1] == 2:
                ans[nxt] = 1
            else:
                ans[nxt] = 2
        
        for prior in range(loc-1, -1, -1):
            
            if ans[prior+1] == 2:
                ans[prior] = 1
            else:
                ans[prior] = 2
        
    
    print(max(ans))
    print(*ans)
        
    
for tc in range(int(input())):
    solve()
        