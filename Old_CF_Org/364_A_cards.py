import sys
input = sys.stdin.readline

n = int(input().strip())

arr = map(int, input().split())

sArr = sorted([(x, i+1) for i, x in enumerate(arr)])
offset = 0
for person in range(n//2):
    print(sArr[n-1-offset][1], sArr[offset][1])
    offset += 1
