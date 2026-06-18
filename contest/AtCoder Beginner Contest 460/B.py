# Problem: B (Two Ringse)

# Contest: AtCoder Beginner Contest 460

# URL: https://atcoder.jp/contests/abc460/tasks/abc460_b

# Approach: 2つの円の中心間距離の二乗 d² を求める。接する条件(r1-r2)² ≤ d² ≤ (r1+r2)²を満たすか判定する。

# Time Complexity: O(T)

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (r1 - r2) ** 2 <= (((x1 - x2) ** 2) + ((y1 - y2) ** 2))  <= (r1 + r2) ** 2:
        print("Yes")
    else:
        print("No")