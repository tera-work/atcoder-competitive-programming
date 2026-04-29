# Problem: 061 (Deck（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bi

# Approach: 空のdequeを作り、ti=1のときは最初に、ti=2のときは最後にxi追加する。ti=3のときはxiに書かれた数-1した位置にある数を出力する。

# Time Complexity: O(Q)

import sys
from collections import deque
input = sys.stdin.readline

Q = int(input())

S = deque()

for _ in range(Q):
    t, x = map(int, input().split())
    
    if t == 1:
        S.appendleft(x)
    elif t == 2:
        S.append(x)
    else:
        print(S[x-1])