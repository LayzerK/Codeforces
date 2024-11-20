import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  t, textkey = input().strip().split(" ")
  plaintext = input().strip()
  np = []
  for char in plaintext:
    if char.isalpha():
      np.append(char.lower())
  plaintext = "".join(np)
  textkey += "!"

  def encrypt(textkey):
    i = 0
    n = len(plaintext)
    ans = [""] * n
    fwd = 1
    indices = list(range(n))
    for char in textkey:
      mv = ord(char) - ord('a') + 2 if char != "!" else 1
      iterator = range(mv-1, len(indices), mv) if fwd else range(len(indices)-mv, -1, -mv)
      rem = []

      for j in iterator:
        pi = indices[j] 
        if i == len(plaintext):
          break
        if ans[pi]:
          continue
        ans[pi] = plaintext[i]
        i += 1
        rem.append(pi)
      
      indices = [x for x in indices if x not in rem]

      fwd ^= 1
    return "".join(ans)

  def decrypt(textkey):
    original = []
    marked = [False] * len(plaintext)
    fwd = 1
    for char in textkey:
      mv = ord(char) - ord('a') + 2 if char != "!" else 1
      indices = list(range(len(plaintext)))
      for char in textkey:
        mv = ord(char) - ord('a') + 2 if char != "!" else 1
        iterator = range(mv-1, len(indices), mv) if fwd else range(len(indices)-mv, -1, -mv)
        rem = []

        for j in iterator:
          pi = indices[j] 
          if marked[pi]:
            continue
          original.append(plaintext[pi])
          marked[pi] = True
          rem.append(pi)
        
        indices = [x for x in indices if x not in rem]

        fwd ^= 1
      return "".join(original)
  

  if t == "E":
    print(encrypt(textkey))
  else:
    print(decrypt(textkey))
          


solve()
    