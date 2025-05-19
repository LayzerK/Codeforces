import sys
input = sys.stdin.readline

def solve():
    mapping = {1:1, 10:1, 2:2, 9:2, 3:3, 8:3, 4:4, 7:4, 5:5, 6:5}
    ans = 0
    for row in range(1, 11):
        curr = input().strip()

        for i,val in enumerate(curr):
          if val == "X":
              if mapping[row] <= i+1 <= 10-(mapping[row]-1):
                  #print(row, i+1, mapping[row], "row val")
                  ans += mapping[row]
              else:
                  #print(row, i+1, mapping[i+1])
                  ans += mapping[i+1]
    print(ans)
            

for tc in range(int(input())):
    solve()