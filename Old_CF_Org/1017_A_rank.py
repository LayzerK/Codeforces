n = int(input())
ranking = []

for sid in range(n):
    student = sum(map(int, input().split()))
    ranking.append((student, -sid))

ranking.sort(reverse=True)
pos = 1
for s, sid in (ranking):
    if sid == 0:
        print(pos)
    pos += 1
