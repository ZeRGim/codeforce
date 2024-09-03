import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
t = int(input())

def solve(x: int):
    global cnt
    if bw[x] == "0":
        cnt += 1
    if not visited[arr[x]]:
        visited[arr[x]] = 1
        solve(arr[x])
        visited[arr[x]] = 0

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    bw = list(input())
    arr.insert(0,0)
    bw.insert(0,"0")
    visited = [0]*(n+1)
    for i in range(1,n+1):
        cnt = 0
        visited[i] = 1
        solve(i)
        visited[i] = 0
        print(cnt, end=" ")
    print()