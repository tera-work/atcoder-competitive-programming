# Problem: A (Armor)

# Contest: AtCoder Beginner Contest 461

# URL: https://atcoder.jp/contests/abc461/tasks/abc461_a

# Approach: AがD以上かどうかを判断し、Yes、Noを出力する。

# Time Complexity: O(1)

a, d = map(int, input().split())
if a <= d:
    print("Yes")
else:
    print("No")