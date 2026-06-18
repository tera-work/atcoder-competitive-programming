# Problem: C (Not Adjacent)

# Contest: AtCoder Beginner Contest 456

# URL: https://atcoder.jp/contests/abc456/tasks/abc456_c

# Approach: 文字列を左から順に見ていき、直前と異なる文字が続く区間の長さを管理しながら、各位置で作れる条件を満たす部分文字列の数を累積する。

# Time Complexity: O(N)

S = list(input())

tmp = 0
ans = 0

for i in range(len(S)):
    if i == 0 or S[i-1] != S[i]:
        tmp += 1
        ans += tmp

    else:
        ans += 1
        tmp = 1

print(ans % 998244353)
