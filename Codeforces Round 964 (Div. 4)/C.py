import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, s, m = map(int, input().split())
    intervals = []
    for i in range(n):
        start, end = map(int, input().split())
        intervals.append((start, end))
    
    covered = [0] * (m + 1)
    for start, end in intervals:
        for j in range(start, end):
            covered[j] = 1
    
    found = False
    for i in range(m - s + 1):
        if sum(covered[i:i+s]) == 0:
            found = True
            break
    
    if found:
        print("YES")
    else:
        print("NO")