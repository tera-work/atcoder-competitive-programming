# Problem: 024 (Select +／- One（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_x

# Approach: A[i]をB[i]に変えるために必要な操作回数は|A[i]-B[i]|である。その合計をその合計をtempとする。temp<=Kかつ(K - temp)であるときYes。それ以外はNoを出力する。

# Time Complexity: O(N)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

temp = 0
for i in range(N):
    temp += abs(A[i] - B[i])
    
if temp <= K:
    if (K % 2) == (temp % 2):
        print("Yes")
    else:
        print("No")
else:
    print("No")