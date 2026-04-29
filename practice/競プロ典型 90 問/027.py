# Problem: 027 (Sign Up Requests （★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_aa

# Approach:名前を集合setで管理する。各日について、名前がまだ集合に存在しない場合はその日付を出力し集合に追加する。

# Time Complexity: O(N)

import sys
input = sys.stdin.readline

N = int(input())
used_names = set()

for i in range(1, N + 1):
    S = input().strip()

    if S not in used_names:
        print(i)
        used_names.add(S)
