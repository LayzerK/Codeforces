import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    
    results = []

    for p in range(n):
        results.append(list(map(int, input().strip().split())))



    def check(curr, comp):
        total = 0
        for res1, res2 in zip(results[curr], results[comp]):
            if res1 < res2:
                total += 1
        
        if total >= 3:
            return curr
        else:
            return comp

    def validate(curr):
        valid = True
        for i in range(n):
            if i == curr:
                continue 
            total = 0
            for res1, res2 in zip(results[curr], results[i]):
                if res1 < res2:
                    total += 1
            #print(total, valid, i)
            valid = valid and total >= 3
        if valid:
            print(ans+1)
        else:
            print(-1)


    ans = 0
    for i in range(1, n):
        #print(ans)
        ans = check(ans, i)
    #validate(4)
    validate(ans)


for tc in range(int(input())):
    solve()



