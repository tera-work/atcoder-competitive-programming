# Problem: B (The Honest Woodcutters)

# Contest: AtCoder Beginner Contest 461

# URL: https://atcoder.jp/contests/abc461/tasks/abc461_b

# Approach: 各要素番号iについて、A[i]が指す位置のBの値がi+1であるかを確認する。

# Time Complexity: O(N)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ok = "Yes"

for i in range(n):
    if b[a[i]-1] != i+1:
        ok = "No"
        break

print(ok)