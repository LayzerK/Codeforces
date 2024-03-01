import sys
input = sys.stdin.readline

"""
observation 1: the biggest element will always come up to the front
unless* it is already there
in that case, it is the second

So all valid permutation swaps will just be from 1:right before max
OR in the case of arr[1] being the max
from 1: from 1 to right before the second max

define the first case as case1 and the second case as case2

#the question then becomes, where do you decide to start the prefix

my intuition is that you will end your prefix right at the greatest number found
before the  maximum in case 1

the segment you choose does have to be non-empty

For case 2 it seems like you end your prefix at the minimum before the second mx


(using 1 indexing)

#bugging out on second and second to last

the commonality of those seems to be that the number we are searching for is the last number

now bugging out on 
6
3 2 4 1 5 6

seems to be that you have an empty right iff the first element is less than the element right before the max AND the max is the last element

The last edge case which doesn't actually appear in tests is when you want to move your reversal front backwards and chop off the prefix

"""


def solve():
    n = int(input())
    perm = list(map(int, input().strip().split()))

    if len(perm) == 1:
        print(1)
        return
    
    split = 0

    #case 1
    if perm[0] == n:
        for i,num in enumerate(perm):
            if num == n-1:
                newleft = i
    else:
        for i,num in enumerate(perm):
            if num == n:
                newleft = i

    ans = []
    #if the last element is the right shitter then we have to do that special case where potentially have no right frontier
    if newleft == n-1:
        ans = [perm[newleft]]
        reversal = newleft-1
        while reversal > 0 and perm[reversal] > perm[0]:
            ans.append(perm[reversal])
            reversal -= 1
        for prefix in range(reversal+1):
            ans.append(perm[prefix])
    else:
        #otherwise we just move the reversal frontier as far back as possible
        #first, get all the newleft elements
        reversal = newleft - 1
        while newleft < n:
            ans.append(perm[newleft])
            newleft += 1
        
        #reversal segment has to be at least size 1
        ans.append(perm[reversal])
        reversal -= 1

        while reversal > 0 and perm[reversal] > perm[0]:
            ans.append(perm[reversal])
            reversal -= 1
        
        #get suffix

        for i in range(reversal+1):
            ans.append(perm[i])


    print(*ans)
for tc in range(int(input())):
    solve() 