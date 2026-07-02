# Problem: A (16:9)

# Contest: AtCoder Beginner Contest 463

# URL: https://atcoder.jp/contests/abc463/tasks/abc463_a

# Approach: Xの9倍とYの16倍が同じか判断する。

# Time Complexity: O(1)

x, y = map(int, input().split())

if x * 9 == y * 16:
    print("Yes")
else:
    print("No")