pi = str(314159265358979323846264338327)

test_cases = int(input())

for case in range(test_cases):
    right = 0
    digits = str(input())

    for i, digit in enumerate(digits):
        if digit == pi[i]:
            right += 1
        else:
            break
    print(right)
