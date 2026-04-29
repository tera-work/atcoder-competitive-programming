# Problem: 032 (AtCoder Ekiden（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_af

# Approach: 全順序探索からダメなペアを削り、最も最小になる順序を求める

# Time Complexity: O(N! × N)

import itertools

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
bad = set()

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    bad.add((x, y))
    bad.add((y, x))

ans = float('inf')

for p in itertools.permutations(range(N)):
    ok = True
    
    for i in range(N-1):
        if (p[i], p[i+1]) in bad:
            ok = False
            break
    
    if not ok:
        continue
    
    total = 0
    for i in range(N):
        total += A[p[i]][i]
    
    ans = min(ans, total)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
