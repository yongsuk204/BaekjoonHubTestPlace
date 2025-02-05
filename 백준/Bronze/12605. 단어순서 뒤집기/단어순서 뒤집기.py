# a = int(input())

# for i in range(a):
#     empty_list = ''
#     b = input().split()
#     # print(b)
#     for f in b[::-1]:
#         empty_list += f'{f} '
#     print(f'Case#{i+1}: {empty_list}')

a = int(input())        # 문자열 갯수

for i in range(a):      # 문자열 갯수만큼 반복
    b = input().split()     # 문자열을 스플릿해서 리스트로 패킹
    # print(b)
    empty_list = ' '.join(b[::-1])    # 리스트에 있는요소를 거꾸로, 하나로 합침, 합칠때 요소사이에 '공백'두기? 코로나 거리두기인가?
    print(f'Case #{i+1}: {empty_list}')     # 결과값 출력
    