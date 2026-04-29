# Problem: 014 (We Used to Sing a Song Together（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_n

# Approach: AとBをそれぞれソートし、同じインデックス同士の差の絶対値の合計を求める

# Time Complexity: O(N log N)

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

ans = 0
for i in range(N):
    ans += abs(B[i] - A[i])

print(ans)