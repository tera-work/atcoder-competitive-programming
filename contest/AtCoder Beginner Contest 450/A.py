# Problem: A (3,2,1,GO)

# Contest: AtCoder Beginner Contest 450

# URL: https://atcoder.jp/contests/abc450/tasks/abc450_a

#  Approach: Nから1までの数列を作り、カンマ区切りで出力する

# Time Complexity: O(N)

## 学び: 出力はループで逐次行うより、joinでまとめた方が簡潔

N = int(input())

for i in range(N):
    temp = N-i
    print(temp,end="")
    if temp != 1:
       print(",",end="") 
