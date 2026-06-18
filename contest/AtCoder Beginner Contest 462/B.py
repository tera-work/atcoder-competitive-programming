# Problem: B (Gift)

# Contest: AtCoder Beginner Contest 462

# URL: https://atcoder.jp/contests/abc462/tasks/abc462_b

# Approach: 空の二次配列を作り、送り先の行に送り元の行番号を追加していく。

# Time Complexity: O(N^2)

n = int(input())
arr = [[] for _ in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(l[0]):
        arr[l[j+1]-1].append(i+1)

for k in range(n):
    arr[k].insert(0, len(arr[k]))
    ans = ' '.join(map(str, arr[k]))
    print(ans)