testcases = int(input())

for testcase in range(testcases):
    w, d, h = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    case1 = abs(x1-x2) + y1 + y2 + h
    case2 = abs(d-y1) + abs(d-y2) + abs(x1-x2) + h
    case3 = h + abs(y1-y2) + x1 + x2
    case4 = h + abs(y1-y2) + (w-x1) + (w-x2)

    print(min(case1, case2, case3, case4))
