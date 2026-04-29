# Problem: 038 (Large LCM（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_al

# Approach: math.lcmを用いて最小公倍数を求める。if文を用いて、その数が10^18を超える場合はLargeを、超えない場合は最小公倍数を出力する。

# Time Complexity: O(log(min(A,B)))

# 解説後理解:このコードのまま書くと、AとBが十分に大きい場合にオーバーフローするので、 掛ける前にオーバーフローするか判定する。

# 学び: 大きい数は作る前に防ぐ

import math

A, B = map(int, input().split())

ans = math.lcm(A, B)

if ans > 10 ** 18:
    print("Large")
else:
    print(ans)

# 解説のコード
import math

A, B = map(int, input().split())

g = math.gcd(A, B)

# 先に割る
A //= g

# 掛ける前にオーバーフローするか判定する
if A > 10**18 // B:
    print("Large")
else:
    print(A * B)