# Problem: A (Dice)

# Contest: AtCoder Beginner Contest 456

# URL: https://atcoder.jp/contests/abc456/tasks/abc456_a

#  Approach: Xの値がすべて1のでたときからすべて6がでたときの値の範囲内にあるか調べる。

# Time Complexity: O(1)

X = int(input())

if 3 <= X <= 18:
    print("No")
else:
    print("Yes")