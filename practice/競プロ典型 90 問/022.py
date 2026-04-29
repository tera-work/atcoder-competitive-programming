# Problem: 022 (Cubic Cake（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_v

# Approach: 3つの辺の最大公約数を求める。1辺の長さがgになるようにそれぞれの辺の長さをgで割る。切断回数を合計する。

# Time Complexity: O(log min(A,B,C))

import sys
input = sys.stdin.readline
import math

A, B, C = map(int, input().split())
g = math.gcd(A,B,C)

print((A + B + C) // g - 3)