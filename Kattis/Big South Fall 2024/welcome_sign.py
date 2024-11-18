from math import ceil
def multiple_ints():
    return map(int, input().strip().split())

rLen, cLen = multiple_ints()

words = []

for word in range(rLen):
    words.append(input().strip())

ans = []
bias = 0
for i, word in enumerate(words):


    size = len(word)

    rem = cLen - size

    if rem % 2 != 0:
        bias += 1

    lbias = True if (bias) % 2 == 0 else False

    lside = rem//2 if not lbias else ceil(rem/2)
    rside = rem//2 if lbias else ceil(rem/2)

    dis = "." *lside + word + "." * rside

    ans.append(dis)

for w in ans:
    print(w)
