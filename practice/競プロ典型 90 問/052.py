# Problem: 052 (Dice Product（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_az

# Approach: 各行の和をかけたものを、10^9 +7で割った余りを出力する。

# Time Complexity: O(N)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

mod = 10**9 + 7
ans = 1

for i in range(N):
    ans *= sum(A[i])
    ans %= mod

print(ans)