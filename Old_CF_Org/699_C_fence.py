from collections import Counter
import sys
input = sys.stdin.readline
for tc in range(int(input())):
    n, m = map(int, input().split())

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    colors = list(map(int, input().split()))

    # basic possibility check

    freqNeeded = Counter(end)
    freqHave = Counter(colors)
    s = 0
    dump = colors[-1]
    locs = [[] for x in range(n+1)]
    for i, color in enumerate(start):
        if color == end[i]:
            freqNeeded[color] -= 1
            if color == dump:
                s = i
        else:
            locs[end[i]].append(i)

    if dump not in freqNeeded:
        print("NO")
        continue
    dumploc = locs[dump][0] if locs[dump] else s
    valid = True
    for color in freqNeeded:
        if freqNeeded[color] > freqHave[color]:
            valid = False
    # print(dumploc)
    if valid:
        output = []
        for i, color in enumerate(colors):
            # print(locs)
            if locs[color]:
                output.append(str(locs[color][-1]+1))
                locs[color].pop()
            else:
                output.append(str(dumploc+1))

        print("YES")
        print(" ".join(output))
    else:
        print("NO")
