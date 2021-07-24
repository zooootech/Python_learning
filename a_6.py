# ○✕ゲーム
# https://atcoder.jp/contests/past202012-open/tasks/past202012_a

S = input()
S = input()

count_a = 0
count_b = 0

for i in range(len(S) - 3 + 1):
  if S[i] == "o":
    count_a += 1
    if S[i+1] == "o":
      count_a += 1
      if S[i+2] == "o":
        count_a += 1
        break
  else:
    count_b += 1
    if S[i+1] == "x":
      count_b += 1
      if S[i+2] == "x":
        count_b += 1
        break
  
  count_a = 0
  count_b = 0
  
if count_a == 3:
  print("o")
elif count_b == 3:
  print("x")
else:
  print("draw")