import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    banned = input().strip()
    n = len(banned)
    if banned == "()":
        print("NO")
        return
    

    #we can either do ()()()()()
    #or ((((()))))

    #do we ever need to do anything else?
    
    print("YES")
    #print("ANSWER")
    if ")(" in banned:
        print("(" * n + ")" * n)
    else:
        ans = ""
        for x in range(n):
            ans += "()"
        print(ans)

for tc in range(int(input())):
    solve()
    