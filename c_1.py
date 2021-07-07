# 3 番目
# https://atcoder.jp/contests/past201912-open/tasks/past201912_c

n = list(map(int, input().split()))

# sorted(iterable, *, key=None, reverse=False)
# 組み込み関数である sorted() 関数は、iterable の要素を並べ替えた新たなリストを返します。
# 2 つのオプション引数があり、これらはキーワード引数として指定されなければなりません。
# reverse は真偽値です。 True がセットされた場合、リストの要素は個々の比較が反転したものとして並び替えられます。
sn = sorted(n, reverse=True)
print(sn[2])

# -------------------------------------------------

n = list(map(int, input().split()))

# sort(*, key=None, reverse=False)
# リスト型のメソッドである sort() メソッドは、元のリスト自体が書き換えられる破壊的なソートを行います。
# sort() が返すのは None なので注意。
# デフォルトは昇順なので、降順にソートしたい場合は引数 reverse を True とする。
n.sort(reverse=True)
print(n[2])