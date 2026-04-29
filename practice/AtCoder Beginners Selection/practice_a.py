# Problem: practice_1 (Welcome to AtCoder)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/practice_1

#  Approach: 入力を受け取り、a+b+cを計算して文字列とともに出力

# Time Complexity: O(1)

a = int(input())
b,c = map(int, input().split())
s = input()

print(a+b+c, s)
