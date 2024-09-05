import sys
input = sys.stdin.readline
import math
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    print(((n**2)+(2*k-1)*n)//2)