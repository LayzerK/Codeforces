for tc in range(int(input())):
    starting, target = map(int, input().split())

    def dfs(curr):
        if curr == target:
            return True
        if curr % 3 != 0 or curr < target:
            return False

        return dfs((curr//3)*2) or dfs(curr//3)

    if dfs(starting):
        print("yes")
    else:
        print("no")
