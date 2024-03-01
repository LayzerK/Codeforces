for case in range(int(input())):
    fixes = []
    n = int(input())
    for fix in input().split():
        fixes.append(fix)
    fixes.sort(key=len)
    #print(fixes, fixes[0], fixes[1], fixes[-1][::-1], fixes[-2])
    if fixes[0] == fixes[1] and fixes[-1][::-1] == fixes[-2]:
        print("yes")
    else:
        print("no")
