import sys
import math
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())


def dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)          
    
    

def solve():
    pX,pY = multiple_ints()
    aX, aY = multiple_ints()
    bX, bY = multiple_ints()

    a_to_origin = dist(0,0,aX, aY)
    b_to_origin = dist(0,0,bX, bY)

    a_to_house = dist(pX, pY, aX, aY)
    b_to_house = dist(pX, pY, bX, bY)

    a_to_b = dist(aX, aY, bX, bY)

    allA = max(a_to_origin, a_to_house)
    allB = max(b_to_origin, b_to_house)
    both = max(min(a_to_origin, b_to_origin), min(a_to_house, b_to_house), a_to_b/2)
    #print(allA, allB, both)
    print(min(allA, allB, both))
for tc in range(int(input())):
    solve()
    