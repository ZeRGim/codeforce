import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  s = list(input().strip())
  t = list(input().strip())
  mul = []
  tin = []
  for i in range(s):
    if s[i] == "?":
      mul.append(i)
  for i in range(t):
    if t[i] in s:
      for j in range(s):
        if s[j] == t[i]:
          pass