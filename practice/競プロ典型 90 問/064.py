# Problem: 064 (Uplift（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bl

# Approach: Dという区画ごとの標高差を要素とするリストを作る。その差が変わる位置のみ、標高差を変化させる。最後に標高差の絶対値の和を出力する。

# Time Complexity: O(Q)

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

D = [A[i] - A[i-1] for i in range(1, N)]
total = sum(abs(d) for d in D)


for _ in range(Q):
    l, r, v = map(int, input().split())
    
    if l > 1:
        total -= abs(D[l-2])
        D[l-2] += v
        total += abs(D[l-2])
    
    if r < N:
        total -= abs(D[r-1])
        D[r-1] -= v
        total += abs(D[r-1])
    
    print(total)