# Problem: C (C Stands for Center)

# Contest: AtCoder Beginner Contest 458

# URL: https://atcoder.jp/contests/abc458/tasks/abc458_c

# Approach: 文字Cが中央になるような奇数文字の部分文字列の数を、それぞれのCから求め合計を出力する。

# Time Complexity: O(|S|)

S = list(input())
count = 0

for i in range(len(S)):
    if S[i] == "C":
        count += min(i, len(S) -1 - i) + 1
        
print(count)
