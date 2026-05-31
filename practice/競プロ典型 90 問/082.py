# Problem: 082 (Counting Numbers（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_cd

# Approach: 文字の桁数ごとに分けて、書かれている文字の個数を求め、10^9+7で割った余りを出力する。

# Time Complexity: O(1)

l, r = map(int, input().split())

mod = 10 ** 9 + 7
ans = 0

for i in range(1, 20):
    start = 10 ** (i - 1)
    end = 10 ** i - 1
    
    start1 = max(l, start)
    end1 = min(r, end)
    
    if start1 <= end1:
        count = end1 - start1 + 1
        
        if (start1 + end1) % 2 == 0:
            tmp = ((start1 + end1) // 2) % mod * count
        else:
            tmp = (start1 + end1) % mod * (count // 2)
        
        ans += (tmp % mod) * i
        ans %= mod

print(ans)