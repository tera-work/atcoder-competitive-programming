# Problem: ABC085B (Kagami Mochi)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/abc085_b

#  Approach: 入力された配列を大きい順に並べ替え、大きさの異なる場合に答えに1を足していく

# Time Complexity: O(N log N)

N = int(input())
D = []
for i in range(N):
    A = int(input())
    D.append(A)

total = 1

D.sort(reverse=True)

for j in range(N-1):
    if D[j+1] != D[j]:
        total += 1

print(total)