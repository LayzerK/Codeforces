for tc in range(int(input())):
    n = int(input())
    a = 10**20
    b = 10**20
    both = 10**20

    for book in range(n):
        cost, gain = map(int, input().split())

        if gain & 1 and gain & 2:
            both = min(both, cost)
        elif gain & 1:
            a = min(a, cost)
        elif gain & 2:
            b = min(b, cost)
    final = min(a+b, both)
    if final == 10**20:
        final = -1
    print(final)
