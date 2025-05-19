import sys
input = sys.stdin.readline

def solve():
    nodes, edges, k = map(int, input().strip().split())

    #you know the graph is connected
    #a maximally connected graph MUST have (n*(n-1))/2 edges
    #this is releevant if k == 2 (req would then be 1)
    #in all other cases, if k is 

    z = ((nodes) * (nodes-1))/2

    if edges > z or edges < nodes-1:
        print("NO") #too many edges to construct a graph w/o repeated edges/self loops OR too little edges

        return

    if nodes == 1:
        if k > 1:
            print("YES")
        else:
            print("NO")
    elif k <= 2:
        print("NO")
        
    elif k == 3:
        if edges == z:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    
    #main edge cases handled

for tc in range(int(input())):
    solve()