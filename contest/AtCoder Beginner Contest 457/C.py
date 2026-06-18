# Problem: C (Long Sequence)

# Contest: AtCoder Beginner Contest 457

# URL: https://atcoder.jp/contests/abc457/tasks/abc457_c

# Approach: 配列の要素数から、答えがある行を特定し、そこから答えを導く。

# Time Complexity: O(N)

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
a = [list(map(int,input().split(" "))) for _ in range(N)]
c = list(map(int, input().split()))

for i in range(N):
    K -= c[i]*a[i][0]
    if K <= 0:
        if (K+c[i]*a[i][0]) % a[i][0] == 0:
            print(a[i][-1])
            break
        else:
            K = (K+c[i]*a[i][0]) % a[i][0]
            print(a[i][K])
            break