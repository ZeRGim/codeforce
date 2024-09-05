import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    if n == 1:
        print("1")
        continue
    if n == 2:
        if s[0] != s[1]:
            print("0")
            continue
        else:
            print("1")
            continue
    if n % 2 == 1:
        pass