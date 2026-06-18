# Problem: C (Not Covered Points)

# Contest: AtCoder Beginner Contest 462

# URL: https://atcoder.jp/contests/abc462/tasks/abc462_c

#  Approach: 点をX座標で昇順ソートし、Y座標の最小値を更新する点だけが他の点に覆われないため、その個数を数える。

# Time Complexity: O(N log N)

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

l.sort(key=lambda x: x[0])
y = float('inf')
ans = 0

for i in range(n):
    if y > l[i][1]:
        ans += 1
        y = l[i][1]

print(ans)