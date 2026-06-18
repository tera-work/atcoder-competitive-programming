# Problem: B (Count Adjacent Cells)

# Contest: AtCoder Beginner Contest 458

# URL: https://atcoder.jp/contests/abc458/tasks/abc458_b

# Approach: 隣接マスの最大値4で配列を作り、グリッドの行と列の端にあたる場合-1を行う。

# Time Complexity: O(H * W)

H, W = map(int, input().split())

a = [[4 for j in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0:
            a[i][j] -= 1
        if j == 0:
            a[i][j] -= 1
        if i == H-1:
            a[i][j] -= 1
        if j == W-1:
            a[i][j] -= 1
        
for row in a:
    print(*row)