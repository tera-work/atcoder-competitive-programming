# Problem: ABC086A (Product)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/abc086_a

#  Approach: 入力を受け取り、a*bを奇数か偶数か判断して、その結果から文字列を出力

# Time Complexity: O(1)

a,b = map(int, input().split())

if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")