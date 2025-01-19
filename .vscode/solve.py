all_grade = [0 for i in range(20)]      # 입력값 넣을 빈 리스트 만들기
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
}
total_score = 0
for i in range(20):
    all_grade[i] = list(map(str, input().split()))      # 입력값을 리스트로 만들기
