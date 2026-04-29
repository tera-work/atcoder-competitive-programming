# Problem: 048 (I will not drop out（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_av

# Approach: 部分点と満点の差と部分点を大きい順にリストを作る。範囲Kの範囲の合計を出力する。

# Time Complexity: O(NlogN)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

S = []
for i in range(N):
    S.append(L[i][0] - L[i][1])
    S.append(L[i][1])

S.sort(reverse=True)

print(sum(S[:K]))