# ○✕ゲーム
# https://atcoder.jp/contests/past202012-open/tasks/past202012_a

S = input()
ans = "draw"
if S[0] == S[1] == S[2]:
    ans = S[0]
if S[1] == S[2] == S[3]:
    ans = S[1]
if S[2] == S[3] == S[4]:
    ans = S[2]
print(ans)

# -------------------------------------------------

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