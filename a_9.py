# ケース・センシティブ
# https://atcoder.jp/contests/past202005-open/tasks/past202005_a

s = input()
t = input()

if s == t:
  print("same")
elif s.lower() == t.lower():
  print("case-insensitive")
else:
  print("different")