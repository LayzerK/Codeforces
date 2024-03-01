import sys
input = sys.stdin.readline
for tc in range(int(input())):
    rLen, cLen = map(int, input().split())
    grid = []

    for row in range(rLen):
        grid.append(list(map(int, input().split())))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for x in range(cLen)] for y in range(rLen)]

    ans = 0

    for r in range(rLen):
        for c in range(cLen):
            if not visited[r][c] and grid[r][c] != 0:
                visited[r][c] = True
                q = []
                q.append((r, c))
                curr = 0
                while q:
                    row, col = q.pop()
                    curr += grid[row][col]
                    for dr, dc in directions:
                        NR = row + dr
                        NC = col + dc

                        if 0 <= NR < rLen and 0 <= NC < cLen and grid[NR][NC] != 0 and not visited[NR][NC]:
                            q.append((NR, NC))
                            visited[NR][NC] = True
                ans = max(ans, curr)
    print(ans)
