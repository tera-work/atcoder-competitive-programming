# Problem: 044 (Shift and Swapping（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ar

# Approach: Tによって、dequeを適切に処理する

# Time Complexity: O(Q)

# 解説後理解: 今回rotateでT==2の操作を行ったが、毎回データを動かしているため無駄がある。shiftを使うことで配列を動かさずに管理できる。

import sys
input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
A = list(map(int, input().split()))

temp_list = deque(A)

for _ in range(Q):
    T, x, y = map(int, input().split())

    if T == 1:
        temp = temp_list[x-1]
        temp_list[x-1] = temp_list[y-1]
        temp_list[y-1] = temp
    elif T == 2:
        temp_list.rotate(1)
    else:
        print(temp_list[x-1])