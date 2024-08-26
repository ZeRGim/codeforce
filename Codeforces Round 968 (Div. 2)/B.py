import sys
input = sys.stdin.readline
from collections import deque
t = int(input())

for _ in range(t):
  n = int(input())
  nums = list(map(int, input().split()))
  nums.sort()
  nums = deque(nums)
  while len(nums) > 1:
    #turtle's turn
    nums.popleft()
    if len(nums) == 1:
      break
    #piggy's turn
    nums.pop()
  print(nums[0])
