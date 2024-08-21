import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  s = list(input().strip())
  t = list(input().strip())
  pointer = 0
  counter = 0
  letters = []
  for i in s:
    try:
      if t[pointer] == i:
        pointer += 1
      if i == "?":
        counter += 1
        if pointer == len(t):
          letters.append(t[pointer])
        elif pointer < len(t):
          letters.append(t[pointer])
          pointer += 1
    except:
      pass
  if pointer != len(t):
    print("NO")
    continue
  print("YES")
  pointer2 = 0
  for i in s:
    if i != "?":
      print(i, end="")
    else:
      try:
        print(letters[pointer2], end="")
      except:
        print("a", end="")
      pointer2 += 1
  print()