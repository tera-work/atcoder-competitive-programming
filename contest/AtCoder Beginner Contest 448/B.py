# Problem: B (Pepper Addiction)

# Contest: AtCoder Beginner Contest 448

# URL: https://atcoder.jp/contests/abc448/tasks/abc448_b

# Approach: 各種類ごとの数量の合計を配列で管理する。その後、各種類についてmin(合計, 上限C[i])を計算し、その合計を答えとする。

# Time Complexity: O(N + M)

N, M = map(int, input().split())
C = list(map(int, input().split()))
A = []
for i in range(N):
    B = list(map(int, input().split()))
    A.append(B)

t = [0] * (M)
ans = 0

for j in range(N):
    t[A[j][0]-1] += A[j][1]

for k in range(M):
    ans += min(t[k], C[k])

print(ans)