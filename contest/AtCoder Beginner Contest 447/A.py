# Problem: A (Seats 2)

# Contest: AtCoder Beginner Contest 447

# URL: https://atcoder.jp/contests/abc447/tasks/abc447_a

# Approach: 入力された数が奇数か偶数かによって分岐させ、範囲を定める

# Time Complexity: O(N)

# 解説後理解：分岐数を減らし、短く記述する本質を理解した

# 本質：M * 2 -1 <= Nで求められる問題だった

N, M = map(int, input().split())

if N % 2 == 0:
    if N // 2 >= M:
        print("Yes")
    else:
        print("No")

else:
    if N // 2 + 1 >= M:
        print("Yes")
    else:
        print("No")