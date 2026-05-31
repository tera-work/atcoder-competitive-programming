# Problem: A (Hell, World!)

# Contest: AtCoder Beginner Contest 459

# URL: https://atcoder.jp/contests/abc459/tasks/abc459_a

#  Approach: 文字列HelloWorldをリストとして持ち、X文字目を削除し、再び文字列に変換し出力する。

# Time Complexity: O(1)

X = int(input())

s = list("HelloWorld")
del s[X - 1]

print(''.join(s))