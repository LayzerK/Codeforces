for case in range(int(input())):
    n = int(input())
    arr = []
    for num in map(int, input().split()):
        arr.append(num)
    prior = arr[0]
    cnt = 0
    for i in range(1, len(arr)):
        if prior == 1:
            arr[i-1] += 1
            if i - 1 != 0:
                while arr[i-1] % arr[i-2] == 0:
                    arr[i-1] += 1
            prior = arr[i-1]
        while arr[i] % prior == 0:
            arr[i] += 1
        prior = arr[i]
    for num in arr:
        print(num)
