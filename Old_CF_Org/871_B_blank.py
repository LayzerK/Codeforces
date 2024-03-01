for tc in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))

    mx = 0
    curr = 0

    for c in arr:
        if not c:
            curr += 1
        else:
            curr = 0
        mx = max(mx, curr)
    print(mx)
