def func(n, s):
  rightmost = n-1
  for end in range(n-1, n//2, -1):
    suffixLength = n-end
    if s[end:n+1] == s[end-suffixLength:end][::-1]:
      missing = n-suffixLength * 2
      print(missing)
      print((s[:missing])[::-1])
      return
  print(n-1, s[:n-1][::-1])
  #if somethign is even: i.e. xxxY you can just add reversed(xxx)
  #if something is odd: i.e. xxxxY you can just add reversed (xxxx)

n = int(input())
s = "".join(input().strip().split())

if s == s[::-1]:
  print("yes")
else:
  func(n, s)
      

  