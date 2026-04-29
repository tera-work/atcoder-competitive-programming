# Problem: ABC081B (Shift only)

# Contest: AtCoder Beginners Selection

# URL: https://atcoder.jp/contests/abs/tasks/abc081_b

#  Approach: すべての要素が偶数である間、各要素を2で割り続け、その割った回数を数え出力する

# Time Complexity: O(N × logA)

N = int(input())
A = list(map(int, input().split()))

count = 0

while True:
    for i in range(N):
        if A[i] % 2 == 1:
            print(count)
            exit()
        
        else:
            A[i] //= 2
          
    count += 1