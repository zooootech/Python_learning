# エレベーター
# https://atcoder.jp/contests/past202004-open/tasks/past202004_a

a = ["B9", "B8", "B7", "B6", "B5", "B4", "B3", "B2", "B1", "1F", "2F", "3F", "4F", "5F", "6F", "7F", "8F", "9F"]
S, T = list(input().split())

print(abs(a.index(S) - a.index(T)))

# -------------------------------------------------

# 上の階が下の階の整数 + 1 になるように、各階に整数を割り当てます。
# 今回は B9, B8, ..., B1 に -8, -7, ..., 0 を割り当て、1F, 2F, ..., 9F に 1, 2, ..., 9 を割り当てます。

def to_int(f):
  if f[0] == "B":
    return - (int(f[1]) - 1)
  return int(f[0])

f1, f2 = input().split()
print(abs(to_int(f1) - to_int(f2)))