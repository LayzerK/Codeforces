from collections import defaultdict
numbits = int(input())
num1 = input()
num2 = input()

# 01011
# 11001

# two ways to stop

# if a position is 1/1 you can make no swaps in

# if a position is 0/1 you cannot swap in anything to change

# the only time A has power is if it is 0 currently OR if it is 1 and B is 0

# two cases 0/0 and 1/0

# if it is 0/0 you can swap with all eligible 1s

# if it is 1/0 you can swap with all eligible 0s
counts = defaultdict(int)
ways = 0
for binary in num1:
    counts[int(binary)] += 1
cnt = 0
for a, b in zip(num1, num2):
    if int(a) == 0 and int(b) == 0:
        ways += counts[1]
        counts[0] -= 1
    elif int(a) == 1 and int(b) == 0:
        ways += counts[0]
        counts[1] -= 1
print(ways)
