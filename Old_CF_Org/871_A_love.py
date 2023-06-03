comp = "codeforces"

for tc in range(int(input())):
    diff = 0
    for c1, c2 in zip(comp, input()):
        if c1 != c2:
            diff += 1
    print(diff)
