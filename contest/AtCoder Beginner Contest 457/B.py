# Problem: B (Arrays)

# Contest: AtCoder Beginner Contest 457

# URL: https://atcoder.jp/contests/abc457/tasks/abc457_b

# Approach: 配列のX行、Y列に位置にある要素を出力する。

# Time Complexity: O(1)

N = int(input())
a = [ list(map(int,input().split(" "))) for _ in range(N)]
X, Y = map(int, input().split())

print(a[X-1][Y])