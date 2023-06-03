import sys
input = sys.stdin.readline

for tc in range(int(input())):
    s = input()
    n = 0
    ones = 0
    zeros = 0
    for c in s:
        if c == "1":
            ones += 1
        elif c == "0":
            zeros += 1
    n = ones + zeros
    zeros = 0

    # let ones represent the number of 1s outside our window and zeros be the number of zeros in our window
    ans = n
    right = 0

    for left in range(n):
        while right < n and zeros < ones:
            if s[right] == "0":
                # print("here")
                zeros += 1
            else:
                ones -= 1
            right += 1
        #print(ans, zeros, ones)
        #print(left, right, zeros, ones, s[left:right+1])
        ans = min(ans, max(zeros, ones))
        if s[left] == "0":
            zeros -= 1
        else:
            ones += 1
    print(ans)
