# Problem: 069 (Colorful Blocks 2（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bq

# Approach: ブロックの数が1,2,3以上の場合に分けて、色の塗り方のパターン数を求める。

# Time Complexity: O(log N)

import sys
input = sys.stdin.readline

N, K = map(int,input().split())

mod = 10**9 + 7

if N == 1:
    print(K % mod)

elif N == 2:
    print(K * (K - 1) % mod)

elif K < 3:
    print(0)

else:
    ans = K * (K - 1) % mod
    ans *= pow(K - 2, N - 2, mod)
    ans %= mod

    print(ans)