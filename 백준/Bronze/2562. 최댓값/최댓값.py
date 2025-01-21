# 숫자 입력 받기
numbers = [int(input()) for _ in range(9)]

# 최댓값과 그 위치 찾기
max_value = max(numbers)
max_index = numbers.index(max_value) + 1  # 인덱스는 0부터 시작하므로 1을 더함

# 출력
print(max_value)
print(max_index)