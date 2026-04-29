# Problem: 016 (Minimum Coins（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_p

# Approach: 制約の範囲内でループを行い、最小値を更新し続ける

# Time Complexity: O(10000^2)

import sys
input = sys.stdin.readline

N = int(input())
C = list(map(int, input().split()))

C.sort(reverse=True)

temp_ans = 10 ** 9

for i in range(10000):
    for j in range(10000 - i):
        rem = N - (C[0] * i + C[1] * j)
        
        if rem < 0:
            break
            
        if rem % C[2] == 0:
            k = rem // C[2]
            if i + j + k < temp_ans:
                temp_ans = i + j + k

print(temp_ans)
