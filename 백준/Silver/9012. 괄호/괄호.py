a = int(input())  # 몇 개의 괄호 문자열을 입력받을지

for _ in range(a):  # a개 만큼 반복함
    b = input()  # 괄호 문자열 입력
    empty_list = []  # '('의 갯수와 ')' 갯수를 맞추기위해 임시로 넣을 빈공간 만듬
    is_empty_list = True  # 입력된 b 가 True라고 가정함

    for i in b :    # 입력된 b의 괄호문을 하나하나 가져옴
        #print(i)
        if i == '(':    # 괄호문요소가 ( 인경우,
            empty_list.append(i)    # 빈리스트에 ( 를 채움
        elif i == ')':  # 괄호문요소가 ) 인경우,
            if empty_list:      # 리스트에 요소가 있으면
                empty_list.pop()  # 넣었던 ( 를 제거
            else:       # ( 를 제거해야하는데 없다는말은 ( 와 ) 의 갯수가 다르거나, 순서가 바뀌었음 = VPS가 아님
                print("NO")  # 올바르지 않은 경우 즉시 NO 출력
                is_empty_list = False   # 리스트에 아무것도 없기때문에
                break  # 검사 중단
    if is_empty_list:
        if empty_list:      # is_empty_list = True 라고 하더라도 리스트가 있을수도 있고 없을 수도 있기때문에,
            print('NO')
        else:
            print('YES')
    else:
        continue        # 이미 NO라고 출력했기때문에 지나침