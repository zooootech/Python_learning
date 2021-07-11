# 3 番目
# https://atcoder.jp/contests/past201912-open/tasks/past201912_c

a = list(map(int, input().split()))

# sorted(iterable, *, key=None, reverse=False)
# 組み込み関数である sorted() は、iterable の要素を並べ替えた新たなリストを返します。
# 2 つのオプション引数があり、これらはキーワード引数として指定されなければなりません。
# reverse は真偽値です。 True がセットされた場合、リストの要素は個々の比較が反転したものとして並び替えられます。
sa = sorted(a, reverse=True)
print(sa[2])

# -------------------------------------------------

a = list(map(int, input().split()))

# sort(*, key=None, reverse=False)
# リスト型のメソッドである sort() は、元のリスト自体が書き換えられる破壊的なソートを行います。
# sort() が返すのは None なので注意。
# デフォルトは昇順なので、降順にソートしたい場合は引数 reverse を True とする。
a.sort(reverse=True)
print(a[2])

# -------------------------------------------------

a = list(map(int, input().split()))
a.sort()
print(a[-3])