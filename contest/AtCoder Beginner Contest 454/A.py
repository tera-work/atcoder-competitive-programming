# Problem: A (Closed interval)

# Contest: AtCoder Beginner Contest 454

# URL: https://atcoder.jp/contests/abc454/tasks/abc454_a

# Approach: 数を受け取り、その範囲にある整数の数を出力する。

# Time Complexity: O(1)

import sys
input = sys.stdin.readline

L, R = map(int, input().split())

print(R-L+1)