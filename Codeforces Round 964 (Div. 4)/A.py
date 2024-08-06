import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = input().strip()
  a, b = map(int, [n[0], n[1]])
  print(a+b)