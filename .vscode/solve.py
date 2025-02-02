def is_sosu(n):     # 소수인지 확인하는 함수만들기기
    if n < 2:       # 0,1 은 소수가 아님님
        return False
    for i in range(2, int(n**0.5) + 1):     # 2부터 제곱근 까지
        if n % i == 0:      # 나눠서 0이 된다는건 나눠진다는것이기때문에 소수가 아님
            return False    # 2부터 제곱근까지 모두 나눠보았을때 나눠지는게 하나라도 있으면 소수가 아님 판정정
    return True     # 2부터 제곱근까지 모두 나눠보았을때 나눠지는게 모두 없으면 소수로 판정 / if문 안으로 else: 로해서 들어가면, 나눠지는게 있어도 소수판정하는 오류가 있음 그래서 조건문 밖으로 빼야함

def is_palin(n):    # 팰린드롬숫자인지 확인하는 함수만들기
    if str(n) == str(n)[::-1]:      # n은 int로 입력되기때문에 문자열로 바꿔서 거꾸로해도 동일한경우 True판정
        return True
    

n = int(input())        # 입력값 받아오기

while True:
    if is_sosu(n) and is_palin(n):      # 두가지 함수에서 True가 리턴되어야 조건문성립,
        print(n)        # 두 조건을 만족하는 n 출력
        break       # 조건을 찾았으니 반복문 종료
    n+=1    # 두조건을 만족하지 못하는 n 이기때문에 다음숫자로 다시진행행