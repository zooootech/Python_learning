# Bingo
# https://atcoder.jp/contests/abc157/tasks/abc157_b

A = []
for _ in range(3):
  A.append(list(input().split()))

M = [[False for _ in range(3)] for _ in range(3)]

N = int(input())
for _ in range(N):
  b = input()

  for i in range(3):
    for j in range(3):
      if A[i][j] == b:
        M[i][j] = True

bingo = False

for i in range(3):
  # i 行目の 3 つに印が付いているか調べる
  if M[i][0] and M[i][1] and M[i][2]:
    bingo = True

for i in range(3):
  # i 列目の 3 つに印が付いているか調べる
  if M[0][i] and M[1][i] and M[2][i]:
    bingo = True

# 左上から右下にかけて、斜めに 3 つ印が付いているか調べる
if M[0][0] and M[1][1] and M[2][2]:
  bingo = True

# 右上から左下にかけて、斜めに 3 つ印が付いているか調べる
if M[0][2] and M[1][1] and M[2][0]:
  bingo = True

if bingo:
  print("Yes")
else:
  print("No")

# -------------------------------------------------

A = []
for _ in range(3):
  A.append(list(input().split()))

M = [[False for _ in range(3)] for _ in range(3)]

N = int(input())
for _ in range(N):
  b = input()

  for i in range(3):
    for j in range(3):
      if A[i][j] == b:
        M[i][j] = True

bingo = "No"

for i in range(3):
  # i 行目の 3 つに印が付いているか調べる
  if M[i][0] and M[i][1] and M[i][2]:
    bingo = "Yes"

for i in range(3):
  # i 列目の 3 つに印が付いているか調べる
  if M[0][i] and M[1][i] and M[2][i]:
    bingo = "Yes"

# 左上から右下にかけて、斜めに 3 つ印が付いているか調べる
if M[0][0] and M[1][1] and M[2][2]:
  bingo = "Yes"

# 右上から左下にかけて、斜めに 3 つ印が付いているか調べる
if M[0][2] and M[1][1] and M[2][0]:
  bingo = "Yes"

print(bingo)

# -------------------------------------------------

a = []
for i in range(3):
  a.append(list(input().split()))

N = int(input())
for _ in range(N):
  b = input()
  
  for i in range(3):
    for j in range(3):
      if a[i][j] == b:
        a[i][j] = "mark"

bingo = "No"

for i in range(3):
  if a[i].count("mark") == 3:
    bingo = "Yes"

for i in range(3):
  if a[0][i] == "mark" and a[1][i] == "mark" and a[2][i] == "mark":
    bingo = "Yes"
    
if a[0][0] == "mark" and a[1][1] == "mark" and a[2][2] == "mark":
  bingo = "Yes"
  
if a[0][2] == "mark" and a[1][1] == "mark" and a[2][0] == "mark":
  bingo = "Yes"
  
print(bingo)