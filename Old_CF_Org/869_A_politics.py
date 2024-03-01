for tc in range(int(input())):
    n, k = map(int, input().split())

    opinions = [[False for x in range(n)] for case in range(k)]

    for person in range(n):
        opinion = input()

        for i, take in enumerate(opinion):
            if take == "+":
                opinions[i][person] = True
            else:
                opinions[i][person] = False
    present = [True] * n

    for case in range(k):
        us = opinions[case][0]

        for person in range(n):
            if opinions[case][person] != us:
                present[person] = False
    print(sum(present))
