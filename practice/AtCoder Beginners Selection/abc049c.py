# Problem: ABC049C (白昼夢)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/arc065_a

#  Approach: 入力された文字列を後ろから探索していき、与えられた文字列に該当した場合その文字列を消し続ける。

# Time Complexity: O(N)

S = input()

while True:
    if S.endswith("dreamer"):
        S = S[:-7]
    elif S.endswith("eraser"):
        S = S[:-6]
    elif S.endswith("dream"):
        S = S[:-5]
    elif S.endswith("erase"):
        S = S[:-5]
    else:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")