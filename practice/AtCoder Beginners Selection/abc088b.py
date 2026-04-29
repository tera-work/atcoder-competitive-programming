# Problem: ABC088B (Some Card Game for Two)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/abc088_b

#  Approach: 入力枚数のカードのうち大きい順に、AliceとBobにカードの値を足していき、その差を計算

# Time Complexity: O(N^2)

N = int(input())
A = list(map(int, input().split()))

num = N
a = 0
b = 0

for i in range(N // 2):
    temp_a_num = 0
    for j in range(len(A)):
        if A[temp_a_num] < A[j]:
            temp_a_num = j
    a += A.pop(temp_a_num)

    if not A:
        break

    temp_b_num = 0
    for k in range(len(A)):
        if A[temp_b_num] < A[k]:
            temp_b_num = k
    b += A.pop(temp_b_num)

if A:
    a += A.pop(0)

print(a - b)