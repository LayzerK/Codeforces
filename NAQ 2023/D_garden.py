import sys
input = sys.stdin.readline
from math import sqrt
def multiple_ints():
    return map(int, input().strip().split())
def dist(x, y):
    return sqrt(x**2 + y**2)
def solve():
    n,radius,width,height = multiple_ints()

    plants = []

    for p in range(n):
        x,y,value = multiple_ints()
        plants.append((x,y,value))
    
    dists = []

    for x,y,value in plants:
        dists.append((dist(x,y), value))
    
    print(dists)
    


solve()
    