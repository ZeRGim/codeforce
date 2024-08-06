import sys
from collections import deque
import time
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  a, b = map(int, input().split())
  start = time.time()
  numbers = deque([i for i in range(a,b+1)])
  cnt = 0
  while numbers[0] != 0:
    numbers[0] = numbers[0] // 3
    cnt += 2
  numbers.popleft()
  for i in numbers:
    for j in range(13):
      if i // (3**j) < 3:
        cnt += j+1
        break
  end = time.time()
  print(end - start)
  print(cnt)