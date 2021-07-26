# Vanishing Pitch
# https://atcoder.jp/contests/abc191/tasks/abc191_a

v, t, s, d = list(map(int, input().split()))

if v * t > d or v * s < d:
  print("Yes")
else:
  print("No")