from collections import defaultdict
testcases = int(input())
for testcase in range(testcases):
    n = int(input())
    #print("Here", n)
    freqs = defaultdict(lambda: defaultdict(int))
    output = [0] * n
    for p in range(n):
        premutation = map(int, input().split())

        for i, num in enumerate(premutation):
            freqs[i][num] += 1

    for first in freqs[0]:
        if freqs[0][first] == 1:
            nxt = first
        else:
            output[0] = first

    for indice in range(1, n-1):
        two = freqs[indice]
        #print(nxt, indice)
        #print(indice, nxt, n-1)
        output[indice] = nxt
        newnxt = -1
        for num, freq in two.items():
            if num != nxt:
                newnxt = num
        nxt = newnxt
    output[-1] = nxt
    for i in output:
        print(i)
