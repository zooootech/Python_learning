# 多数決
# https://atcoder.jp/contests/past202004-open/tasks/past202004_b

s = input()

na = s.count("a")
nb = s.count("b")
nc = s.count("c")

mx = max(na, nb, nc)

if mx == na:
  print("a")
elif mx == nb:
  print("b")
else:
  print("c")