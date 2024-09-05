import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    board = []
    cnt = 0
    for i in range(n):
        x, y = map(int, input().split())
        board.append([x,y])
    board.sort()
    idx = 0
    for i in range(n):
        if board[i][1] == 0:
            if 0<= i+1 <n:
                if board[i+1][0] == board[i][0]:
                    cnt += (n-2)
            if 0<= i+2 <n:
                if board[i+1][0] == board[i][0]+1 and board[i+1][1] == 1:
                    if board[i+2][0] == board[i][0]+2 and board[i+2][1] == 0:
                        cnt += 1
            if 0<= i+3 <n:
                if board[i+2][0] == board[i][0]+1 and board[i+2][1] == 1:
                    if board[i+3][0] == board[i][0]+2 and board[i+3][1] == 0:
                        cnt += 1
            if 0<= i+4 <n:
                if board[i+3][0] == board[i][0]+1 and board[i+3][1] == 1:
                    if board[i+4][0] == board[i][0]+2 and board[i+4][1] == 0:
                        cnt += 1
        else:
            if 0<=i+1< n and board[i+1][0] == board[i][0]+1 and board[i+1][1] == 0:
                if 0<= i+2 <n and board[i+2][0] == board[i][0]+2 and board[i+2][1] == 1:
                    cnt += 1
                elif 0<=i+3<n and board[i+3][0] == board[i][0]+2 and board[i+3][1] == 1:
                    cnt += 1
                elif 0<=i+4<n and board[i+4][0] == board[i][0]+2 and board[i+4][1] == 1:
                    cnt += 1
    print(cnt)