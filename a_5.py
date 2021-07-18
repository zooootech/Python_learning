# 中央値
# https://atcoder.jp/contests/past202010-open/tasks/past202010_a

A, B, C = list(map(int, input().split()))

S = sorted([A, B, C])

if S[1] == A:
  print("A")
elif S[1] == B:
  print("B")
else:
  print("C")