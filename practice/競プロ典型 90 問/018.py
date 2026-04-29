# Problem: 018 (Statue of Chokudai（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_r

# Approach: 入力された時間の座標を求め、高橋直大像との角度を求める

# Time Complexity: O(Q)

import sys
input = sys.stdin.readline
import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
R = L / 2
for i in range(Q):
    E = int(input())

    temp = math.pi * 2 * E / T
    temp_y = -R * math.sin(temp)
    temp_z = R - R * math.cos(temp)

    dist = math.sqrt(X ** 2 + (Y - temp_y) ** 2)
    rad = math.atan2(temp_z, dist)

    print(math.degrees(rad))