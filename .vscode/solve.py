import sys

dp = [1,1,1] + [None] * 36

def fib(n):
    if dp[n]:
        return dp[n]
    else:
        dp[n] = fib(n - 1) + fib(n - 2)
        return  dp[n]
    

print(fib(30))
print(dp)