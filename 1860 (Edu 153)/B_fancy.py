import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    m,k,reg_one,reg_k = multiple_ints()


    total_k = k*min(reg_k, m//k)

    take_all = total_k + reg_one


    if take_all >= m:
        print("0")
        return
    
    shortfall = m-take_all

    req = shortfall%k + shortfall//k

    if reg_one >= k-shortfall%k:  #reduce the number of normal 1s that we use SUCH that we can use 1 extra fancy K coin
        req = min(req, shortfall//k + 1)

    print(req)


for tc in range(int(input())):
    solve()