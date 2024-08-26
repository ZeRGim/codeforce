import sys
input = sys.stdin.readline
from collections import deque
t = int(input())

for _ in range(t):
  length = int(input())
  s = list(input().strip())
  s.sort()
  s = deque(s)
  