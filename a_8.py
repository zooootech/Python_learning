# POSTal Code
# https://atcoder.jp/contests/past202104-open/tasks/past202104_a

S = input()
flag = True

if S[3] == "-":
  for i in range(len(S)):
    # i が 3 のとき処理をスルーする
    if i == 3:
      continue

    # str.isdecimal() は文字列が十進数字か判定する
    if not S[i].isdecimal():
      flag = False
      break
else:
  flag = False

if flag:
  print("Yes")
else:
  print("No")

# -------------------------------------------------

S = input()
if S[3] == '-' and S.count('-') == 1:
    print("Yes")
else:
    print("No")