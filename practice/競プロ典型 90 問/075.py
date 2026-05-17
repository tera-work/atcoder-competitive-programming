# Problem: 075 (Magic For Balls（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bw

# Approach: 素数で割れる可能性のある範囲で割れる個数を探す。その数が2の何乗の範囲で行えるかを調べる。

# Time Complexity: O(√N)

N = int(input())

cnt = 0

p = 2
while p * p <= N:
    while N % p == 0:
        cnt += 1
        N //= p
    p += 1

if N > 1:
    cnt += 1

ans = 0
x = 1

while x < cnt:
    x *= 2
    ans += 1

print(ans)