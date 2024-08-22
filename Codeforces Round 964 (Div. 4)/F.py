import sys
input = sys.stdin.readline
import math
t = int(input())
facto = [1] * int(2e5+5)
for i in range(2, int(2e5+5)):
  facto[i] = facto[i-1] * i % int(1e9+7)
for _ in range(t):
  n, k = map(int, input().split())
  sequence = list(map(int, input().split()))
  ones = sum(sequence)
  zeros = n - ones
  atleast = (k+1)//2
  cnt = 0
  if atleast > ones:
    print("0")
    continue
  for i in range(atleast, min(k+1, ones+1)):
    cnt += ((facto[ones]//(facto[ones-i]*facto[i]))*(facto[zeros]//(facto[zeros-(k-i)]*facto[k-i])))%(1e9+7)
    cnt %= (1e9+7)
  print(int(cnt))