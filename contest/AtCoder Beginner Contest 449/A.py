# Problem: A (π)

# Contest: AtCoder Beginner Contest 449

# URL: https://atcoder.jp/contests/abc449/tasks/abc449_a

#  Approach: Dを円の面積の公式に基づき計算する

# Time Complexity: O(1)

# 解説後理解：浮動小数点誤差について意識が足りず、エラーになる可能性のあるコードだった

import math

D = int(input())
print((D/2) ** 2 * math.pi)