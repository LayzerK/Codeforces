from collections import deque
from math import sqrt
used = 2
pyramid = [[1]]


def fn(a):
    return int((a*(a+1)*(2*a+1))//6)


while len(pyramid) < 2023:
    curr = []
    for x in range(len(pyramid[-1])+1):

        curr.append(used)
        used += 1
    pyramid.append(curr)

for tc in range(int(input())):
    n = int(input())
    ans = 0
    q = deque()

    row = int((-1 + sqrt(1 + 8 * (n-1))) / 2)

    sz = len(pyramid[row])
    col = n - pyramid[row][0]
    q.append((col, col, row))
    while q:
        lb, rb, r = q.popleft()

        if r == 0:
            ans += 1
            continue

        left = pyramid[r][lb]
        right = pyramid[r][rb]

        ans += (fn(right) - fn(left-1))

        q.append((max(0, lb-1), min(len(pyramid[r-1])-1, rb), r-1))
    print(int(ans))
