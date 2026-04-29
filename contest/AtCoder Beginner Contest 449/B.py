# Problem: B (Deconstruct Chocolate)

# Contest: AtCoder Beginner Contest 449

# URL: https://atcoder.jp/contests/abc449/tasks/abc449_b

#  Approach: queryの一列目に応じて、二列目を行か列から引いていく

# Time Complexity: O(Q)

H, W, Q = map(int, input().split())

for i in range(Q):
    t, n = map(int, input().split())
    if t == 1:
        print(n * W)
        H = H - n
    else:
        print(n * H)
        W = W - n