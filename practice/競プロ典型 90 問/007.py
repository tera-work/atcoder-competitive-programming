# Problem: 007 (CP Classes（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_g

# Approach: 与えられた数がどの大きさに近いかを求め、その数との絶対値を求める

# Time Complexity: O(N log N + Q log N)

import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())

for i in range(Q):
    b = (int(input()))

    idx = bisect.bisect_left(A, b)
    
    res = float('inf')
    
    if idx < N:
        res = min(res, abs(A[idx] - b))
        
    if idx > 0:
        res = min(res, abs(A[idx-1] - b))
        
    print(res)