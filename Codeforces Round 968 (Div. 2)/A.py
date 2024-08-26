import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  s = input().strip()
  for i in range(1,n):
    piece1 = s[0:i]
    piece2 = s[i:]
    if piece1[0] != piece2[-1]:
      print("YES")
      break
  else:
    print("NO")