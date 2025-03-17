import sys

# 입력 받기
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# DP 테이블 초기화
dp = [1] * n

# LIS 계산
for i in range(1, n):
    # print(i)
    for j in range(i):
        if arr[j] < arr[i]:  # 증가하는 경우
            dp[i] = max(dp[i], dp[j] + 1)


# 가장 긴 부분 수열의 길이 출력
print(max(dp))


