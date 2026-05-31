# Problem: A (459)

# Contest: AtCoder Beginner Contest 459

# URL: https://atcoder.jp/contests/abc459/tasks/abc459_b

#  Approach: 文字列の頭文字を空の配列に判定をしながら追加していき、最後に文字列に変換して出力する。

# Time Complexity: O(N)

# 学び： 文字参照は辞書を使うと簡潔に行える。

n = int(input())
s = input().split()

ans = []

for i in range(n):
    tmp = ''.join(s[i])
    if tmp[0] == "a" or tmp[0] == "b" or tmp[0] == "c":
        ans.append(2)
    if tmp[0] == "d" or tmp[0] == "e" or tmp[0] == "f":
        ans.append(3)
    if tmp[0] == "g" or tmp[0] == "h" or tmp[0] == "i":
        ans.append(4)
    if tmp[0] == "j" or tmp[0] == "k" or tmp[0] == "l":
        ans.append(5)
    if tmp[0] == "m" or tmp[0] == "n" or tmp[0] == "o":
        ans.append(6)
    if tmp[0] == "p" or tmp[0] == "q" or tmp[0] == "r" or tmp[0] == "s":
        ans.append(7)
    if tmp[0] == "t" or tmp[0] == "u" or tmp[0] == "v":
        ans.append(8)
    if tmp[0] == "w" or tmp[0] == "x" or tmp[0] == "y" or tmp[0] == "z":
        ans.append(9)

ans = ''.join(map(str, ans))
print(ans)

# 参考コード：
n = int(input())
s = input().split()

ans = []

for word in s:
    c = word[0]

    if c in "abc":
        ans.append("2")
    elif c in "def":
        ans.append("3")
    elif c in "ghi":
        ans.append("4")
    elif c in "jkl":
        ans.append("5")
    elif c in "mno":
        ans.append("6")
    elif c in "pqrs":
        ans.append("7")
    elif c in "tuv":
        ans.append("8")
    else:
        ans.append("9")

print(''.join(ans))