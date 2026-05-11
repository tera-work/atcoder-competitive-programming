# Problem: A (Array)

# Contest: AtCoder Beginner Contest 457

# URL: https://atcoder.jp/contests/abc457/tasks/abc457_a

#  Approach: 配列のX番目に位置にある要素を出力する。

# Time Complexity: O(1)

N = int(input())
A = list(map(int, input().split()))
X = int(input())

print(A[X-1])