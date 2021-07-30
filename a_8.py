# POSTal Code
# https://atcoder.jp/contests/past202104-open/tasks/past202104_a

S = input()
flag = True

if S[3] == "-":
  for i in range(len(S)):
    if i == 3:
      continue

    if not S[i].isdigit():
      flag = False
      break
else:
  flag = False

if flag:
  print("Yes")
else:
  print("No")