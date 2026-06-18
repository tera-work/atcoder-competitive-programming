# Problem: A (Secret Numbers)

# Contest: AtCoder Beginner Contest 462

# URL: https://atcoder.jp/contests/abc462/tasks/abc462_a

# Approach: 入力された文字列を一文字目から順に数字であるか判断し、数字のみ出力する。

# Time Complexity: O(|S|)

s = list(input())

ans = []

for i in range(len(s)):
    if s[i] == "0":
        ans.append(0)
    if s[i] == "1":
        ans.append(1)
    if s[i] == "2":
        ans.append(2)
    if s[i] == "3":
        ans.append(3)
    if s[i] == "4":
        ans.append(4)
    if s[i] == "5":
        ans.append(5)
    if s[i] == "6":
        ans.append(6)
    if s[i] == "7":
        ans.append(7)
    if s[i] == "8":
        ans.append(8)
    if s[i] == "9":
        ans.append(9)

ans = ''.join(map(str, ans))
print(ans)

# より簡潔な参考コード:

s = input()
t = ""
for c in s:
    if c.isdigit():
        t += c
print(t)
