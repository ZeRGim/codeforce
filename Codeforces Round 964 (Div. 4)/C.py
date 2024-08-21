# import sys
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n, s, m = map(int, input().split())
#     intervals = [0] * m
#     for i in range(n):
#         a,b = map(int, input().split())
#         for j in range(a,b):
#             intervals[j] = 1
#     cnt = 0
#     found = False
#     for i in intervals:
#         if i:
#             cnt = 0
#         else:
#             cnt += 1
#         if cnt == s:
#             found = True
#             break
#     if found:
#         print("YES")
#     else: print("NO")

# MEMORY EXCEED

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, s, m = map(int, input().split())
    intervals = [[0,0],[m,m]]
    for i in range(n):
        intervals.append(list(map(int, input().split())))
    intervals.sort()
    for i in range(1,len(intervals)):
        if intervals[i][0] - intervals[i-1][1] >= s:
            print("YES")
            break
    else:
        print("NO")