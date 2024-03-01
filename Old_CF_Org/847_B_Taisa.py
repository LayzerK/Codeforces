testcases = int(input())

for testcase in range(testcases):
    ndice, dicesum, remsum = map(int, input().split())

    missing = dicesum - remsum
    remdice = ndice-1
    print(missing)
    while remsum > 0:
        avg = remsum//remdice

        remsum -= avg
        print(avg)
        remdice -= 1
