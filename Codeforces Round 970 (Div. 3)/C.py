import sys
input = sys.stdin.readline

t = int(input())
dp = [0]
for i in range(1,44722):
    dp.append(dp[i-1]+i)

for _ in range(t):
    l,r = map(int, input().split())
    dif = r - l
    cnt = 22361
    min_ = 0
    max_ = 44721
    while dp[cnt] > dif or dif >= dp[cnt+1]:
        if dp[cnt] < dif:
            min_ = cnt
            cnt = (cnt+max_) // 2
        else:
            max_ = cnt
            cnt = (cnt+min_)//2
    print(cnt+1)