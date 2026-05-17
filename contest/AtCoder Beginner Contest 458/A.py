# Problem: A (Chompers)

# Contest: AtCoder Beginner Contest 458

# URL: https://atcoder.jp/contests/abc458/tasks/abc458_a

#  Approach: 文字列SのN+1文字目からlen(S)-N文字目までを出力する。

# Time Complexity: O(|S|)

S = input()
N = int(input())

print(S[N:-N])