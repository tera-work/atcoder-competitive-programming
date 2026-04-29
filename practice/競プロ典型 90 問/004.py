# Problem: 004 (Cross Sum（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_d

# Approach: 各行、列の合計値を求め、それを用いて新しいリストを作る

# Time Complexity: O(HW)

H, W = map(int, input().split())
A = []

for i in range(H):
    temp = list(map(int, input().split()))
    A.append(temp)

row_sum = [0] * H
col_sum = [0] * W
ans = []

for j in range(H):
    for k in range(W):
        row_sum[j] += A[j][k]
        col_sum[k] += A[j][k]

ans = [[0] * W for _ in range(H)]

for j in range(H):
    for k in range(W):
        ans[j][k] = row_sum[j] + col_sum[k] - A[j][k]

for row in ans:
    print(*row)