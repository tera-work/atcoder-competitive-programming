# Problem: 067 (Base 8 to 9（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bo

# Approach: 8進数を10進数に変え、それを9進数に変える。さらに9進数の8を5に変える。これを繰り返す。

# Time Complexity: O(K)

import sys
input = sys.stdin.readline

N, K = input().split()
K = int(K)

for _ in range(K):
    d = int(N, 8)

    if d == 0:
        N = "0"
    else:
        s = ""
        while d > 0:
            s += str(d % 9)
            d //= 9

        s = s[::-1]

        N = s.replace("8", "5")

print(N)

