import sys
input = sys.stdin.readline
output = sys.stdout.write

# 테스트 케이스 개수 입력
T = int(input())

# 결과 저장 리스트
results = []

# T번 반복하며 입력받기
for _ in range(T):
    A, B = map(int, input().split())
    results.append(A + B)

# 결과 출력
output("\n".join(map(str, results)) + "\n")