import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve(sections, decrease, limit):
    arr = []

    for sec in range(sections):
        fun, dizzy = multiple_ints()
        arr.append((fun, dizzy))
    #let dp[i] represent the most fun you can have at this index with diz

    

while True():
    N,K,L = multiple_ints()

    if N == K == L == 0:
        break
    solve(N,K,L)
    