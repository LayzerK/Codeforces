import sys
input = sys.stdin.readline

def solve():
    start, end = map(int, input().strip().split())

    #just reverse operations
    seq  = [end]
    while True:
        #print(end)
        if start == end:
            print("YES")
            print(len(seq))
            print(*seq[::-1])
            return
        
        x = str(end)
        if end < start:
            print("NO")
            return
        if end%2 == 0:
            end //= 2
            
        elif x[-1] == "1":
            end -= 1
            end //= 10

        else:
            print("NO")
            return
        seq.append(end)



solve()