# Problem: 050 (Stair Jump（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ax

# Approach: N+1サイズの配列を作る。その配列がどのようにその時点の位置に来れるかを足していく。

# Time Complexity: O(N)

N, L = map(int, input().split())

mod = 10**9 + 7

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    dp[i] = dp[i-1]
    
    if i >= L:
        dp[i] = (dp[i] + dp[i-L]) % mod

print(dp[N])