import sys

dp = [[[None] * 21 for _ in range(21)] for _ in range(21)]  # 3차원 리스트 생성
# x,y,z 축으로 0~20 까지숫자의 21개를 만든다 / 0번째는 사실상 1 이기 때문 / 실질적으로 1~20번째 칸에 의미있는 숫자를 집어넣는다.

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if dp[a][b][c] is not None:  # 이미 계산한 값이 있으면 바로 반환
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return dp[a][b][c]  # 계산한 값을 저장 후 반환

while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

# import sys

# while not a==-1 and b==-1 and c==-1:
#     a,b,c = map(int, sys.stdin.readline().split())
#     print(w(a,b,c))