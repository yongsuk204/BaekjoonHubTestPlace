import sys
a = int(sys.stdin.readline())

ampty_list = [i for i in range(1, a+1)]    #1~a 까지 들어있는 리스트 생성

start_num = 0        # 시작 인덱스
end_num = a - 2      # 카드의 반복은 항상 주어진 숫자-2 만큼만 반복함
for _ in range(end_num):
    start_num += 1    # 건너뛰기
    ampty_list.append(ampty_list[start_num])    # 뒤로 넘기기
    start_num += 1    # 다음카드는 어떻게 할건지 대기
print(ampty_list[-1])    # 주어진숫자-2 만큼 반복해서 뒤로넘겨진 총 리스트의 맨 마지막(남은수)수