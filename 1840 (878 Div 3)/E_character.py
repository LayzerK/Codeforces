import sys
input = sys.stdin.readline
from collections import deque
def solve():
    s1 = list(input().strip())
    s2 = list(input().strip())

    t,qs = map(int, input().strip().split())

    time = 0
    diff = 0

    blocked = deque()
    for a,b in zip(s1, s2):
        diff += int(a!=b)
    

    for query in range(qs):
        q = list(map(int, input().strip().split()))

        if blocked and blocked[0][1] == time-t:
            first = blocked.popleft()
            second = blocked.popleft()

            if first != second:
                diff += 1
            
        if q[0] == 1:
            i = q[1] - 1

            blocked.append((s1[i], time))
            blocked.append((s2[i], time))

            if s1[i] != s2[i]:
                diff -= 1

            
        elif q[0] == 2:
            a, b = q[1], q[3]
            i, j = q[2]-1, q[4]-1

           
            pre = int(s1[i] == s2[i]) + int(s1[j] == s2[j])

            if a == 1 and b == 2:
                s1[i], s2[j] = s2[j], s1[i]
            elif a == 2 and b == 1:
                s1[j], s2[i] = s2[i], s1[j]
            elif a == 1:
                s1[i], s1[j] = s1[i], s2[j]
            else:
                s2[i], s2[j] == s2[j], s2[i]

            post = int(s1[i] == s2[i]) + int(s1[j] == s2[j])

            diff += (pre-post)

            #print(pre, post, diff, "in case 2")
            #print(s1, s2)
        else:
            #print(diff, "diff")
            if not diff:
                print("YES")
            else:
              print("NO")
        time += 1

for tc in range(int(input())):
    solve()