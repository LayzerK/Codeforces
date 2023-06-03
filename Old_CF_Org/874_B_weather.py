import sys
input = sys.stdin.readline


def solve():
    n,k = map(int, input().strip().split())
    pred = list(map(int, input().strip().split()))
    actual = list(map(int, input().strip().split()))

    output = [0] * n

    sortedpred = sorted(((x,i) for i,x in enumerate(pred)))
    sortedactual = sorted(x for x in actual)

    for i, pair in enumerate(sortedpred):
        val, idx = pair

        output[idx] = str(sortedactual[i])
    
    print(" ".join(output))


for tc in range(int(input())):
    solve()