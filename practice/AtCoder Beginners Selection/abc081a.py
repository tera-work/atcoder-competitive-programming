# Problem: ABC081A (Placing Marbles)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/abc081_a

#  Approach: 入力文字列に対してループを用いて、1の出現回数を出力

# Time Complexity: O(N)

s = list(map(int, input()))

count = 0

for i in range(3):
    if s[i] == 1:
        count += 1
      
print(count)