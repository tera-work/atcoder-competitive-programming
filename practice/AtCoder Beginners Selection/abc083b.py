# Problem: ABC083B (Some Sums)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/abc083_b

#  Approach: 1からNまでの各整数について桁和を求め、その値がA以上B以下ならその整数を合計に加える

# Time Complexity: O(N)

N, A, B = map(int, input().split())

ans = 0

for i in range(1,N+1):
    temp = i
    total = 0
    while temp > 0:
        total += temp % 10
        temp //= 10

    if A <= total <= B:
        ans += i

print(ans)
