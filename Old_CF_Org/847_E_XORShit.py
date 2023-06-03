testcases = int(input())
for _ in range(testcases):
    half = int(input())

    oneq = half//2
    threeq = oneq * 3

    if oneq ^ threeq == half:
        print(oneq, threeq)
    else:
        print(-1)
