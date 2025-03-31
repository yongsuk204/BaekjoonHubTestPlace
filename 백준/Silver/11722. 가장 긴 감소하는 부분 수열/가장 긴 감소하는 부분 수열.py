len_1 = int(input())

A = list(map(int, input().split()))

dp = [1] * len_1

for i in range(len_1):
    for g in range(i):
        if A[g] > A[i]:
            dp[i] = max(dp[i], dp[g]+1)

print(max(dp))