# Problem: 010 (Score Sum Queries（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_j

# Approach: 与えられた数によって合計値のリストを２つ作り、答えを求める

# Time Complexity: O(N + Q)

import sys
input = sys.stdin.readline

N = int(input())

sum1 = [0] * (N + 1)
sum2 = [0] * (N + 1)

for i in range(1, N + 1):
    c, p = map(int, input().split())
    
    sum1[i] = sum1[i-1]
    sum2[i] = sum2[i-1]
    
    if c == 1:
        sum1[i] += p
    else:
        sum2[i] += p

Q = int(input())
for j in range(Q):
    L, R = map(int, input().split())
    
    ans1 = sum1[R] - sum1[L-1]
    ans2 = sum2[R] - sum2[L-1]
    
    print(ans1, ans2)