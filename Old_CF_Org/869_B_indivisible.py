for tc in range(int(input())):

    size = int(input())

    if size == 1:
        print(1)
        continue
    if size % 2 == 1:
        print(-1)
        continue
    output = []
    for even in range(2, size+1, 2):
        output.append(str(even))
        output.append(str(even-1))
    print(" ".join(output))
