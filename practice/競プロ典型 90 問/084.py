# Problem: 084 (There are two types of characters（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_cf

# Approach: AとBという空の配列を持ち、oとxが出た最新の位置を把握し続け、小さい方の値を合計していく。

# Time Complexity: O(N)

N = int(input())
S = list(input())

A = [0] * (N + 1)
B = [0] * (N + 1)
    
for i in range(1, N + 1):
    if S[i - 1] == 'o':
        A[i] = i
        B[i] = B[i - 1]
    else:
        A[i] = A[i - 1]
        B[i] = i
            
ans = 0

for i in range(1, N + 1):
    ans += min(A[i], B[i])
        
print(ans)