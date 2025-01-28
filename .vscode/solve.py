
a = int(input())

original = a    # 초기값설정해서 새로운수와 비교할 수 있도록 저장
count = 0       # 몇번째 사이클인지 횟수세기

while True:
    # 첫 번째 자리와 두 번째 자리 분리
    tens = a // 10      # 몫으로 10의 자릿수 빼내기
    ones = a % 10       # 나머지 값으로 1의 자릿수 빼내기
    
    # 각 자리수의 합 계산
    new_number = tens + ones
    
    # 새로운 숫자 생성
    a = (ones * 10) + (new_number % 10)
        # 1의 자리를 10의자릿수로 변환  , 새로운수의 1의 자릿수
    # 사이클 카운트 증가
    count += 1
    
    # 원래 숫자로 돌아오면 종료
    if a == original:
        break

# 결과 출력
print(count)
