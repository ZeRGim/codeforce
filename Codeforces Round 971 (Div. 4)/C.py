import sys
input = sys.stdin.readline
import math
t = int(input())

for _ in range(t):
    x, y, d = map(int, input().split())
    x_ = x // d
    y_ = y // d
    if x % d > 0:
        x_ += 1
    if y % d > 0:
        y_ += 1
    if x_ > y_:
        print(x_*2 - 1)
    elif x_ <= y_:
        print(y_*2)
    