# Problem: B (Mapping)

# Contest: AtCoder Beginner Contest 454

# URL: https://atcoder.jp/contests/abc454/tasks/abc454_a

#  Approach: 質問１を判断するために、人数と着られている服の種類が同じかどうかを調べる。また質問２を判断するために、服の種類と着ている服の種類が同じかどうか調べる。

# Time Complexity: O(1)

import collections

N, M = map(int, input().split())

F = list(map(int, input().split()))
c = collections.Counter(F)

if len(c) == N:
    print("Yes")
else:
    print("No")

if len(c) == M:
    print("Yes")
else:
    print("No")