# Problem: B (456)

# Contest: AtCoder Beginner Contest 456

# URL: https://atcoder.jp/contests/abc456/tasks/abc456_b

# Approach: それぞれのサイコロで4,5,6がでる確率を調べて結果を出力する。

# Time Complexity: O(1)

# 改善すべき点: コードが冗長で間違えやすく、応用しにくい

tmp = 1

A_1 = list(map(int, input().split()))

tmp4_1 = A_1.count(4) / 6
tmp5_1 = A_1.count(5) / 6
tmp6_1 = A_1.count(6) / 6

A_2 = list(map(int, input().split()))

tmp4_2 = A_2.count(4) / 6
tmp5_2 = A_2.count(5) / 6
tmp6_2 = A_2.count(6) / 6

A_3 = list(map(int, input().split()))

tmp4_3 = A_3.count(4) / 6
tmp5_3 = A_3.count(5) / 6
tmp6_3 = A_3.count(6) / 6

ans = tmp4_1 * (tmp5_2 * tmp6_3 + tmp6_2 * tmp5_3) + tmp4_2 * (tmp5_1 * tmp6_3 + tmp6_1 * tmp5_3) + tmp4_3 * (tmp5_1 * tmp6_2 + tmp6_1 * tmp5_2)

print(ans)

# 改善コード

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

cnt = 0

for a in A1:
    for b in A2:
        for c in A3:
            if sorted([a, b, c]) == [4, 5, 6]:
                cnt += 1

print(cnt / 216)
