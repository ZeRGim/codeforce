import sys
input = sys.stdin.readline

import itertools

t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  sequence = list(map(int, input().split()))
  subsequence = itertools.combinations(sequence, k)
  median_sum = 0
  for i in subsequence:
    i = list(i)
    i.sort()
    median = i[((k+1) // 2)-1]
    median_sum += median
  print(median_sum % (10**9+7))