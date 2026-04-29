# Problem: ABC086C (Traveling)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/arc089_a

#  Approach: 入力時間内に目的地に移動できるかを求め結果を出力する

# Time Complexity: O(N)

N = int(input())
A = [[0, 0, 0]]
for i in range(N):
    A.append(list(map(int, input().split())))

for j in range(N):
    t_diff = A[j+1][0] - A[j][0]
    dist = abs(A[j+1][1] - A[j][1]) + abs(A[j+1][2] - A[j][2])

    if dist > t_diff:
        print("No")
        exit()
    
    if (t_diff - dist) % 2 != 0:
        print("No")
        exit()

print("Yes")