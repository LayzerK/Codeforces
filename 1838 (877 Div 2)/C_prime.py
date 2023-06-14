import sys
input = sys.stdin.readline

def solve():
    #trivially we know we can just do adj diff of 1
    #column diff is trickier. If the length of a row is non prime, then its fine. If it is prime -> you need a multiple difference. -> skip over?

    rLen,cLen = map(int, input().strip().split())

    output = [[0 for x in range(cLen)] for x in range(rLen)]
    curr = 1
    for rows in range(1, rLen, 2):
        for col in range(cLen):
            #print(rows, col)
            output[rows][col] = curr
            curr += 1
    
    for rows in range(0, rLen, 2):
        for col in range(cLen):
            output[rows][col] = curr
            curr += 1
    
    for row in output:
        print(*row)

for tc in range(int(input())):
    solve()