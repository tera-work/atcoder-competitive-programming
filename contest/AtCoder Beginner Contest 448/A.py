# Problem: A (chmin)

# Contest: AtCoder Beginner Contest 448

# URL: https://atcoder.jp/contests/abc448/tasks/abc448_a

# Approach: 入力された数Xを保持し、A[i]<XのときXを更新して1を出力、それ以外は0を出力する

# Time Complexity: O(N)

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        X = A[i]
        print(1)
    else:
        print(0)