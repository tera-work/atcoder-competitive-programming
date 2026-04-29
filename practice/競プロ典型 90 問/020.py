# Problem: 020 (Log Inequality（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_t

# Approach: 初めはmath.log2を用いた比較を検討したが、浮動小数点数に計算誤差によりエラーが発生した。そのため、対数ではなく整数の累乗比較を用いて比較を行った。

# Time Complexity: O(log b)

import sys
input = sys.stdin.readline
import math

a, b, c = map(int, input().split())

if a < pow(c, b):
    print("Yes")
else:
    print("No")