import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dp = [0]*200001
dp[1] = 1
dp[2] = 1
for i in range(3,200001):
  dp[i] = dp[i//3] + 1
dp1 = [0]*200001
dp1[1] = 1
dp1[2] = 2
for i in range(3,200001):
  dp1[i] = dp1[i-1] + dp[i]
for _ in range(t):
  a, b = map(int, input().split())
  cnt = 0
  num = a
  while num != 0:
    num = num // 3
    cnt += 2
  cnt = cnt + (dp1[b] - dp1[a])
  print(cnt)