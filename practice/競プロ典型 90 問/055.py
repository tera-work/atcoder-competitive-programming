# Problem: 055 (Select 5（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bc

# Approach: 全探索ですべての組み合わせを計算し、Pで割るとQ余る組み合わせの数を出力する。

# Time Complexity: O(N ^ 5)

import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

tmp = 0
ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                for m in range(l+1, N):
                    tmp = A[i] % P
                    tmp = (tmp * A[j]) % P
                    tmp = (tmp * A[k]) % P
                    tmp = (tmp * A[l]) % P
                    tmp = (tmp * A[m]) % P
                    
                    if tmp == Q:
                        ans += 1

print(ans)