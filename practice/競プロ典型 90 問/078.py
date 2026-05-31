# Problem: 078 (Easy Graph Problem（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bz

# Approach: 隣接リストを作成し、条件に合う頂点の数を最後に求める。

# Time Complexity: O(N + M)

N, M = map(int, input().split())

l = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    
    l[a].append(b)
    l[b].append(a)

cnt = 0

for j in range(1, N+1):
    tmp = 0
    for k in l[j]:
        if j > k:
            tmp += 1

    if tmp == 1:
        cnt +=1

print(cnt)