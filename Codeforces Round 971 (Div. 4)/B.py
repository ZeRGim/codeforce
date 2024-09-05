import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    board = []
    res = []
    for i in range(n):
        board.append(list(input()))
    for i in range(-1, -len(board)-1, -1):
        res.append(str(board[i].index("#")+1))
    res = " ".join(res)
    print(res)