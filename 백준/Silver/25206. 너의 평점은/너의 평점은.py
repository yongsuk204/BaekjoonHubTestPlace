all_grade = [0 for i in range(20)]      # 입력값 넣을 0으로된 빈 리스트 만들기
all_score =  {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}        # 학점표 만들기
total_score = 0        # 학점평균 총합
total_number = 0        # 단위학점 총합

for i in range(20):        # 과목갯수 20개 ( 0~ 19 )
    all_grade[i] = list(map(str, input().split()))      # 공백없이 문자열화된 입력값을 리스트로 만들기

for i in range(20):     # 리스트 인덱스위치 0~19
    if all_grade[i][2] == "P":        # [학과명, 단위학점, 학점] 으로 이루어진 리스트에서 학점에 해당하는부분이 P일때 반영 안되게 하기위해서 지나감 
        pass
    else:                        # 이부분에 int()를 씌우면 소수점 사라짐(정수*실수 가능하긴함)
        total_score += all_score[all_grade[i][2]]*float(all_grade[i][1])      # 학점평균총합
        total_number += float(all_grade[i][1])      # 단위학점 총합
        result = total_score / total_number

print(f'{result:5f}')        # 소수점 컷