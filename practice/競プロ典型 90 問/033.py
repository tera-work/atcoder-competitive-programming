# Problem: 033 (Not Too Bright（★2）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ag

# Approach: 2×2のLEDができる場合とできない場合に分け、HとWの単純な計算と2の切り上げ割り算を行う

# Time Complexity: O(1)

H, W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
else:
    print(((H + 1) // 2) * ((W + 1) // 2))