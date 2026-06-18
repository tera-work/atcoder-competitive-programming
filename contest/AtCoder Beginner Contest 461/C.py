# Problem: C (Variety)

# Contest: AtCoder Beginner Contest 461

# URL: https://atcoder.jp/contests/abc461/tasks/abc461_c

# Approach: Vの値が大きい順に並べ替え、選択済みの色を集合で管理しながら価値の高い商品から順に選び、重複色をK−M個まで許容してK個の商品を選ぶことで価値の総和を求める。

# Time Complexity: O(N log N)

import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

l.sort(key=lambda x: x[1], reverse=True)
s = set()
cnt = 0
tmp = 0

for i in range(n):
    c, v = l[i]
    if k - m > cnt:
        tmp += v
        if c in s:
            cnt += 1
        s.add(c)
        

    elif c not in s:
        s.add(c)
        tmp += v

    if len(s) + cnt == k:
        break
print(tmp)
