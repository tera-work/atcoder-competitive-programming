# Problem: 046 (I Love 46（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_at

# Approach: A,B,Cの要素をそれぞれ46で割った余りの数をリストにする。そのリストをもとに合計が46の倍数と組み合わせの数を求める。

# Time Complexity: O(N)

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cntA = [0] * 46
cntB = [0] * 46
cntC = [0] * 46

for x in A: 
    cntA[x % 46] += 1
for x in B: 
    cntB[x % 46] += 1
for x in C: 
    cntC[x % 46] += 1

ans = 0

for i in range(46):
    for j in range(46):
        k = (-i - j) % 46
        if (i + j + k) % 46 == 0:
            ans += cntA[i] * cntB[j] * cntC[k]

print(ans)