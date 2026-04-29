# Problem: ABC085C (Otoshidama)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/abc085_c

#  Approach: 入力された枚数になる組み合わせのうち、入力された値になる組み合わせの有無を確かめる

# Time Complexity: O(N^2)

N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N + 1 - i):
        k = N - i - j
        if 10000 * i + 5000 * j + 1000 * k == Y:
            print(i, j, k)
            exit()
            
print("-1 -1 -1")