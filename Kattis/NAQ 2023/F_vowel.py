import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    
    vowels_with_y = "aeiouy"
    vowels_without_y = "aeiou"

    with_y = 0
    without_y = 0

    s = input().strip()

    for char in s:
        if char in vowels_without_y:
            without_y += 1
        if char in vowels_with_y:
            with_y += 1
    print(without_y, with_y)

solve()
    