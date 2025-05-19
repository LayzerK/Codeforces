import sys
input = sys.stdin.readline

def solve():
    n, target = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))

    banned = []

    for i in range(32):
        if target & (1<<i) == 0:
            
            banned.append(i)
    #print(banned)
    amax = 0
    bmax = 0
    cmax = 0
    av = True
    bv = True
    cv = True
    for i in range(n):
        anxt = amax | a[i]
        bnxt = bmax | b[i]
        cnxt = cmax | c[i]

        for bit in banned:
            if (1<<bit) & anxt:
                av = False
            if (1<<bit) & bnxt:
                bv = False
            if (1<<bit) & cnxt:
                cv = False
        #print(cv, cmax, cnxt, cnxt & 1<<3)
        if av:
            amax = anxt
        if bv:
            bmax = bnxt
        if cv:
            cmax = cnxt
    #print(amax, bmax, cmax,"HERE")
    if amax | bmax | cmax == target:
        print("YES")
    else:
        print("NO")
              


for tc in range(int(input())):
    solve()