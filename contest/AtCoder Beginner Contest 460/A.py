# Problem: A (Mod While Positive)

# Contest: AtCoder Beginner Contest 460

# URL: https://atcoder.jp/contests/abc460/tasks/abc460_a

#  Approach: 指定された指示をwhile文でcountを1足しながら行い、最後にcountの値を出力する。

# Time Complexity: O(M)

n, m = map(int, input().split())
count = 0

while m != 0:
    x = n % m
    m = x
    count += 1 

print(count)