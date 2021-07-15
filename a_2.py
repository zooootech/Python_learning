# Rolling Dice
# https://atcoder.jp/contests/abc208/tasks/abc208_a

A, B = list(map(int, input().split()))

if A <= B <= A * 6:
  print("Yes")
else:
  print("No")