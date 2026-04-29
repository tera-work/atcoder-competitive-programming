# Problem: B (Sensor Data Logging)

# Contest: AtCoder Beginner Contest 453

# URL: https://atcoder.jp/contests/abc453/tasks/abc453_b

#  Approach: 「現時刻の測定値」と「直前に保存された測定値」との差の絶対値を計算し、それがXを超える場合のみ、その時の時刻と現時刻の測定値を出力する。

# Time Complexity: O(T)

T, X = map(int, input().split())
A = list(map(int, input().split()))

L = []
tmp = 0
for i in range(T+1):
    if i == 0 or abs(A[i] - tmp) >= X:
        tmp = A[i]
        L.append([i, A[i]])

for row in L:
    for x in row:
        print(x, end=" ")
    print()