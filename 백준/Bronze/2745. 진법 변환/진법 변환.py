# 입력 받기
b, n = input().split()
n = int(n)  # B진법
b = str(b)  # N을 문자열로 저장

def convert_to_decimal(num_str, base):
    decimal = 0
    # 각 자리수별로 계산
    for i, digit in enumerate(reversed(num_str)):
        # 알파벳인 경우 숫자로 변환 (A=10, B=11, ...)
        if digit.isalpha():
            value = ord(digit.upper()) - ord('A') + 10
        else:
            value = int(digit)
        
        # B진법의 각 자리를 10진법으로 변환하여 더함
        decimal += value * (base ** i)
    
    return decimal

# 결과 출력
result = convert_to_decimal(b, n)
print(result)