"""
【問題文】
N 個の部屋（部屋 0 から 部屋 N-1）と、M 本の廊下があります。廊下 i は部屋 A_i と部屋 B_i を双方向に結んでいます。
あなたは部屋 $0$ から出発して、廊下を通って他の部屋へ移動します。
部屋 0 からそれぞれの部屋にたどり着くために通る廊下の最小本数を求めてください。
ただし、どうしてもたどり着けない部屋については -1 を出力してください。
"""

# Approach: 幅優先探索で、最短経路で行ける距離を求めて出力する

# Time Complexity: O(N + M)

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)

dist = [-1] * n
q = deque()

dist[0] = 0
q.append(0)

while q:
    v = q.popleft()
    
    for next_v in g[v]:
        if dist[next_v] == -1:
            dist[next_v] = dist[v] + 1
            q.append(next_v)

for d in dist:
    print(d)