import sys
input = sys.stdin.readline
import math
t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input().strip())
    no = False
    if n == 1 and s[0] == "1":
        print("YES")
        continue
    if n == 4:
        if s == ["1","1","1","1"]:
            print("YES")
        else:
            if not no:
                print("NO")
                no = True
        continue
    rootn = math.sqrt(n)
    if rootn % 1 != 0:
        if not no:
            print("NO")
            no = True
        continue
    rootn = int(rootn)
    idx = 0
    for i in range(rootn):
        if s[idx] != "1":
            if not no:
                print("NO")
                no = True
                continue
        idx += 1
    for i in range(rootn-2):
        if s[idx] != "1":
            if not no:
                print("NO")
                no = True
                continue
        idx += 1
        for j in range(rootn-2):
            if s[idx] != "0":
                if not no:
                    print("NO")
                    no = True
                    continue
            idx += 1
        if s[idx] != "1":
            if not no:
                no = True
                print("NO")
                continue
        idx += 1
    for i in range(rootn):
        if s[idx] != "1":
            if not no:
                no = True
                print("NO")
                continue
        idx += 1
    if not no:
        print("YES")
