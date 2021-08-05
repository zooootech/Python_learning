# Cabbages
# https://atcoder.jp/contests/abc210/tasks/abc210_a

n, a, x, y = list(map(int, input().split(" ")))

if n <= a:
  print(n * x)
else:
  print(a * x + (n - a) * y)