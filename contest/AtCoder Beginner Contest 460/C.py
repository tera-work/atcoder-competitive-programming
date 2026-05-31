# Problem: C (Sushi)

# Contest: AtCoder Beginner Contest 460

# URL: https://atcoder.jp/contests/abc460/tasks/abc460_c

#  Approach: 尺取り法を使って、AとBの組み合わせの数を求める。

# Time Complexity: O( NlogN + MlogM )

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

j = 0
count = 0

for x in a:
    if j < m and x * 2 >= b[j]:
        count += 1
        j += 1

print(count)