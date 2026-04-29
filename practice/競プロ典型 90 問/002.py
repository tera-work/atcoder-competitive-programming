# Problem: 002 (Encyclopedia of Parentheses（★3）)

# Contest: 競プロ典型 90 問

# URL: https://atcoder.jp/contests/typical90/tasks/typical90_b

# Approach: 入力数と(、)の合計数が同じになる組み合わせを全探索して見つける

# Time Complexity: O(N × 2^N)

N = int(input())

if N % 2 != 0:
    print("")
    exit()

else:
    for i in range(2 ** N):
        candidate = ""
        score = 0
        is_ok = True

        for j in range(N - 1, -1, -1):
            if (i >> j) & 1 == 0:
                candidate += "("
                score += 1
            else:
                candidate += ")"
                score -= 1
            
            if score < 0:
                is_ok = False
                break
        
        if is_ok and score == 0:
            print(candidate)