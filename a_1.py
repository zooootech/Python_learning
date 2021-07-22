# Welcome to AtCoder
# https://atcoder.jp/contests/practice/tasks/practice_1

a = int(input())

# map(function, iterable, ...)
# 組み込み関数である map() は、function を、結果を返しながら iterable の全ての要素に適用するイテレータを返します。
# str.split(sep=None, maxsplit=-1)
# 文字列メソッドである split() は、文字列を sep をデリミタ文字列として区切った単語のリストを返します。
# リストオブジェクトを複数の変数に同時代入
b, c = list(map(int, input().split()))
s = input()

print(f"{a + b + c} {s}")

# -------------------------------------------------

a = int(input())

# map 型のオブジェクト（イテレータ）を複数の変数に同時代入
b, c = map(int, input().split())
s = input()

# str.format(*args, **kwargs)
# 文字列の書式化操作を行います。このメソッドを呼び出す文字列は通常の文字、または、 {} で区切られた置換フィールドを含みます。
# それぞれの置換フィールドは位置引数のインデックスナンバー、または、キーワード引数の名前を含みます。
# 返り値は、それぞれの置換フィールドが対応する引数の文字列値で置換された文字列のコピーです。
# 置換フィールドの数と引数の数が単純に左から順に一対一になっている場合は、以下のようにインデックス番号を省略できます。
print("{} {}".format(a + b + c, s))

# -------------------------------------------------

a = int(input())

# map 型のオブジェクト（イテレータ）を複数の変数に同時代入
b, c = map(int, input().split())
s = input()

# {0} や {1} のように{}内に整数値を指定すると引数の順番に応じて出力される。同じ番号を繰り返し使うこともできる。
print("{0} {1}".format(a + b + c, s))

# -------------------------------------------------

a = int(input())

# map 型のオブジェクト（イテレータ）を複数の変数に同時代入
b, c = map(int, input().split())
s = input()

# {} 内に任意の名前を指定し、キーワード引数として入力することも可能。
print("{sum} {str}".format(sum=a + b + c, str=s))