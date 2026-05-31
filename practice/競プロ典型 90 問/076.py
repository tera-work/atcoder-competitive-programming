# Problem: 076 (Cake Cut（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bx

# Approach: 尺取り法を用いて、効率的に全探索を行う。

# Time Complexity: O(N)

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

total = sum(A)

if total % 10 != 0:
    print("No")
    exit()

A2 = A + A
ave = sum(A) // 10
ans = "No"

current = 0
right = 0

for i in range(N):

    while current < ave:
        current += A2[right]
        right += 1
    
    if current == ave:
        ans = "Yes"
        break

    current -= A2[i]

print(ans)
