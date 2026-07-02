# Problem: B (Train Reservation)

# Contest: AtCoder Beginner Contest 463

# URL: https://atcoder.jp/contests/abc463/tasks/abc463_b

# Approach: Xの文字から配列のどの列を予約したいのかを判断し、全探索で予約可能か判断する。

# Time Complexity: O(N)

x, y = map(int, input().split())

n, x = input().split()

if x == 'A':
    X = 1
elif x == 'B':
    X = 2
elif x == 'C':
    X = 3
elif x == 'D':
    X = 4
elif x == 'E':
    X = 5

tmp = "No"
for _ in range(int(n)):
    s = list(input())
    if s[X-1] == 'o':
        tmp = "Yes"
        break
print(tmp)