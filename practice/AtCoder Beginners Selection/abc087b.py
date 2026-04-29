# Problem: ABC087B (Coins)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/abc087_b

#  Approach: 入力数の計算範囲内で全探索して、合計金額がXになる組み合わせを数える

# Time Complexity: O(A × B × C)

A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            total = 500 * i + 100 * j + 50 * k
            if total == X:
                ans += 1

print(ans)