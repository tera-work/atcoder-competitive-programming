# Problem: A (Trimo)

# Contest: AtCoder Beginner Contest 453

# URL: https://atcoder.jp/contests/abc453/tasks/abc453_a

# Approach: 文字列を配列として受け取り、配列の先頭に連続してでてくるoを除いていき、o以外がでた時点で残りを文字列に戻して出力する。

# Time Complexity: O(N)

# 学び: remove()は重たいのでできるだけ使わない方が良い

N = int(input())
S = list(input())

for i in range(N):
    if S[0] == "o":
        S.remove("o")
    else:
        break

S = ''.join(map(str, S))
print(S)

