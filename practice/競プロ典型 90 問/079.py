# Problem: 079 (Two by Two（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ca

# Approach: 変更を行える位置すべてのAとBの要素を比較して、変更が必要な場合変更する。最終的に、AがBと同じになるか判断する。

# Time Complexity: O(H * W)

h, w = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]

total = 0

for i in range(h-1):
    for j in range(w-1):
        tmp = A[i][j] - B[i][j]
        
        if tmp != 0:
            total += abs(tmp)
            A[i][j]     -= tmp
            A[i+1][j]   -= tmp
            A[i][j+1]   -= tmp
            A[i+1][j+1] -= tmp

if A == B:
    print("Yes")
    print(total)
else:
    print("No")