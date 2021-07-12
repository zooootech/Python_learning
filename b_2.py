# Factorial Yen Coin
# https://atcoder.jp/contests/abc208/tasks/abc208_b

# -------------------------------------------------

# 貪欲法

# factorial(x) は、 x の階乗を整数で返します。 x が整数でないか、負の数の場合は、 ValueError を送出します。
# math モジュールの、階乗を返す関数 factorial() をインポート
from math import factorial

p = int(input())

ans = 0

for i in range(10, 0, -1):
  print(i)
  while factorial(i) <= p:
    p -= factorial(i)
    ans += 1

print(ans)

# -------------------------------------------------

# 貪欲法

p = int(input())

coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
result = 0

# スライスを用いて、対象の range オブジェクトの逆順を生成
for i in range(0, 10)[::-1]:
  if coins[i] <= p:
    # print(f"coins[i] は {coins[i]}")
    result += p // coins[i]
    # print(f"result は {result}")
    p %= coins[i]
    if p == 0:
      break

print(result)

# -------------------------------------------------

# 貪欲法

p = int(input())

coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
result = 0

# range(start, stop[, step])
# step 引数に負の数を指定し、適切な値を start と stop に指定することで降順の range オブジェクトを生成する
# step 引数が省略された場合のデフォルト値は 1 です。
# start 引数が省略された場合のデフォルト値は 0 です。
for i in range(9, -1, -1):
  if coins[i] <= p:
    # print(f"coins[i] は {coins[i]}")
    result += p // coins[i]
    # print(f"result は {result}")
    p %= coins[i]
    if p == 0:
      break

print(result)

# -------------------------------------------------

# 貪欲法

p = int(input())

coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
result = 0

# 組み込み関数 reversed(seq) は、指定されたシーケンシャルオブジェクトを逆順にしたイテレータを返します。
for i in reversed(range(0, 10)):
  if coins[i] <= p:
    # print(f"coins[i] は {coins[i]}")
    result += p // coins[i]
    # print(f"result は {result}")
    p %= coins[i]
    if p == 0:
      break

print(result)