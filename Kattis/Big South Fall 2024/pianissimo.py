from collections import defaultdict
from bisect import bisect_left
def multiple_ints():
    return map(int, input().strip().split())

notes, changes = multiple_ints()

alts = {}

arr = []

for i in range(notes):
    arr.append(int(input()))

for i in range(changes):
    change_note, dynamic = input().strip().split()
    change_note = int(change_note)
    alts[change_note-1] = dynamic


mp = {
    "ppp": 0,
    "pp" : 1,
    "p": 2,
    "mp" : 3,
    "mf" : 4,
    "f" : 5,
    "ff" : 6,
    "fff" : 7,
}

dyn_notes = [[] for i in range(8)]
curr = ""
for i, power in enumerate(arr):
    if i in alts:
        curr = alts[i]

    dyn_notes[mp[curr]].append(power)

for dyn in dyn_notes:
    dyn.sort()

ans = 0

for i in range(8):
    for val in dyn_notes[i]:
        for j in range(i):
            ans += len(dyn_notes[j]) - bisect_left(dyn_notes[j], val)
print(ans)
    
