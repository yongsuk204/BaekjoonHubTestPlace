while True:
    a = input()
    str_save = a
    if a == '0':
        break
    elif a[::-1] == str_save:
        print('yes')
    else:
        print('no')