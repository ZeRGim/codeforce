import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  a1, a2, b1, b2 = map(int, input().split())
  sunnet = list([a1, a2])
  slavic = list([b1, b2])
  win = 0
  for i in range(2):
    cnt = 0
    if sunnet[0] > slavic[0]:
      cnt += 1
    elif sunnet[0] == slavic[0]:
      pass
    else:
      cnt -= 1
    if sunnet[1] > slavic[1]:
      cnt += 1
    elif sunnet[1] == slavic[1]:
      pass
    else:
      cnt -= 1
    if cnt > 0: win += 1
    sunnet.reverse()
  print(win*2)