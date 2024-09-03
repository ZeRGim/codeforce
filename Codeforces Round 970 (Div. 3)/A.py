import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    b = b % 2
    if b == 0:
        if a % 2 == 0:
            print("YES")
            continue
        else:
            print("NO")
            continue
    else:
        if a >= 2 and a % 2 == 0:
            print("YES")
            continue
        else:
            print("NO")
            continue