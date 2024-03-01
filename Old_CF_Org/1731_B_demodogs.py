testcases = int(input())

for testcase in range(testcases):
    n = int(input())
    killed = 2*(n*(n+1)*((2*n+1))//6) - (n*(n+1))//2
    # series is sum of i^2 + i^2 - i from 1 to N

    # 2(n(n+1)(2n+1)/6) - (n(n+1)/2)

    killed *= int(2022)
    killed %= int((10**9 + 7))
    print(int(killed))
